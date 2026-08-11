# Project Blueprint

## Purpose

This document is the implementation map between the BRD, SRS, Odoo standard capabilities, custom modules, data flows, security boundaries, test coverage, and release phases.

## System context

The project delivers an Odoo-based ERP for an F&B business. Odoo standard behavior is preferred first; customization is introduced only when the BRD/SRS cannot be met safely or clearly with configuration.

## Phase model

| Phase | Scope | Exit gate |
|---|---|---|
| P0 | Repository, CI/CD, security foundation | Reliable branch/commit validation, lint, tests, container build |
| P1 | Master data and shared configuration | Product/UoM/partner/warehouse foundations usable |
| P2 | Purchase and Procure-to-Stock | RFQ/PO approval, receipt traceability, vendor linkage |
| P3 | Inventory lot, expiry and FEFO | Lot/expiry enforcement and expired-stock governance |
| P4 | Inventory operations | Count approval, reordering, barcode, internal transfer |
| P5 | Manufacturing | BOM, MO, work orders, lot traceability, costing |
| P6 | Quality | QCP, alerts, blocking rules, corrective action |
| P7 | Sales and returns | Quotation/SO, delivery, return quarantine, invoicing handoff |
| P8 | POS and accounting basic | POS session/order/return and invoice/payment baseline |
| P9 | Approval and audit | Sensitive action approval + auditable changes |
| P10 | API and integration | Authenticated company-safe APIs, idempotency, webhook/retry |
| P11 | Dashboard and analytics | Operational KPIs with tested company isolation |
| P12 | Demo data and end-to-end UAT | Representative data and P2S/P2P-MRP/O2C/POS flows pass |
| P13 | Hardening and release | Security review, staging, backup/restore, RC and release docs |

## Core data model map

| Domain | Odoo standard model / table | Custom extension intent |
|---|---|---|
| Product | `product.template`, `product.product` | F&B SKU, shelf life, storage condition, traceability flags |
| UoM | `uom.uom`, `uom.category` | Prefer standard configuration; test valid/invalid conversion |
| Partner | `res.partner` | Prefer standard customer/vendor/payment/tax data |
| Company | `res.company` | Approval thresholds and company-owned configuration |
| Warehouse | `stock.warehouse`, `stock.location` | Demo structure for Raw Materials, Production, Finished Goods |
| Inventory | `stock.quant`, `stock.move`, `stock.picking` | Receipt validation, count approval, stock policies |
| Lots | `stock.lot` | Default expiry and traceability rules |
| Purchase | `purchase.order`, `purchase.order.line` | Approval state, audit metadata, rejection flow |
| Manufacturing | `mrp.bom`, `mrp.production`, work-order models | Traceability and demo costing extensions as needed |
| Quality | Quality-related Odoo models available in selected edition | QCP, alert, blocking behavior where standard is insufficient |
| Sales | `sale.order`, `sale.order.line` | Return governance and integration endpoints |
| POS | POS session/order models | Standard-first demo workflow |
| Accounting | `account.move`, payment models | Basic invoice/payment demo integration only |
| Integration | Custom API/integration log models | Idempotency, retry state, dead-letter simulation, audit metadata |
| Dashboard | ORM/report models | KPI aggregation and company-safe query definitions |

## Primary data flows

### Procure-to-Stock

Demand/reordering → RFQ → approval → PO → receipt → quality check → lot/expiry validation → stock → vendor bill linkage.

### Plan-to-Produce

Demand/reordering → MO → reserve ingredients → consume ingredient lots → work orders → quality → finished lot → stock → costing comparison.

### Order-to-Cash

Quotation → SO → availability/reservation → delivery → invoice → payment.

### POS-to-Inventory

POS session → POS order/payment → store stock deduction → return/refund if required → close session/reconcile.

### Inventory adjustment

Inventory count → actual quantity → variance calculation → threshold evaluation → approval if required → adjustment → audit log.

### Traceability

Vendor/PO → receipt → ingredient lot → MO consumption → finished-product lot → delivery/POS sale → return/quarantine.

### API and event flow

External client → authentication → schema validation → company scope → service/ORM → response/audit. Business event → integration queue/log → retry policy → delivery or dead-letter state.

## Security boundaries

- Every company-owned record must be evaluated against allowed companies.
- Warehouse-specific restrictions are added where BRD/SRS requires them.
- No `sudo()` is used to bypass access failures.
- APIs use explicit authentication, input allowlists and pagination bounds.
- Idempotency keys are scoped to an authenticated integration/company context.
- Sensitive payloads, credentials and personal data are not written to logs.

## Documentation set

- `docs/BRD_Odoo_FnB_ERP.md` — business requirements.
- `docs/SRS_Odoo_FnB_ERP.md` — software requirements.
- `docs/PROJECT_BLUEPRINT.md` — phases, system context, data model and flows.
- `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` — requirement-to-task mapping.
- `docs/DEVELOPMENT_RULES.md` — execution and delivery rules.
- Future implementation tasks add detailed architecture, ERD, API contract and UAT evidence when their phase is reached.
