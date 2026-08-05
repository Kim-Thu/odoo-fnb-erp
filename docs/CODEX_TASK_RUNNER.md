# Codex Task Runner

The local task runner advances one backlog task at a time by combining:

- `codex exec` for non-interactive code changes;
- `gh` for pull-request and workflow status;
- `git` for branch, commit and push operations.

It does **not** automate the ChatGPT web interface.

## Requirements

- macOS or Linux.
- Python 3.12+.
- Git.
- GitHub CLI authenticated with `gh auth login`.
- Codex CLI installed and authenticated with `codex login`.

Do not store GitHub or OpenAI tokens in this repository.

## Dry run

Run one inspection cycle without repository writes:

```bash
python scripts/codex_task_runner.py
```

The runner reports the current PR state or the next eligible backlog task.

## Apply one cycle

Allow Codex, Git and GitHub writes for one cycle:

```bash
python scripts/codex_task_runner.py --apply
```

## Continuous mode

Check every 20 minutes:

```bash
python scripts/codex_task_runner.py --apply --loop --interval 1200
```

The minimum accepted interval is 300 seconds. Twenty minutes is recommended to avoid overlapping with CI and wasting Codex usage.

## Automatic merge

Automatic merge is disabled by default. To allow squash merge after every required check is green:

```bash
AGENT_ALLOW_MERGE=1 python scripts/codex_task_runner.py --apply --loop --interval 1200
```

Keep branch protection and required status checks enabled. The runner must not bypass them.

## Execution flow

Each cycle performs one of these actions:

1. If an open task PR has pending checks, wait.
2. If checks failed, fetch the latest failed logs and ask Codex to repair only the root cause.
3. If checks passed, stop or merge when `AGENT_ALLOW_MERGE=1`.
4. If no task PR exists, read `MASTER_TASK_PLAN.md`, select the first eligible `todo` task, create a correctly named branch, invoke Codex, validate changes, commit, push and open a PR.

A filesystem lock prevents two runner processes from operating on the repository simultaneously.

## Safety boundaries

- The repository must be clean before every cycle.
- Codex may edit only the current repository.
- The wrapper, not Codex, performs Git and GitHub mutations.
- Full Odoo tests are not run automatically unless the selected task requires them.
- Logs are stored locally under `.agent-logs/` and ignored by Git.
- Automatic merge requires an explicit environment variable.
- The runner stops safely on missing commands, malformed GitHub output, dirty worktree or unexpected command failures.

## Stop the runner

Press `Ctrl+C`.

For long-running use, run it inside `tmux`, `screen`, a Dev Container terminal, or a user-level service managed by the operating system.
