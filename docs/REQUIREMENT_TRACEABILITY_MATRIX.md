# Requirement Traceability Matrix

This matrix keeps BRD/SRS coverage visible. `Existing` means a task already exists in the previous master plan; `Added` means the roadmap expansion adds explicit coverage.

| Requirement | Coverage area | Task(s) | Plan status |
|---|---|---|---|
| BR-01 / FR-MD-01 | Product master | T1001-T1010 | Existing |
| BR-01 / FR-MD-02 | UoM configuration and validation | T1101-T1103 | Added |
| BR-01 / FR-MD-03 | Customer/vendor master | T1104-T1106 | Added |
| BR-01 / FR-INV-01 | Three-warehouse/location demo structure | T1201-T1203 | Added |
| BR-02 / FR-PUR-01 | RFQ/PO standard flow and partial receipt | T2101-T2103 | Added |
| BR-02 / FR-PUR-02 | Purchase approval | T2001-T2016 | Existing |
| BR-02 / FR-PUR-03 | PO/receipt/vendor-bill traceability | T2104-T2106 | Added |
| BR-03 / FR-INV-02 | Lot/expiry/FEFO | T3001-T3209 | Existing |
| BR-03 / FR-INV-03 | Inventory count and variance approval | T3301-T3307 | Added |
| BR-03 / FR-INV-04 | Reordering and source logging | T3401-T3406 | Added |
| BR-03 / FR-INV-05 | Barcode demo | T3501-T3504 | Added |
| BR-04 / FR-MRP-01 | BOM and by-product configuration | T4001-T4003, T4101-T4103 | Expanded |
| BR-04 / FR-MRP-02 | MO, consumption, output, scrap | T4004-T4011, T4104-T4108 | Expanded |
| BR-04 / FR-MRP-03 | Work orders / three operations | T4201-T4205 | Added |
| BR-04 / FR-MRP-04 | Planned vs actual costing | T4301-T4306 | Added |
| BR-05 / FR-QLT-01 | Quality control points | T5001-T5009 | Existing |
| BR-05 / FR-QLT-02 | Quality alerts and corrective action | T5101-T5106 | Added |
| BR-06 / FR-SAL-01 | Quotation/SO/ATP/delivery/invoice linkage | T6001-T6010, T6101-T6105 | Expanded |
| BR-06 / FR-SAL-02 | Return/quarantine | T6003-T6009 | Existing |
| BR-07 / FR-POS-01/02 | POS session, order, return, stock | T6501-T6508 | Added |
| FR-ACC-01/02 | Basic invoice/payment | T6601-T6607 | Added |
| BR-08 / FR-APR-01 | Generic approval/audit rules beyond PO | T6701-T6707 | Added |
| BR-09 / FR-DASH-01/02/03 | Operational dashboards | T8001-T8008, T8101-T8107 | Expanded |
| BR-10 / FR-API-01/02 | Product/stock APIs | T7001-T7014 | Existing |
| BR-10 / FR-API-03 | Sales order API + idempotency | T7101-T7107 | Added |
| BR-10 / FR-API-04 | Webhook/retry/dead-letter | T7201-T7208 | Added |
| BR-11 / FR-AUD-01 | ACL/record rules/company/warehouse isolation | T9001-T9006, T7301-T7304 | Expanded |
| BR-11 / FR-AUD-02 | Business audit log | T7401-T7406 | Added |
| BR-12 / NFR-05/06 | Environments, backup, logs, observability | T9009-T9016, T7501-T7505 | Expanded |
| SRS 4.1 | Representative demo data | T8501-T8508 | Added |
| SRS 7.1 | Minimum automated test scenarios | Domain test tasks + T8601 | Expanded |
| SRS 7.2 | UAT-01..07 | T8602-T8608 | Added |
| SRS 9 | Portfolio acceptance, architecture/ERD/docs/demo | T8701-T8708 | Added |

## Rule

A requirement is considered covered only when its mapped implementation/configuration task, test task, and required documentation evidence are merged and green in CI.
