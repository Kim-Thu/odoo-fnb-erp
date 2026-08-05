#!/usr/bin/env python3
"""Local autonomous task runner for the Odoo F&B ERP repository.

This script does not automate the ChatGPT web UI. It invokes Codex CLI in
non-interactive mode, inspects GitHub through the `gh` CLI, and advances one
small backlog task at a time.

Safe defaults:
- dry-run unless --apply is supplied;
- no automatic merge unless AGENT_ALLOW_MERGE=1;
- one process at a time through an advisory lock;
- stop when the repository is dirty or a command fails unexpectedly.
"""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = REPO_ROOT / ".git" / "codex-task-runner.lock"
LOG_DIR = REPO_ROOT / ".agent-logs"
PLAN_PATH = REPO_ROOT / "MASTER_TASK_PLAN.md"
RULES_PATH = REPO_ROOT / "docs" / "DEVELOPMENT_RULES.md"
DEFAULT_INTERVAL_SECONDS = 20 * 60
BRANCH_PATTERN = re.compile(
    r"^(feat|fix|refactor|test|docs|ci|maint|security|performance)/"
    r"T\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*-\d{8}-\d{4}$"
)
TASK_ROW_PATTERN = re.compile(
    r"^\|\s*(T\d{4})\s*\|\s*([a-z]+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(\w+)\s*\|$"
)


class RunnerError(RuntimeError):
    """Raised when the runner must stop safely."""


@dataclass(frozen=True)
class Task:
    task_id: str
    task_type: str
    title: str
    dependencies: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class PullRequest:
    number: int
    branch: str
    url: str
    checks: tuple[dict[str, Any], ...]


def run(
    args: list[str],
    *,
    check: bool = True,
    capture: bool = True,
    cwd: Path = REPO_ROOT,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        capture_output=capture,
        check=False,
    )
    if check and result.returncode != 0:
        command = " ".join(shlex.quote(arg) for arg in args)
        raise RunnerError(
            f"Command failed ({result.returncode}): {command}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result


def require_commands() -> None:
    for command in ("git", "gh", "codex"):
        result = run(["bash", "-lc", f"command -v {shlex.quote(command)}"], check=False)
        if result.returncode != 0:
            raise RunnerError(f"Missing required command: {command}")


def ensure_repo_ready() -> None:
    if not (REPO_ROOT / ".git").exists():
        raise RunnerError("Run inside a Git repository.")
    if not PLAN_PATH.exists() or not RULES_PATH.exists():
        raise RunnerError("MASTER_TASK_PLAN.md or DEVELOPMENT_RULES.md is missing.")
    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if status:
        raise RunnerError(
            "Repository has uncommitted changes. Commit, stash, or clean them before running."
        )


def gh_json(args: list[str]) -> Any:
    result = run(["gh", *args])
    try:
        return json.loads(result.stdout or "null")
    except json.JSONDecodeError as exc:
        raise RunnerError(f"Invalid JSON from gh: {exc}\n{result.stdout}") from exc


def current_open_pr() -> PullRequest | None:
    rows = gh_json(
        [
            "pr",
            "list",
            "--state",
            "open",
            "--author",
            "@me",
            "--limit",
            "20",
            "--json",
            "number,headRefName,url,statusCheckRollup",
        ]
    )
    for row in rows:
        branch = row.get("headRefName", "")
        if BRANCH_PATTERN.match(branch):
            return PullRequest(
                number=int(row["number"]),
                branch=branch,
                url=row["url"],
                checks=tuple(row.get("statusCheckRollup") or ()),
            )
    return None


def classify_checks(checks: tuple[dict[str, Any], ...]) -> str:
    if not checks:
        return "pending"
    states: list[str] = []
    for check in checks:
        state = str(check.get("conclusion") or check.get("state") or "").upper()
        states.append(state)
    if any(state in {"FAILURE", "ERROR", "CANCELLED", "TIMED_OUT", "ACTION_REQUIRED"} for state in states):
        return "failed"
    if all(state in {"SUCCESS", "NEUTRAL", "SKIPPED"} for state in states):
        return "success"
    return "pending"


def latest_failed_logs(branch: str) -> str:
    runs = gh_json(
        [
            "run",
            "list",
            "--branch",
            branch,
            "--limit",
            "1",
            "--json",
            "databaseId,status,conclusion",
        ]
    )
    if not runs:
        return "No workflow run found."
    run_id = str(runs[0]["databaseId"])
    result = run(["gh", "run", "view", run_id, "--log-failed"], check=False)
    logs = (result.stdout + "\n" + result.stderr).strip()
    return logs[-30_000:] if logs else "No failed logs were returned."


def parse_tasks() -> list[Task]:
    tasks: list[Task] = []
    for raw_line in PLAN_PATH.read_text(encoding="utf-8").splitlines():
        match = TASK_ROW_PATTERN.match(raw_line.strip())
        if not match:
            continue
        deps_raw = match.group(4).strip()
        dependencies = tuple(
            dep.strip() for dep in deps_raw.split(",") if dep.strip() and dep.strip() != "—"
        )
        tasks.append(
            Task(
                task_id=match.group(1),
                task_type=match.group(2),
                title=match.group(3),
                dependencies=dependencies,
                status=match.group(5),
            )
        )
    if not tasks:
        raise RunnerError("No task rows found in MASTER_TASK_PLAN.md.")
    return tasks


def next_eligible_task() -> Task | None:
    tasks = parse_tasks()
    statuses = {task.task_id: task.status for task in tasks}
    for task in tasks:
        if task.status != "todo":
            continue
        if all(statuses.get(dep) == "done" for dep in task.dependencies):
            return task
    return None


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return "-".join(slug.split("-")[:6]) or "task"


def branch_name(task: Task) -> str:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    prefix = task.task_type if task.task_type in {
        "feat",
        "fix",
        "refactor",
        "test",
        "docs",
        "ci",
        "maint",
        "security",
        "performance",
    } else "maint"
    return f"{prefix}/{task.task_id}-{slugify(task.title)}-{timestamp}"


def codex_exec(prompt: str, *, apply: bool) -> None:
    args = ["codex", "exec", "--ephemeral"]
    if apply:
        args.append("--full-auto")
    args.append(prompt)
    LOG_DIR.mkdir(exist_ok=True)
    log_path = LOG_DIR / f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
    with log_path.open("w", encoding="utf-8") as log_file:
        process = subprocess.Popen(
            args,
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        assert process.stdout is not None
        for line in process.stdout:
            print(line, end="")
            log_file.write(line)
        return_code = process.wait()
    if return_code != 0:
        raise RunnerError(f"Codex exited with code {return_code}. See {log_path}.")


def fix_failed_pr(pr: PullRequest, *, apply: bool) -> None:
    logs = latest_failed_logs(pr.branch)
    prompt = f"""
You are continuing task work in this repository.

Current PR: #{pr.number} ({pr.url})
Current branch: {pr.branch}
The latest CI checks failed. Fix only the root cause shown below.

Rules:
- Read MASTER_TASK_PLAN.md and docs/DEVELOPMENT_RULES.md first.
- Do not broaden the task scope.
- Do not disable security checks globally.
- Prefer narrow, Odoo-specific lint exceptions when justified.
- Run the smallest relevant local checks.
- Do not commit, push, merge, or edit GitHub settings; the wrapper handles Git operations.
- Do not add secrets, credentials, real data, sudo(), or raw SQL.

Failed logs:
---
{logs}
---
""".strip()
    codex_exec(prompt, apply=apply)


def implement_task(task: Task, *, apply: bool) -> str:
    new_branch = branch_name(task)
    if not BRANCH_PATTERN.match(new_branch):
        raise RunnerError(f"Generated invalid branch name: {new_branch}")
    if not apply:
        print(f"[dry-run] Would create branch: {new_branch}")
    else:
        run(["git", "fetch", "origin", "master"])
        run(["git", "checkout", "master"])
        run(["git", "pull", "--ff-only", "origin", "master"])
        run(["git", "checkout", "-b", new_branch])

    prompt = f"""
Implement exactly one backlog task in this repository.

Task ID: {task.task_id}
Type: {task.task_type}
Title: {task.title}
Dependencies: {', '.join(task.dependencies) or 'none'}
Branch: {new_branch}

Required process:
1. Read MASTER_TASK_PLAN.md, docs/DEVELOPMENT_RULES.md, and the relevant code/tests.
2. Implement only this task with the smallest coherent change.
3. Add or update focused tests required by the task and global rules.
4. Preserve Odoo ACL, record-rule, multi-company, ORM, and secret-handling rules.
5. Run the smallest relevant checks locally. Do not run the full Odoo suite unless necessary.
6. Update this task to `review` in MASTER_TASK_PLAN.md only when implementation and local checks are complete.
7. Do not commit, push, open a PR, merge, or edit GitHub settings; the wrapper handles Git operations.
8. If blocked or ambiguous, make no speculative code change and explain the blocker in the final output.
""".strip()
    codex_exec(prompt, apply=apply)
    return new_branch


def validate_changes() -> None:
    run([sys.executable, "-m", "compileall", "addons", "scripts"])
    if run(["bash", "-lc", "command -v ruff"], check=False).returncode == 0:
        run(["ruff", "check", "addons", "scripts"])


def commit_and_open_pr(task: Task, branch: str, *, apply: bool) -> None:
    status = run(["git", "status", "--porcelain"]).stdout.strip()
    if not status:
        raise RunnerError("Codex made no repository changes.")
    validate_changes()
    if not apply:
        print("[dry-run] Changes validated; would commit, push, and open a PR.")
        return

    run(["git", "add", "--all"])
    commit_message = (
        f"{task.task_type}({task.task_id}): {slugify(task.title).replace('-', ' ')}\n\n"
        "Changes:\n- Implement the scoped backlog task.\n\n"
        "Security:\n- Preserve repository security and multi-company rules.\n\n"
        "Tests:\n- Run focused syntax, lint, and task-specific checks."
    )
    run(["git", "commit", "-m", commit_message])
    run(["git", "push", "--set-upstream", "origin", branch])
    title = f"{task.task_type}({task.task_id}): {slugify(task.title).replace('-', ' ')}"
    body = (
        f"## Task\n- {task.task_id} — {task.title}\n\n"
        "## Changes\n- Implemented the scoped task from MASTER_TASK_PLAN.md.\n\n"
        "## Security\n- No secrets added.\n- Reviewed ACL, record-rule, sudo(), raw SQL, and multi-company impact.\n\n"
        "## Tests\n- Focused syntax and lint checks.\n- Task-specific tests added or updated where required.\n"
    )
    run(["gh", "pr", "create", "--base", "master", "--head", branch, "--title", title, "--body", body])


def maybe_merge(pr: PullRequest, *, apply: bool) -> None:
    if os.getenv("AGENT_ALLOW_MERGE") != "1":
        print(f"CI is green for PR #{pr.number}; automatic merge is disabled.")
        return
    if not apply:
        print(f"[dry-run] Would squash-merge PR #{pr.number}.")
        return
    run(["gh", "pr", "merge", str(pr.number), "--squash", "--delete-branch"])


def run_cycle(*, apply: bool) -> None:
    ensure_repo_ready()
    pr = current_open_pr()
    if pr:
        state = classify_checks(pr.checks)
        print(f"PR #{pr.number} check state: {state}")
        if state == "failed":
            if apply:
                run(["git", "fetch", "origin", pr.branch])
                run(["git", "checkout", pr.branch])
                run(["git", "pull", "--ff-only", "origin", pr.branch])
            fix_failed_pr(pr, apply=apply)
            if apply:
                validate_changes()
                if run(["git", "status", "--porcelain"]).stdout.strip():
                    run(["git", "add", "--all"])
                    run([
                        "git",
                        "commit",
                        "-m",
                        "fix(ci): repair failing checks\n\nChanges:\n- Fix the reported CI root cause.\n\nSecurity:\n- Keep checks scoped and enabled.\n\nTests:\n- Re-run focused validation.",
                    ])
                    run(["git", "push"])
            return
        if state == "success":
            maybe_merge(pr, apply=apply)
            return
        print("CI is pending; no action this cycle.")
        return

    task = next_eligible_task()
    if task is None:
        print("No eligible todo task found.")
        return
    print(f"Next eligible task: {task.task_id} — {task.title}")
    branch = implement_task(task, apply=apply)
    commit_and_open_pr(task, branch, apply=apply)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Allow Codex and Git/GitHub writes.")
    parser.add_argument("--loop", action="store_true", help="Run continuously.")
    parser.add_argument(
        "--interval",
        type=int,
        default=DEFAULT_INTERVAL_SECONDS,
        help="Seconds between cycles in loop mode (default: 1200).",
    )
    args = parser.parse_args()
    if args.interval < 300:
        parser.error("--interval must be at least 300 seconds.")

    require_commands()
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("w", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RunnerError("Another codex_task_runner process is already running.") from None

        while True:
            try:
                run_cycle(apply=args.apply)
            except RunnerError as exc:
                print(f"ERROR: {exc}", file=sys.stderr)
            if not args.loop:
                break
            print(f"Sleeping for {args.interval} seconds...")
            time.sleep(args.interval)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130) from None
    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
