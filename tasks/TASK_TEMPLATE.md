# <TASK-ID> — <Task title>

## Metadata

- Type: `<feat|fix|refactor|test|docs|ci|maint|security|performance>`
- Epic: `<epic name>`
- Status: `todo`
- Depends on: `<task IDs or none>`
- Source requirements: `<BRD/SRS/PLAN references>`
- Branch: `<type>/T<4-digit-task-id>-<short-name>-<yyyyMMdd-HHmm>`

## Goal

One measurable outcome only.

## In scope

- Item 1.
- Item 2.

## Out of scope

- Item 1.

## Implementation notes

- Prefer standard Odoo behavior before customization.
- Use ORM unless a documented limitation requires parameterized SQL.
- Do not use `sudo()` without explicit written justification.

## Required tests

- [ ] Positive path.
- [ ] Validation/error path.
- [ ] Permission path, when applicable.
- [ ] Multi-company path, when applicable.
- [ ] Regression test for affected behavior.

## Security checklist

- [ ] No secret, token, password or real personal data.
- [ ] ACL reviewed.
- [ ] Record rules reviewed.
- [ ] Company scope enforced.
- [ ] Input validated.
- [ ] No unsafe `sudo()`.
- [ ] No unsafe raw SQL.
- [ ] Logs and errors do not expose sensitive data.

## Definition of done

- [ ] Code is limited to this task.
- [ ] Required tests pass locally or in CI.
- [ ] CI passes.
- [ ] Documentation is updated.
- [ ] Commit message contains Changes/Reason/Security/Tests/Rules checked sections.
- [ ] Task evidence is recorded below.

## Evidence

- Commit:
- Pull request:
- CI run:
- Test commands:
- Notes:
