# T0004 — Validate structured commit messages in CI

## Metadata
- Type: `ci`
- Epic: Repository and delivery foundation
- Status: `todo`
- Depends on: `T0002`
- Branch: `ci/T0004-commit-message-check-<YYYYMMDD-HHmm>`

## Goal
Require each non-merge commit to explain behavior, tests and security impact.

## In scope
- Require a conventional subject with task ID.
- Require `Added/Changed/Fixed` as applicable.
- Require `Tests` section.
- Require `Security` section.
- Define explicit handling for merge commits and automated version commits.

## Required tests
- [ ] Valid feature commit passes.
- [ ] Missing Tests section fails.
- [ ] Missing Security section fails.
- [ ] Empty section fails.
- [ ] Commit text is processed safely as plain data.

## Security checklist
- [ ] No shell evaluation of commit content.
- [ ] Read-only GitHub permissions.
- [ ] Error output does not print secrets.

## Definition of done
- [ ] CI rejects incomplete commit messages.
- [ ] Documentation includes a valid example.
- [ ] CI passes on its own branch.
