# T3004 — Derive default expiration from shelf life

## Metadata
- Type: `feat`
- Epic: Inventory lot and expiry
- Status: `review`
- Depends on: `T3003`
- Branch: `feat/T3004-default-expiry-20260806-1858`

## Goal
Populate the standard lot expiration date from product shelf life without creating duplicate expiry fields.

## In scope
- Use standard Odoo lot expiration fields.
- Calculate expiration from the lot creation time and `fnb_shelf_life_days`.
- Preserve a user-entered expiration date.
- Skip products that do not require traceability.

## Out of scope
- FEFO removal strategy.
- Expired-stock override.
- Custom expiry model.

## Required tests
- [x] Traceable product with shelf life gets a default expiration date.
- [x] Existing expiration date is not overwritten.
- [x] Zero shelf life does not create an invalid date.
- [x] Untracked product is unchanged.
- [x] Behavior remains company-scoped.

## Security checklist
- [x] No `sudo()`.
- [x] ORM only.
- [x] No cross-company lot lookup.
- [x] No sensitive data in logs.

## Definition of done
- [x] Standard Odoo expiry field is used.
- [x] Required automated tests are implemented.
- [ ] CI passes.
- [x] Documentation explains the date source.

## Evidence
- `addons/fnb_core/models/stock_lot.py` derives `expiration_date` at lot creation.
- `addons/fnb_core/tests/test_stock_lot_expiration.py` covers all required scenarios.
- CI execution is pending on the pull request.
