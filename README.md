# Odoo F&B ERP

Portfolio-oriented Odoo ERP project for an F&B manufacturing and retail business.

## Scope

The project follows the `Standard First` principle and implements a vertical business flow:

`Purchase -> Inventory -> Manufacturing -> Quality -> Sales`

Planned capabilities include:

- Master data for ingredients and finished products
- Purchase approval
- Multi-warehouse inventory, lot and expiry tracking
- MRP and traceability
- Quality controls
- Sales and returns
- Authenticated REST APIs
- Audit logging, automated tests and CI

## Security baseline

- No secrets or production credentials are committed.
- Runtime secrets must be supplied through environment variables.
- `.env` and local Odoo configuration files are ignored.
- Public API routes must authenticate requests and enforce company scope.
- Odoo ACLs and record rules remain the primary authorization layer.
- Demo data must never contain real customer, employee or company data.

## Local setup

1. Copy `.env.example` to `.env`.
2. Replace every placeholder secret.
3. Start the stack:

```bash
make up
```

4. Open `http://localhost:${ODOO_PORT:-8069}`.

## Useful commands

```bash
make up
make down
make logs
make shell
make lint
make test
```

## Documentation

- `docs/BRD.md`
- `docs/SRS.md`
- `docs/PLAN.md`
- `docs/SECURITY.md`

## Current milestone

Week 1 foundation: secure Docker environment, custom addon skeleton, lint/test workflow and documentation baseline.
