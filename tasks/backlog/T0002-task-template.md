# T0002 — Standardize task specifications

## Metadata
- Type: `maint`
- Epic: Repository and delivery foundation
- Status: `review`
- Depends on: `T0001`
- Branch: `maint/T0002-standardize-branch-format-20260806-0528`

## Goal
Standardize the reusable task template and canonical branch naming format before automated task execution.

## In scope
- Verify `tasks/TASK_TEMPLATE.md` contains metadata, scope, dependencies, tests, security and evidence.
- Standardize branch format to `<type>/T<4-digit-task-id>-<short-name>-<yyyyMMdd-HHmm>`.
- Cross-check task instructions with `docs/DEVELOPMENT_RULES.md` and `tasks/README.md`.

## Required tests
- [x] Manual structure review.
- [x] Confirm every mandatory development rule has a matching checklist item.
- [x] Validate canonical examples against the documented regex.

## Security checklist
- [x] No secrets or real data.
- [x] Security checks are mandatory, not optional.
- [x] No ACL, record-rule, `sudo()` or raw SQL changes.

## Definition of done
- [x] Template is complete.
- [x] Branch format is consistent across workflow documents.
- [ ] CI documentation checks pass.
- [x] Task moves to review.

## Evidence
- Commit: `3477aceb01febc1a77b9ba789f3944e272590d50`
- Pull request: pending
- CI run: pending
- Test commands: manual regex and document consistency review
- Notes: runtime code was not changed.
