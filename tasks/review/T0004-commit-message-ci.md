# T0004 — Validate structured commit messages in CI

## Metadata
- Type: `ci`
- Epic: Repository and delivery foundation
- Status: `review`
- Depends on: `T0002`
- Branch: `ci/T0004-commit-message-check-20260806-0902`

## Goal
Require each non-merge commit to explain behavior, tests and security impact.

## In scope
- Require a conventional subject with task ID.
- Require `Added/Changed/Fixed` as applicable.
- Require `Tests` section.
- Require `Security` section.
- Exempt automated `chore(release):` version commits.

## Required tests
- [x] Valid feature or CI commit passes.
- [x] Missing Tests section fails.
- [x] Missing Security section fails.
- [x] Empty section fails.
- [x] Commit text is processed safely as plain data.

## Security checklist
- [x] No shell evaluation of commit content.
- [x] Read-only GitHub permissions.
- [x] Error output does not print commit bodies or secrets.

## Definition of done
- [x] CI rejects incomplete commit messages.
- [x] Workflow includes valid and invalid examples.
- [ ] CI passes on its own branch.

## Evidence
- Workflow: `.github/workflows/commit-message.yml`
- Pull request: pending
- CI: pending
