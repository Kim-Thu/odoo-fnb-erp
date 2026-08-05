# Implementation slices

This file breaks the delivery plan into small, continuous slices. Each slice must be independently reviewable and must include code, tests, security checks and a clear definition of done.

## Slice 1 — Purchase rejection wizard

Goal: replace the temporary context-based rejection with a proper transient wizard.

Deliverables:

- Required rejection reason with trimming and minimum length validation.
- Only users in the Purchase Approver group can reject.
- Only draft/sent purchase orders can be rejected.
- Rejection updates audit fields through the model method, not direct arbitrary writes.
- Unit tests for empty reason, unauthorized user and successful rejection.

Definition of done:

- Reject button opens a modal wizard.
- Confirming the wizard writes the reason and closes the modal.
- The purchase order cannot be confirmed while rejected.
- Existing approval audit-field protections remain intact.

## Slice 2 — Inventory lot and expiry foundation

Goal: enforce traceability for F&B products using standard Odoo lot/serial and expiration features first.

Deliverables:

- Add `product_expiry` dependency.
- Require lot tracking for ingredients and finished goods when configured as traceable F&B items.
- Configure expiration defaults from product shelf life.
- Add validation preventing receipt completion when required lot/expiry data is missing.
- Tests for tracked and untracked products.

Definition of done:

- Standard Odoo expiration fields are used; no duplicate expiry model is created.
- Receipt validation fails safely when traceability data is incomplete.

## Slice 3 — FEFO and expired-stock protection

Goal: reduce expired-stock risk and prevent invalid outbound operations.

Deliverables:

- FEFO removal strategy configuration guidance and demo data.
- Validation blocking delivery/manufacturing consumption of expired lots.
- Manager-only override with mandatory reason and audit chatter entry.
- Tests for normal, expired and override paths.

## Slice 4 — Inventory reporting

Goal: provide operational visibility without premature dashboard complexity.

Deliverables:

- Near-expiry lot list.
- Expired inventory list.
- Stock by warehouse and product category.
- Read-only SQL/reporting review for indexes and query plans where needed.

## Slice 5 — MRP foundation

Goal: connect ingredients, BOMs and finished goods.

Deliverables:

- Manufacturing dependencies and standard-first configuration.
- BOM and production-order test data.
- Lot traceability from ingredient consumption to finished product.
- Tests for production completion and traceability.

## Delivery rules

- Never commit secrets, tokens, real personal data or production configuration.
- Avoid `sudo()` unless a documented security review proves it is necessary.
- Prefer ORM and standard Odoo models over raw SQL and duplicate custom models.
- Every externally reachable action must enforce authorization, company scope and input validation.
- Each slice updates tests and documentation before starting the next slice.
