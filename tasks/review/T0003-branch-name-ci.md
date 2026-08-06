# T0003 — Validate branch naming in CI

## Metadata
- Type: `ci`
- Epic: Repository and delivery foundation
- Status: `review`
- Depends on: `T0002`
- Branch: `ci/T0003-branch-name-check-20260806-0856`

## Goal
Fail pull-request CI when the source branch does not follow the approved format.

## In scope
- Validate allowed prefixes.
- Validate task ID.
- Validate short kebab-case name.
- Validate `YYYYMMDD-HHmm` timestamp.

## Required tests
- [x] Valid `feat/T3004-default-expiry-20260806-0600` passes.
- [x] Unknown prefix fails.
- [x] Missing task ID fails.
- [x] Missing timestamp fails.
- [x] Branch metadata is treated as data, never executed as shell code.

## Security checklist
- [x] No `eval`.
- [x] Quote all shell variables.
- [x] Read-only GitHub permissions.

## Definition of done
- [x] CI check has clear failure output.
- [x] Tests cover valid and invalid names.
- [ ] CI passes on its own branch.

## Evidence
- Branch: `ci/T0003-branch-name-check-20260806-0856`
- Workflow: `.github/workflows/branch-name.yml`
- Commit: `bfa3364b18976f8d88baded903955a4f95d15c8c`
- Pull request: pending
- CI run: pending
