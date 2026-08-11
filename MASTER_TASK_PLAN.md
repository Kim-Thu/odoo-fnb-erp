# Master Task Plan

This backlog is the single source of truth for delivery. It is organized by delivery phase and mapped to the BRD/SRS in `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.

## Status values

- `todo`
- `in_progress`
- `review`
- `blocked`
- `done`

## Global completion gates

Every task must satisfy the applicable items below:

- Positive-path test or validation evidence.
- Validation/error-path test where behavior can fail.
- Permission test when access is affected.
- Multi-company test when company-owned records are affected.
- No secret, token, real personal data or production configuration.
- No `sudo()` without written security justification.
- No raw SQL without written ORM limitation, parameter binding and query-plan review.
- Documentation updated when behavior or architecture changes.
- CI must pass before `done`.

## Phase 0 — Repository, CI/CD and security foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T0001 | maint | Add task-state directory workflow | — | done |
| T0002 | docs | Add reusable task template | T0001 | done |
| T0003 | ci | Validate branch-name format in CI | T0002 | done |
| T0004 | ci | Validate commit-message sections in CI | T0002 | review |
| T0005 | ci | Add Ruff configuration and lint command | — | todo |
| T0006 | ci | Add XML validation for Odoo views | T0005 | todo |
| T0007 | security | Add Gitleaks configuration | — | todo |
| T0008 | security | Add dependency/container vulnerability scan | T0007 | todo |
| T0009 | ci | Run Odoo module install in CI | — | todo |
| T0010 | ci | Run tagged Odoo tests in CI | T0009 | todo |
| T0011 | ci | Upload Odoo logs on failure | T0010 | todo |
| T0012 | ci | Add CI concurrency cancellation | T0010 | todo |
| T0013 | ci | Build container image on approved branches | T0009 | todo |
| T0014 | ci | Push immutable SHA image to GHCR | T0013 | todo |
| T0015 | docs | Document protected production environment | T0014 | todo |
| T0016 | docs | Establish BRD/SRS project blueprint and phased roadmap | T0002 | review |

## Phase 1 — Master data and shared configuration

### Product master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1001 | feat | Add F&B classification field | T0010 | done |
| T1002 | feat | Add storage-condition field | T1001 | done |
| T1003 | feat | Add shelf-life-days field | T1001 | done |
| T1004 | feat | Add traceability-required flag | T1003 | done |
| T1005 | fix | Validate shelf life is non-negative | T1003 | done |
| T1006 | feat | Enforce F&B SKU uniqueness by company | T1001 | done |
| T1007 | test | Test SKU uniqueness in same company | T1006 | done |
| T1008 | test | Test same SKU across different companies | T1006 | done |
| T1009 | test | Test negative shelf-life rejection | T1005 | todo |
| T1010 | docs | Add product import template and field guide | T1004 | todo |

### UoM and partner master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1101 | docs | Define standard-first UoM configuration | T0016 | todo |
| T1102 | test | Test valid UoM conversion within category | T1101 | todo |
| T1103 | test | Test invalid cross-category UoM conversion | T1101 | todo |
| T1104 | docs | Define customer/vendor master-data configuration | T0016 | todo |
| T1105 | test | Test vendor/customer master demo setup | T1104 | todo |
| T1106 | docs | Add partner import template and field guide | T1104 | todo |

### Warehouse foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1201 | docs | Define Raw Materials Production Finished Goods warehouse structure | T0016 | todo |
| T1202 | feat | Add warehouse/location demo configuration | T1201 | todo |
| T1203 | test | Test internal transfer across configured locations | T1202 | todo |

## Phase 2 — Purchase and Procure-to-Stock

### Purchase approval

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T2001 | feat | Add company approval threshold | T0010 | done |
| T2002 | feat | Add purchase approver group | T2001 | done |
| T2003 | feat | Compute approval-required state | T2001 | done |
| T2004 | feat | Add approve action | T2002,T2003 | done |
| T2005 | security | Protect approval audit fields from direct writes | T2004 | done |
| T2006 | feat | Reset approval when commercial fields change | T2004 | done |
| T2007 | feat | Block confirmation before approval | T2004 | done |
| T2008 | feat | Add rejection wizard | T2002 | done |
| T2009 | test | Test unauthorized approval | T2004 | todo |
| T2010 | test | Test approval and confirmation path | T2007 | todo |
| T2011 | test | Test approval reset after vendor change | T2006 | todo |
| T2012 | test | Test approval reset after order-line change | T2006 | todo |
| T2013 | test | Test rejection reason validation | T2008 | todo |
| T2014 | test | Test rejected order cannot confirm | T2007,T2008 | todo |
| T2015 | test | Test approval records remain company-scoped | T2004 | todo |
| T2016 | docs | Document purchase approval workflow | T2015 | todo |

### Standard purchase flow and traceability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T2101 | docs | Define standard-first RFQ and PO configuration | T1105 | todo |
| T2102 | test | Test manual RFQ to PO flow | T2101 | todo |
| T2103 | test | Test partial purchase receipt | T2101 | todo |
| T2104 | test | Test PO to receipt traceability | T2103 | todo |
| T2105 | test | Test receipt to PO and lot traceability | T2104,T3004 | todo |
| T2106 | docs | Document vendor bill linkage in Procure-to-Stock | T2104 | todo |

## Phase 3 — Inventory lot, expiry, FEFO and reporting

### Lot and expiry

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3001 | feat | Add product_expiry dependency | T0010 | done |
| T3002 | feat | Synchronize traceability flag to lot tracking | T1004,T3001 | done |
| T3003 | feat | Enable expiration handling for traceable products | T3002 | done |
| T3004 | feat | Derive default expiration from shelf life | T3003 | done |
| T3005 | feat | Detect inbound moves requiring lot data | T3002 | done |
| T3006 | feat | Block receipt validation when lot is missing | T3005 | done |
| T3007 | feat | Block receipt validation when expiration is missing | T3005 | done |
| T3008 | test | Test untracked product receipt succeeds | T3006 | todo |
| T3009 | test | Test traceable receipt without lot fails | T3006 | todo |
| T3010 | test | Test traceable receipt without expiry fails | T3007 | todo |
| T3011 | test | Test complete traceable receipt succeeds | T3007 | todo |
| T3012 | test | Test receipt checks are company-scoped | T3011 | todo |
| T3013 | docs | Document inbound lot and expiry workflow | T3012 | todo |

### FEFO and expired-stock protection

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3101 | feat | Add FEFO removal strategy demo configuration | T3013 | todo |
| T3102 | feat | Detect expired lots on outbound moves | T3101 | todo |
| T3103 | feat | Block delivery of expired lots | T3102 | todo |
| T3104 | feat | Block manufacturing consumption of expired lots | T3102 | todo |
| T3105 | feat | Add expired-stock override group | T3103 | todo |
| T3106 | feat | Add mandatory override-reason wizard | T3105 | todo |
| T3107 | security | Log override user time reason and affected lots | T3106 | todo |
| T3108 | test | Test normal FEFO selection | T3101 | todo |
| T3109 | test | Test expired delivery is blocked | T3103 | todo |
| T3110 | test | Test expired consumption is blocked | T3104 | todo |
| T3111 | test | Test unauthorized override fails | T3106 | todo |
| T3112 | test | Test authorized override is audited | T3107 | todo |
| T3113 | docs | Document FEFO and override governance | T3112 | todo |

### Inventory reporting

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3201 | feat | Add near-expiry lot search filter | T3013 | todo |
| T3202 | feat | Add expired-lot search filter | T3201 | todo |
| T3203 | feat | Add configurable near-expiry day threshold | T3201 | todo |
| T3204 | feat | Add near-expiry list action | T3203 | todo |
| T3205 | feat | Add stock-by-warehouse pivot | T3204 | todo |
| T3206 | performance | Review indexes for expiry list domains | T3204 | todo |
| T3207 | test | Test near-expiry boundary dates | T3203 | todo |
| T3208 | test | Test report company isolation | T3205 | todo |
| T3209 | docs | Document inventory reports | T3208 | todo |

## Phase 4 — Inventory operations

### Inventory count and variance approval

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3301 | docs | Define inventory-count approval policy and threshold | T1203 | todo |
| T3302 | feat | Add inventory variance approval configuration | T3301 | todo |
| T3303 | feat | Block large inventory adjustment before approval | T3302 | todo |
| T3304 | security | Audit inventory adjustment approval metadata | T3303 | todo |
| T3305 | test | Test small variance adjustment path | T3302 | todo |
| T3306 | test | Test large variance requires approval | T3303 | todo |
| T3307 | test | Test inventory adjustment company isolation | T3304 | todo |

### Reordering

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3401 | docs | Define standard-first reordering rules | T1202 | todo |
| T3402 | feat | Add F&B reordering demo configuration | T3401 | todo |
| T3403 | feat | Log source of generated procurement proposal | T3402 | todo |
| T3404 | test | Test below-minimum purchase proposal | T3402 | todo |
| T3405 | test | Test manufacturing proposal when route is configured | T3402,T4001 | todo |
| T3406 | docs | Document replenishment decision flow | T3405 | todo |

### Barcode demo

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3501 | docs | Define barcode demo scope and standard capabilities | T1202 | todo |
| T3502 | feat | Add product barcode demo data | T3501 | todo |
| T3503 | test | Test barcode-assisted receipt and transfer demo | T3502 | todo |
| T3504 | docs | Document barcode limitations and demo steps | T3503 | todo |

## Phase 5 — Manufacturing

### Manufacturing foundation and traceability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4001 | feat | Add MRP dependency | T3113 | todo |
| T4002 | docs | Define standard-first BOM configuration | T4001 | todo |
| T4003 | feat | Add F&B BOM demo data | T4002 | todo |
| T4004 | feat | Enforce lot tracking on consumed ingredients | T4001 | todo |
| T4005 | feat | Enforce lot tracking on finished output | T4001 | todo |
| T4006 | feat | Link ingredient lots to finished-product lot traceability | T4004,T4005 | todo |
| T4007 | test | Test production with complete lot traceability | T4006 | todo |
| T4008 | test | Test production fails without ingredient lot | T4004 | todo |
| T4009 | test | Test production fails without finished lot | T4005 | todo |
| T4010 | test | Test MRP company isolation | T4007 | todo |
| T4011 | docs | Document manufacturing traceability flow | T4010 | todo |

### BOM and MO coverage

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4101 | test | Test multi-level BOM demo | T4003 | todo |
| T4102 | test | Test BOM component UoM handling | T4003,T1102 | todo |
| T4103 | docs | Document optional by-product configuration | T4003 | todo |
| T4104 | test | Test manual Manufacturing Order creation | T4001 | todo |
| T4105 | test | Test material reservation and actual consumption | T4004 | todo |
| T4106 | test | Test finished output quantity and lot | T4005 | todo |
| T4107 | test | Test scrap recording | T4001 | todo |
| T4108 | docs | Document MO lifecycle and exception paths | T4105,T4107 | todo |

### Work orders

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4201 | docs | Define Prepare Cook Pack work-center flow | T4001 | todo |
| T4202 | feat | Add three-operation work-order demo configuration | T4201 | todo |
| T4203 | test | Test work-order sequence and completion | T4202 | todo |
| T4204 | test | Test work-order duration capture | T4202 | todo |
| T4205 | docs | Document work-order demo flow | T4203 | todo |

### Manufacturing costing

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4301 | docs | Define planned-versus-actual costing formula | T4108,T4205 | todo |
| T4302 | feat | Add F&B manufacturing costing calculation | T4301 | todo |
| T4303 | feat | Add operation-cost contribution | T4302 | todo |
| T4304 | test | Test planned material cost | T4302 | todo |
| T4305 | test | Test actual cost including operation variance | T4303 | todo |
| T4306 | docs | Document costing assumptions and limitations | T4305 | todo |

## Phase 6 — Quality

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T5001 | feat | Add Quality dependency | T4001 | todo |
| T5002 | feat | Add inbound quality-control point demo | T5001 | todo |
| T5003 | feat | Add manufacturing quality-control point demo | T5001 | todo |
| T5004 | feat | Block receipt when mandatory quality check fails | T5002 | todo |
| T5005 | feat | Block production completion when mandatory check fails | T5003 | todo |
| T5006 | test | Test inbound pass path | T5004 | todo |
| T5007 | test | Test inbound fail path | T5004 | todo |
| T5008 | test | Test manufacturing fail path | T5005 | todo |
| T5009 | docs | Document quality checkpoints | T5008 | todo |
| T5101 | feat | Add quality alert severity and owner data | T5001 | todo |
| T5102 | feat | Add root-cause and corrective-action fields | T5101 | todo |
| T5103 | feat | Create quality alert from failed mandatory check | T5004,T5102 | todo |
| T5104 | test | Test failed check creates alert | T5103 | todo |
| T5105 | test | Test quality alert remains company-scoped | T5103 | todo |
| T5106 | docs | Document quality alert and corrective-action flow | T5105 | todo |

## Phase 7 — Sales and returns

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6001 | feat | Add Sales dependency | T3113 | todo |
| T6002 | feat | Validate expired-stock rule on sales delivery | T6001 | todo |
| T6003 | feat | Add return reason field | T6001 | todo |
| T6004 | feat | Require original lot on traceable returns | T6003 | todo |
| T6005 | feat | Add quarantine destination for returned food goods | T6004 | todo |
| T6006 | test | Test valid sales delivery | T6002 | todo |
| T6007 | test | Test expired sales delivery blocked | T6002 | todo |
| T6008 | test | Test return without original lot fails | T6004 | todo |
| T6009 | test | Test return enters quarantine | T6005 | todo |
| T6010 | docs | Document sales and returns flow | T6009 | todo |
| T6101 | docs | Define standard-first quotation and SO flow | T6001 | todo |
| T6102 | test | Test quotation to Sales Order confirmation | T6101 | todo |
| T6103 | test | Test stock availability and reservation path | T6101,T1202 | todo |
| T6104 | test | Test partial delivery behavior | T6102 | todo |
| T6105 | docs | Document Sales Order delivery invoice linkage | T6104 | todo |

## Phase 8 — POS and accounting basic

### POS

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6501 | feat | Add POS dependency and demo configuration | T6001 | todo |
| T6502 | docs | Define POS session and store-stock flow | T6501 | todo |
| T6503 | test | Test POS session open and close | T6502 | todo |
| T6504 | test | Test POS order reduces store stock | T6502 | todo |
| T6505 | test | Test POS pricelist or discount permission path | T6501 | todo |
| T6506 | feat | Add POS return-to-quarantine demo flow | T6005,T6501 | todo |
| T6507 | test | Test POS return enters quarantine | T6506 | todo |
| T6508 | docs | Document POS demo and reconciliation limitations | T6507 | todo |

### Accounting basic

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6601 | docs | Define basic invoice and payment scope | T6105,T6501 | todo |
| T6602 | test | Test customer invoice from Sales Order | T6601 | todo |
| T6603 | test | Test vendor bill linkage from Purchase Order | T2106,T6601 | todo |
| T6604 | test | Test POS accounting handoff at demo level | T6508,T6601 | todo |
| T6605 | test | Test invoice draft posted paid state flow | T6601 | todo |
| T6606 | test | Test basic payment reconciliation | T6605 | todo |
| T6607 | docs | Document accounting demo assumptions and exclusions | T6606 | todo |

## Phase 9 — Cross-domain approval and audit

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6701 | docs | Define reusable approval-rule model boundaries | T3307,T4011,T6105 | todo |
| T6702 | feat | Add approval rule model for model amount company role | T6701 | todo |
| T6703 | feat | Add approval state approver timestamp comment fields | T6702 | todo |
| T6704 | test | Test company-scoped generic approval rule | T6703 | todo |
| T6705 | test | Test unauthorized generic approval | T6703 | todo |
| T6706 | docs | Map PO inventory and cancellation approvals to policy | T6705 | todo |
| T6707 | security | Review generic approval ACLs and record rules | T6706 | todo |

## Phase 10 — API, integration and audit logging

### Core API

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7001 | docs | Define API contract and threat model | T6010 | todo |
| T7002 | security | Add API authentication mechanism | T7001 | todo |
| T7003 | security | Enforce company scope on every API request | T7002 | todo |
| T7004 | feat | Add paginated product endpoint | T7003 | todo |
| T7005 | feat | Add paginated stock endpoint | T7003 | todo |
| T7006 | feat | Add lot-expiry endpoint | T7003 | todo |
| T7007 | security | Add input schema validation | T7004 | todo |
| T7008 | security | Add rate-limit and replay-protection design | T7002 | todo |
| T7009 | security | Add structured audit log without sensitive payloads | T7003 | todo |
| T7010 | test | Test unauthenticated API rejection | T7002 | todo |
| T7011 | test | Test cross-company API denial | T7003 | todo |
| T7012 | test | Test pagination bounds | T7004 | todo |
| T7013 | test | Test invalid input rejection | T7007 | todo |
| T7014 | docs | Publish API examples with fake data only | T7013 | todo |

### Sales Order API and idempotency

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7101 | docs | Define Sales Order API request response and idempotency contract | T7003,T6105 | todo |
| T7102 | feat | Add POST Sales Order endpoint | T7101 | todo |
| T7103 | feat | Add GET Sales Order status endpoint | T7101 | todo |
| T7104 | security | Add company-scoped idempotency-key storage | T7102 | todo |
| T7105 | test | Test duplicate Sales Order request is idempotent | T7104 | todo |
| T7106 | test | Test Sales Order API cross-company denial | T7103 | todo |
| T7107 | docs | Publish Sales Order API examples and limitations | T7106 | todo |

### Webhook and retry

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7201 | docs | Define integration event contract | T7107 | todo |
| T7202 | feat | Add integration event log model | T7201 | todo |
| T7203 | feat | Emit Sales Order confirmed and delivery done events | T7202 | todo |
| T7204 | feat | Emit stock-below-minimum event | T3403,T7202 | todo |
| T7205 | feat | Add retry state and backoff metadata | T7202 | todo |
| T7206 | feat | Add dead-letter simulation state | T7205 | todo |
| T7207 | test | Test retry does not fail entire event batch | T7205 | todo |
| T7208 | test | Test exhausted event enters dead-letter state | T7206 | todo |

### Access and business audit

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7301 | security | Define warehouse-scoped record-rule requirements | T1202 | todo |
| T7302 | security | Add warehouse-scoped access where required | T7301 | todo |
| T7303 | test | Test warehouse access isolation | T7302 | todo |
| T7304 | docs | Document role and permission matrix | T7303,T6707 | todo |
| T7401 | docs | Define sensitive business audit events | T6707 | todo |
| T7402 | feat | Add audit log model with safe payload metadata | T7401 | todo |
| T7403 | feat | Audit PO approval and inventory adjustment | T7402,T3304 | todo |
| T7404 | feat | Audit MO cancel and price changes | T7402,T4001 | todo |
| T7405 | test | Test audit log company isolation | T7404 | todo |
| T7406 | docs | Document audit retention and sensitive-data rules | T7405 | todo |

### Observability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7501 | docs | Define API cron and integration observability fields | T7208 | todo |
| T7502 | feat | Add correlation/request ID for integration logs | T7501 | todo |
| T7503 | feat | Add failed-job operational view or report | T7501 | todo |
| T7504 | test | Test sensitive payloads are excluded from logs | T7502 | todo |
| T7505 | docs | Document operational troubleshooting flow | T7503,T7504 | todo |

## Phase 11 — Dashboard and analytics

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8001 | docs | Define operational KPIs and source models | T3209,T4011,T6010 | todo |
| T8002 | feat | Add inventory-aging KPI | T8001 | todo |
| T8003 | feat | Add near-expiry value KPI | T8001 | todo |
| T8004 | feat | Add purchase lead-time KPI | T8001 | todo |
| T8005 | feat | Add manufacturing yield KPI | T8001 | todo |
| T8006 | performance | Review ORM queries and query plans | T8002,T8003,T8004,T8005 | todo |
| T8007 | test | Test KPI company isolation | T8006 | todo |
| T8008 | docs | Document KPI definitions and limitations | T8007 | todo |
| T8101 | feat | Add below-minimum inventory KPI | T3404,T8001 | todo |
| T8102 | feat | Add open and late Purchase Order KPI | T2102,T8001 | todo |
| T8103 | feat | Add Manufacturing Order status and delay KPI | T4104,T8001 | todo |
| T8104 | feat | Add quality failure-rate KPI | T5104,T8001 | todo |
| T8105 | feat | Add Sales and POS revenue and top-product KPI | T6504,T8001 | todo |
| T8106 | feat | Add return-rate and material-waste KPI | T6009,T4107,T8001 | todo |
| T8107 | test | Test dashboard fixture values across domains | T8101,T8102,T8103,T8104,T8105,T8106 | todo |

## Phase 12 — Demo data, end-to-end tests and UAT

### Demo data

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8501 | docs | Define synthetic demo-data fixture strategy | T8107 | todo |
| T8502 | feat | Add 30 raw-material and 15 finished-product demo records | T8501 | todo |
| T8503 | feat | Add 10 vendors and 20 customers demo records | T8501 | todo |
| T8504 | feat | Add three warehouses and supporting locations demo data | T1202,T8501 | todo |
| T8505 | feat | Add 10 BOM and work-order demo configurations | T4202,T8501 | todo |
| T8506 | feat | Add 50 ingredient lots with expiry data | T3004,T8501 | todo |
| T8507 | feat | Add representative transactional demo scenarios | T8502,T8503,T8504,T8505,T8506 | todo |
| T8508 | test | Validate demo dataset installs without production data | T8507 | todo |

### E2E and UAT

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8601 | test | Run minimum SRS automated scenario coverage gate | T8508 | todo |
| T8602 | test | UAT Procure-to-Stock | T8601 | todo |
| T8603 | test | UAT Plan-to-Produce | T8601 | todo |
| T8604 | test | UAT Quality fail and corrective action | T8601 | todo |
| T8605 | test | UAT Order-to-Cash | T8601 | todo |
| T8606 | test | UAT POS sale and return | T8601 | todo |
| T8607 | test | UAT inventory count and approval | T8601 | todo |
| T8608 | test | UAT Sales Order API integration | T8601 | todo |

### Portfolio acceptance documentation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8701 | docs | Publish system architecture diagram | T8608 | todo |
| T8702 | docs | Publish module and custom-data ERD | T8701 | todo |
| T8703 | docs | Publish complete setup and demo README | T8702 | todo |
| T8704 | docs | Publish API documentation | T7107,T7208 | todo |
| T8705 | docs | Publish end-to-end business-flow documentation | T8608 | todo |
| T8706 | docs | Prepare portfolio demo script | T8705 | todo |
| T8707 | docs | Record demo evidence checklist | T8706 | todo |
| T8708 | test | Verify all SRS portfolio acceptance criteria | T8703,T8704,T8707 | todo |

## Phase 13 — Security hardening, staging and release

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T9001 | security | Review all ACLs | T7014,T8708 | todo |
| T9002 | security | Review all record rules | T9001 | todo |
| T9003 | security | Search and justify every sudo use | T9002 | todo |
| T9004 | security | Search and review every raw SQL call | T9002 | todo |
| T9005 | security | Review sensitive logging and error messages | T9002,T7505 | todo |
| T9006 | security | Test multi-company isolation end to end | T9002 | todo |
| T9007 | performance | Run representative data performance tests | T9006,T8508 | todo |
| T9008 | test | Run complete regression suite | T9007 | todo |
| T9009 | docs | Prepare final UAT evidence index | T9008,T8608 | todo |
| T9010 | docs | Prepare final demo and architecture package | T9009,T8708 | todo |
| T9011 | ci | Build release candidate image | T9008 | todo |
| T9012 | security | Generate and review SBOM | T9011 | todo |
| T9013 | docs | Write backup restore and rollback runbook | T9011 | todo |
| T9014 | ci | Deploy to protected staging environment | T9012,T9013 | todo |
| T9015 | test | Run staging smoke test | T9014 | todo |
| T9016 | docs | Publish release notes | T9015 | todo |

## Scheduled execution algorithm

1. Read `docs/BRD_Odoo_FnB_ERP.md`, `docs/SRS_Odoo_FnB_ERP.md`, this plan, `docs/PROJECT_BLUEPRINT.md`, `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`, and `docs/DEVELOPMENT_RULES.md`.
2. Find the first `todo` task whose dependencies are all `done`.
3. Prefer Standard First: configuration/test/docs tasks before custom code when Odoo standard functionality meets the requirement.
4. Create a branch using task type, ID, short name and current timestamp.
5. Create or move the matching task file to `tasks/in-progress/`.
6. Implement only that task.
7. Run declared tests and global security checks.
8. Commit with valid `## Added|Changed|Fixed`, `## Tests`, and `## Security` sections.
9. Move task to `tasks/review/` and update this table to `review`.
10. Stop on CI failure or ambiguity; mark `blocked` with evidence when appropriate.
11. Mark `done` only after merge and successful CI.
12. Before declaring a phase complete, verify its BRD/SRS rows in the traceability matrix have implementation/configuration, test, and documentation evidence.
