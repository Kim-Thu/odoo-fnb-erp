# Development Workflow Rules

## 1. Task slicing

Each implementation task must be small enough to complete, review, test, and merge independently.

A task must contain:

- Task number and short name.
- Business goal.
- Technical scope.
- Security impact.
- Files expected to change.
- Test cases.
- Definition of done.

Do not combine unrelated features, fixes, refactors, and maintenance work in the same task.

## 2. Branch naming

Canonical format:

```text
<type>/T<4-digit-task-id>-<short-name>-<yyyyMMdd-HHmm>
```

Allowed prefixes:

- `feat/` — new business or technical capability.
- `fix/` — bug or regression fix.
- `refactor/` — internal code restructuring without changing expected behavior.
- `test/` — test-only changes.
- `docs/` — documentation-only changes.
- `ci/` — CI/CD changes.
- `maint/` — dependency, tooling, housekeeping, or operational maintenance.
- `security/` — security hardening or vulnerability remediation.
- `performance/` — performance-only changes with measured evidence.

Examples:

```text
feat/T3004-default-expiry-20260806-1430
fix/T2011-purchase-approval-reset-20260806-1515
ci/T0003-branch-name-validation-20260806-1600
security/T7003-api-company-scope-20260806-1645
```

Validation regex:

```regex
^(feat|fix|refactor|test|docs|ci|maint|security|performance)/T[0-9]{4}-[a-z0-9]+(?:-[a-z0-9]+)*-[0-9]{8}-[0-9]{4}$
```

Rules:

- Task IDs always use uppercase `T` followed by exactly four digits.
- Short names use lowercase kebab-case only.
- Timestamp uses local project time in `yyyyMMdd-HHmm` format.
- One task per branch.
- Branch from the latest accepted base branch.
- Never continue a different task on an existing feature branch.
- Never commit secrets, credentials, database dumps, production data, or private keys.

## 3. Commit format

Subject format:

```text
<type>(<scope>): <clear change summary>
```

Commit body must include all sections below:

```text
Changes:
- Added ...
- Updated ...
- Removed ...

Reason:
- Business or technical reason.

Security:
- Authorization, validation, company scope, secret handling, SQL, RPC, or data exposure impact.
- State `No security impact` only after checking.

Tests:
- Test name or scenario.
- Expected result.
- Actual command used.

Rules checked:
- No sudo() unless documented and justified.
- No raw SQL unless documented, parameterized, and reviewed.
- No bypass of ACLs or record rules.
- No secrets or real personal/business data.
- Multi-company scope checked where relevant.
- Error messages do not expose sensitive internals.
```

## 4. Pull request requirements

Every pull request must include:

- Task number and linked task description.
- Business outcome.
- Technical changes.
- Security review.
- Migration or deployment impact.
- Test evidence.
- Known limitations.
- Rollback approach.

A pull request must not be marked ready until:

- CI passes.
- Odoo module installs or upgrades successfully.
- Automated tests pass.
- Security rules are checked.
- Documentation is updated when behavior changes.
- No unrelated changes remain in the diff.

## 5. Testing rules

Minimum test coverage per task:

- Positive path.
- Validation failure path.
- Unauthorized-user path when permissions are involved.
- Multi-company path when company-owned data is involved.
- Regression test for every bug fix.

For Odoo business logic, prefer `SavepointCase` or `TransactionCase` based on isolation needs.

Required checks:

```text
ruff
python -m compileall addons
manifest validation
secret scan
Odoo module installation/upgrade
Odoo automated tests
```

## 6. Security rules

Mandatory rules:

- Use standard Odoo ORM and security model first.
- Do not use `sudo()` to make failing permissions disappear.
- Any necessary `sudo()` must be isolated, documented, minimized, and covered by tests.
- Raw SQL must be exceptional, parameterized, documented, benchmarked, and reviewed.
- Enforce ACLs, record rules, allowed companies, and field allowlists.
- Validate all external input.
- Never trust IDs, company IDs, domains, or field names supplied by API clients.
- Do not log tokens, passwords, personal data, full request bodies, or confidential business data.
- Use environment variables or secret stores for credentials.
- Demo and test data must be synthetic.
- Public controllers must define authentication, CSRF behavior, rate-limiting expectations, and company scope explicitly.

## 7. Task completion rule

A task is complete only when all items are true:

- Code is committed on its own correctly named branch.
- Commit message follows this document.
- Tests exist and pass.
- CI passes.
- Security checklist passes.
- Pull request is updated with evidence.
- Next task is created from the implementation plan, not improvised from unfinished code.

## 8. Scheduled continuation limitation

Automation may inspect the repository and continue the next ready task on a schedule, but it must still obey:

- Maximum supported frequency: once per hour.
- No automatic event trigger when a previous task finishes.
- Each run must first inspect open PRs, CI status, branch state, and the implementation plan.
- If the current task is incomplete or CI is failing, fix that task before starting another branch.
- Never create parallel branches that modify the same files without an explicit dependency plan.
