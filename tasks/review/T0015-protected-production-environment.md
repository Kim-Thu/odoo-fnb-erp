# T0015 — Document protected production environment

## Business goal

Define the minimum approval, secret-management, deployment, backup and rollback controls required before production use.

## Technical scope

- Add production-environment governance documentation.
- Define GitHub Environment protection requirements.
- Require immutable SHA-tagged container images.
- Define backup, deployment verification and rollback expectations.

## Security impact

Documentation-only task. It strengthens least privilege, secret handling, deployment approval and production-data protection. No credentials, production values, ACLs, record rules, `sudo()` or raw SQL are added.

## Files changed

- `docs/PROTECTED_PRODUCTION_ENVIRONMENT.md`
- `tasks/review/T0015-protected-production-environment.md`

## Tests

- Manual review that no real secret, endpoint or production data is present.
- Manual review that deployment uses immutable image references.
- Manual review that approval, backup and rollback controls are defined.

## Definition of done

- Production environment controls are documented.
- Security and rollback requirements are explicit.
- CI passes.
- PR is merged.
