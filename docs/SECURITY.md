# Security Baseline

## Secrets

- Never commit `.env`, `odoo.conf`, API tokens, private keys, production URLs or database dumps.
- Use long random values for `POSTGRES_PASSWORD` and `ODOO_ADMIN_PASSWD`.
- Rotate any credential immediately if it appears in Git history, logs or screenshots.

## Network exposure

- PostgreSQL is not published to the host.
- Odoo binds to `127.0.0.1` for local development.
- Production traffic must terminate TLS at a reverse proxy.
- Do not expose the Odoo database manager publicly.

## Odoo authorization

- Prefer built-in groups, ACLs and record rules.
- Never use `sudo()` to bypass authorization unless the business requirement is documented and the affected records are explicitly scoped.
- Every future API route must authenticate, validate company scope and reject fields not declared in an allowlist.
- Multi-company queries must include company restrictions.

## Data handling

- Use synthetic demo data only.
- Do not commit customer, employee, vendor, financial or production data.
- Database backups must be encrypted and stored outside the repository.

## Python and SQL

- Use Odoo ORM by default.
- Parameterize SQL queries; never concatenate user-controlled input.
- Validate selection values, identifiers, pagination and payload size.
- Avoid logging credentials, session IDs, access tokens or personal data.

## Deployment

- Separate Development, Staging and Production credentials and databases.
- Run containers without additional privileges.
- Apply security updates to Odoo, PostgreSQL and the base operating system.
- Test restore procedures; a backup is not valid until restored successfully.

## Reporting vulnerabilities

Do not open a public issue containing exploit details or secrets. Report privately to the repository owner and include reproduction steps without production data.
