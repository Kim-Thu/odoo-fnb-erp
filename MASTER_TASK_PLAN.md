# Master Task Plan

This backlog is the single source of truth for delivery. A scheduled worker must select only the first `todo` task whose dependencies are `done`.

## Status values

- `todo`
- `in_progress`
- `review`
- `blocked`
- `done`

## Global completion gates

Every code task must include:

- Positive-path test.
- Validation/error-path test.
- Permission test when access is affected.
- Multi-company test when company-owned records are affected.
- No secret, token, real personal data or production configuration.
- No `sudo()` without a written security justification.
- No raw SQL without a written ORM limitation, parameter binding and query-plan review.
- CI must pass before `done`.

## Epic 00 — Repository and delivery foundation

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

## Epic 10 — Product master data

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1001 | feat | Add F&B classification field | T0010 | done |
| T1002 | feat | Add storage-condition field | T1001 | done |
| T1003 | feat | Add shelf-life-days field | T1001 | done |
| T1004 | feat | Add traceability-required flag | T1003 | done |
| T1005 | fix | Validate shelf life is non-negative | T1003 | done |
| T1006 | feat | Enforce F&B SKU uniqueness by company | T1001 | done |
| T1007 | test | Test SKU uniqueness in same company | T1006 | done |
| T1008 | test | Test same SKU across different companies | T1006 | review |
| T1009 | test | Test negative shelf-life rejection | T1005 | todo |
| T1010 | docs | Add product import template and field guide | T1004 | todo |

## Epic 20 — Purchase approval

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

## Epic 30 — Inventory lot and expiry

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3001 | feat | Add `product_expiry` dependency | T0010 | done |
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

## Epic 31 — FEFO and expired-stock protection

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3101 | feat | Add FEFO removal strategy demo configuration | T3013 | todo |
| T3102 | feat | Detect expired lots on outbound moves | T3101 | todo |
| T3103 | feat | Block delivery of expired lots | T3102 | todo |
| T3104 | feat | Block manufacturing consumption of expired lots | T3102 | todo |
| T3105 | feat | Add expired-stock override group | T3103 | todo |
| T3106 | feat | Add mandatory override-reason wizard | T3105 | todo |
| T3107 | security | Log override user, time, reason and affected lots | T3106 | todo |
| T3108 | test | Test normal FEFO selection | T3101 | todo |
| T3109 | test | Test expired delivery is blocked | T3103 | todo |
| T3110 | test | Test expired consumption is blocked | T3104 | todo |
| T3111 | test | Test unauthorized override fails | T3106 | todo |
| T3112 | test | Test authorized override is audited | T3107 | todo |
| T3113 | docs | Document FEFO and override governance | T3112 | todo |

## Epic 32 — Inventory reporting

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

## Epic 40 — Manufacturing foundation

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

## Epic 50 — Quality

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

## Epic 60 — Sales and returns

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

## Epic 70 — Integration API

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7001 | docs | Define API contract and threat model | T6010 | todo |
| T7002 | security | Add API authentication mechanism | T7001 | todo |
| T7003 | security | Enforce company scope on every API request | T7002 | todo |
| T7004 | feat | Add paginated product endpoint | T7003 | todo |
| T7005 | feat | Add paginated stock endpoint | T7003 | todo |
| T7006 | feat | Add lot-expiry endpoint | T7003 | todo |
| T7007 | security | Add input schema validation | T7004 | todo |
| T7008 | security | Add rate-limit/replay-protection design | T7002 | todo |
| T7009 | security | Add structured audit log without sensitive payloads | T7003 | todo |
| T7010 | test | Test unauthenticated API rejection | T7002 | todo |
| T7011 | test | Test cross-company API denial | T7003 | todo |
| T7012 | test | Test pagination bounds | T7004 | todo |
| T7013 | test | Test invalid input rejection | T7007 | todo |
| T7014 | docs | Publish API examples with fake data only | T7013 | todo |

## Epic 80 — Dashboard and analytics

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

## Epic 90 — Security hardening and release

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T9001 | security | Review all ACLs | T7014,T8008 | todo |
| T9002 | security | Review all record rules | T9001 | todo |
| T9003 | security | Search and justify every `sudo()` | T9002 | todo |
| T9004 | security | Search and review every raw SQL call | T9002 | todo |
| T9005 | security | Review sensitive logging and error messages | T9002 | todo |
| T9006 | security | Test multi-company isolation end to end | T9002 | todo |
| T9007 | performance | Run representative data performance tests | T9006 | todo |
| T9008 | test | Run complete regression suite | T9007 | todo |
| T9009 | docs | Prepare UAT scenarios | T9008 | todo |
| T9010 | docs | Prepare demo script and architecture diagram | T9009 | todo |
| T9011 | ci | Build release candidate image | T9008 | todo |
| T9012 | security | Generate and review SBOM | T9011 | todo |
| T9013 | docs | Write backup, restore and rollback runbook | T9011 | todo |
| T9014 | ci | Deploy to protected staging environment | T9012,T9013 | todo |
| T9015 | test | Run staging smoke test | T9014 | todo |
| T9016 | docs | Publish release notes | T9015 | todo |

## Scheduled execution algorithm

1. Read this file and `docs/DEVELOPMENT_RULES.md`.
2. Find the first `todo` task with all dependencies marked `done`.
3. Create a branch using the task type, ID, short name and current timestamp.
4. Create or move the matching task file to `tasks/in-progress/`.
5. Implement only that task.
6. Run its declared tests and global security checks.
7. Commit with detailed Added/Changed/Fixed/Tests/Security sections.
8. Move the task to `tasks/review/` and update this table to `review`.
9. Stop on CI failure or ambiguity; mark `blocked` with evidence.
10. Mark `done` only after merge and successful CI.
