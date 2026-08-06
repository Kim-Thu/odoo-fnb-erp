# Protected Production Environment

## Purpose

This document defines the minimum controls required before any production deployment of the Odoo F&B ERP system.

## Environment separation

- Production must use a dedicated GitHub Environment named `production`.
- Production credentials, database URLs and registry credentials must never be stored in repository files.
- Development, staging and production must use separate databases, secrets and deployment targets.
- Production data must never be copied into tests, demos or pull-request environments.

## Deployment approval

The `production` GitHub Environment must require manual approval before deployment.

Recommended controls:

- At least one required reviewer who is not the author of the deployment change.
- Prevent self-review where the GitHub plan supports it.
- Restrict deployment branches to `master` and approved `release/**` branches.
- Keep deployment jobs blocked until all required CI checks have passed.

## Secrets and permissions

- Use GitHub Environment secrets or an external secret manager.
- Use the least-privileged token required for the deployment.
- Never grant write access to repository contents unless the deployment process truly requires it.
- Do not print tokens, passwords, database URLs or complete environment payloads in logs.
- Prefer short-lived credentials and workload identity over long-lived static keys.

## Container image policy

- Deploy only images published from approved branches.
- Use the immutable Git SHA tag as the deployment reference.
- Do not deploy mutable tags such as `latest`.
- Record the image digest used for every production deployment.
- Verify that the image passed CI, vulnerability scanning and the required approval gate.

## Database safety

Before deployment:

- Create and verify a recent backup.
- Confirm the restore procedure has been tested in a non-production environment.
- Review module upgrade and migration impact.
- Stop deployment if a migration cannot be rolled back safely.

During deployment:

- Run Odoo module upgrades only through the approved deployment job.
- Do not run ad-hoc SQL against production.
- Do not use `sudo()` or bypass Odoo access controls as a deployment workaround.

After deployment:

- Run a smoke test for login, module loading and critical business flows.
- Check Odoo and database logs for errors without exposing sensitive data.
- Record the deployed commit SHA, image digest, approver and deployment time.

## Rollback

A production deployment must have a documented rollback path:

1. Stop new traffic or disable the affected service when necessary.
2. Redeploy the previously approved immutable image digest.
3. Restore the database backup only when schema or data changes require it.
4. Verify login and critical business flows after rollback.
5. Record the incident, root cause and follow-up actions.

## Required GitHub configuration

Repository administrators should configure:

- GitHub Environment: `production`.
- Required reviewers for that environment.
- Deployment branch restrictions for `master` and approved `release/**` branches.
- Environment secrets only; no production secrets at repository level unless unavoidable.
- Branch protection and required CI checks before merge.

## Security checklist

- No secrets committed to Git.
- No production data in logs, tests or artifacts.
- Immutable image reference used.
- Manual approval completed.
- Backup and rollback plan verified.
- CI and security scans passed.
- Deployment and smoke-test evidence recorded.
