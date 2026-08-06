# T0002 — Standardize task specifications

## Metadata
- Type: `maint`
- Epic: Repository and delivery foundation
- Status: `review`
- Depends on: `T0001`
- Dependencies ready: `yes — T0001 is marked done in MASTER_TASK_PLAN.md`
- Branch: `maint/T0002-finalize-task-template-20260806-0841`

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
- Commit: `0127ee969b18d97459fc3649f167b1adf8109bdc`
- Pull request: pending
- CI run: pending
- Test commands: manual regex and document consistency review
- Dependency evidence: T0001 is marked done in MASTER_TASK_PLAN.md
- Review notes: branch recreated from current master to avoid stale-history changes
- Notes: runtime code was not changed.
