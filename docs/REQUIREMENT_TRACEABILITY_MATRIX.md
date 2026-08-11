# Ma trận truy vết yêu cầu

Tài liệu này dùng để theo dõi mức độ bao phủ BRD/SRS. Mục tiêu là luôn trả lời được: **requirement nào đang được task nào triển khai, kiểm thử và chứng minh**.

Quy ước trạng thái phạm vi:

- `Đã có`: task đã tồn tại trong master plan trước khi mở rộng roadmap.
- `Bổ sung`: task mới được thêm để tránh bỏ sót BRD/SRS.
- `Mở rộng`: phạm vi cũ có nhưng chưa đủ, roadmap được bổ sung thêm task.

| Requirement | Phạm vi bao phủ | Task | Trạng thái phạm vi |
|---|---|---|---|
| BR-01 / FR-MD-01 | Product master | T1001-T1010 | Đã có |
| BR-01 / FR-MD-02 | Cấu hình và validation UoM | T1101-T1103 | Bổ sung |
| BR-01 / FR-MD-03 | Customer/vendor master | T1104-T1106 | Bổ sung |
| BR-01 / FR-INV-01 | Cấu trúc ba warehouse/location demo | T1201-T1203 | Bổ sung |
| BR-02 / FR-PUR-01 | RFQ/PO chuẩn và partial receipt | T2101-T2103 | Bổ sung |
| BR-02 / FR-PUR-02 | Purchase approval | T2001-T2016 | Đã có |
| BR-02 / FR-PUR-03 | Traceability PO/receipt/vendor bill | T2104-T2106 | Bổ sung |
| BR-03 / FR-INV-02 | Lot/expiry/FEFO | T3001-T3209 | Đã có |
| BR-03 / FR-INV-03 | Inventory count và approval variance | T3301-T3307 | Bổ sung |
| BR-03 / FR-INV-04 | Reordering và source logging | T3401-T3406 | Bổ sung |
| BR-03 / FR-INV-05 | Barcode demo | T3501-T3504 | Bổ sung |
| BR-04 / FR-MRP-01 | BOM và cấu hình by-product | T4001-T4003, T4101-T4103 | Mở rộng |
| BR-04 / FR-MRP-02 | MO, consumption, output, scrap | T4004-T4011, T4104-T4108 | Mở rộng |
| BR-04 / FR-MRP-03 | Work order / ba công đoạn | T4201-T4205 | Bổ sung |
| BR-04 / FR-MRP-04 | Planned vs actual costing | T4301-T4306 | Bổ sung |
| BR-05 / FR-QLT-01 | Quality control point | T5001-T5009 | Đã có |
| BR-05 / FR-QLT-02 | Quality alert và corrective action | T5101-T5106 | Bổ sung |
| BR-06 / FR-SAL-01 | Quotation/SO/ATP/delivery/invoice linkage | T6001-T6010, T6101-T6105 | Mở rộng |
| BR-06 / FR-SAL-02 | Return/quarantine | T6003-T6009 | Đã có |
| BR-07 / FR-POS-01/02 | POS session, order, return, stock | T6501-T6508 | Bổ sung |
| FR-ACC-01/02 | Invoice/payment cơ bản | T6601-T6607 | Bổ sung |
| BR-08 / FR-APR-01 | Approval/audit rule ngoài PO | T6701-T6707 | Bổ sung |
| BR-09 / FR-DASH-01/02/03 | Dashboard vận hành | T8001-T8008, T8101-T8107 | Mở rộng |
| BR-10 / FR-API-01/02 | Product/stock API | T7001-T7014 | Đã có |
| BR-10 / FR-API-03 | Sales Order API + idempotency | T7101-T7107 | Bổ sung |
| BR-10 / FR-API-04 | Webhook/retry/dead-letter | T7201-T7208 | Bổ sung |
| BR-11 / FR-AUD-01 | ACL/record rule/company/warehouse isolation | T9001-T9006, T7301-T7304 | Mở rộng |
| BR-11 / FR-AUD-02 | Business audit log | T7401-T7406 | Bổ sung |
| BR-12 / NFR-05/06 | Environment, backup, log, observability | T9009-T9016, T7501-T7505 | Mở rộng |
| SRS 4.1 | Representative demo data | T8501-T8508 | Bổ sung |
| SRS 7.1 | Automated test tối thiểu | Domain test tasks + T8601 | Mở rộng |
| SRS 7.2 | UAT-01..07 | T8602-T8608 | Bổ sung |
| SRS 9 | Portfolio acceptance, architecture/ERD/docs/demo | T8701-T8708 | Bổ sung |

## Quy tắc hoàn tất requirement

Một requirement chỉ được xem là **đã bao phủ hoàn chỉnh** khi tất cả phần áp dụng của nó đã merge và CI xanh:

1. Task configuration/implementation tương ứng.
2. Automated test hoặc validation evidence tương ứng.
3. Security/multi-company evidence nếu requirement liên quan dữ liệu hoặc quyền.
4. Documentation/UAT evidence nếu requirement yêu cầu tài liệu hoặc luồng end-to-end.

Không đánh dấu requirement hoàn tất chỉ vì đã có code; phải truy được từ requirement → task → test → evidence.