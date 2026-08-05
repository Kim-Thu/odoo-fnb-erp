# T3004 — Derive default expiration from shelf life

## Metadata
- Type: `feat`
- Epic: Inventory lot and expiry
- Status: `todo`
- Depends on: `T3003`
- Branch: `feat/T3004-default-expiry-<YYYYMMDD-HHmm>`

## Goal
Populate the standard lot expiration date from product shelf life without creating duplicate expiry fields.

## In scope
- Use standard Odoo lot expiration fields.
- Calculate expiration from the relevant receipt/creation date and `fnb_shelf_life_days`.
- Preserve a user-entered expiration date.
- Skip products that do not require traceability.

## Out of scope
- FEFO removal strategy.
- Expired-stock override.
- Custom expiry model.

## Required tests
- [ ] Traceable product with shelf life gets a default expiration date.
- [ ] Existing expiration date is not overwritten.
- [ ] Zero shelf life does not create an invalid date.
- [ ] Untracked product is unchanged.
- [ ] Behavior remains company-scoped.

## Security checklist
- [ ] No `sudo()`.
- [ ] ORM only.
- [ ] No cross-company lot lookup.
- [ ] No sensitive data in logs.

## Definition of done
- [ ] Standard Odoo expiry field is used.
- [ ] All required tests pass.
- [ ] CI passes.
- [ ] Documentation explains the date source.
