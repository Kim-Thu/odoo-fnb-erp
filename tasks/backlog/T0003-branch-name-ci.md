# T0003 — Validate branch naming in CI

## Metadata
- Type: `ci`
- Epic: Repository and delivery foundation
- Status: `todo`
- Depends on: `T0002`
- Branch: `ci/T0003-branch-name-check-<YYYYMMDD-HHmm>`

## Goal
Fail pull-request CI when the source branch does not follow the approved format.

## In scope
- Validate allowed prefixes.
- Validate task ID.
- Validate short kebab-case name.
- Validate `YYYYMMDD-HHmm` timestamp.

## Required tests
- [ ] Valid `feat/T3004-default-expiry-20260806-0600` passes.
- [ ] Unknown prefix fails.
- [ ] Missing task ID fails.
- [ ] Missing timestamp fails.
- [ ] Branch metadata is treated as data, never executed as shell code.

## Security checklist
- [ ] No `eval`.
- [ ] Quote all shell variables.
- [ ] Read-only GitHub permissions.

## Definition of done
- [ ] CI check has clear failure output.
- [ ] Tests cover valid and invalid names.
- [ ] CI passes on its own branch.
