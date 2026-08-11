# Master Task Plan

Backlog này là nguồn sự thật duy nhất (single source of truth) cho việc triển khai dự án. Kế hoạch được tổ chức theo từng phase và được đối chiếu với BRD/SRS trong `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.

## Giá trị trạng thái

- `todo`
- `in_progress`
- `review`
- `blocked`
- `done`
- `deferred`

`deferred` chỉ dùng cho task hạ tầng/CI/security không chặn tiến độ nghiệp vụ hiện tại. Task ở trạng thái này chưa được xem là hoàn tất và phải quay lại xử lý trước release/hardening cuối dự án.

## Điều kiện hoàn tất chung

Mỗi task phải đáp ứng các mục phù hợp bên dưới:

- Có positive-path test hoặc bằng chứng xác minh tương đương.
- Có validation/error-path test khi hành vi có thể thất bại.
- Có permission test khi task ảnh hưởng quyền truy cập.
- Có multi-company test khi task tác động dữ liệu thuộc company.
- Không chứa secret, token, dữ liệu cá nhân thật hoặc production configuration.
- Không dùng `sudo()` nếu không có giải trình bảo mật bằng văn bản.
- Không dùng raw SQL nếu không có giới hạn ORM được ghi rõ, parameter binding và query-plan review.
- Cập nhật tài liệu khi hành vi hoặc kiến trúc thay đổi.
- CI phải xanh trước khi chuyển sang `done`.

## Quy tắc chuyển phase và task non-blocking

- Luồng ưu tiên là hoàn tất các task nghiệp vụ và dependency thực sự cần thiết của phase hiện tại trước khi chủ động mở rộng sang phase kế tiếp.
- Tuy nhiên, task hạ tầng/CI/security trong Phase 0 có thể chuyển sang `deferred` nếu chúng **không ảnh hưởng khả năng phát triển, cài module, chạy test, kiểm tra PR hoặc xác minh an toàn cho nghiệp vụ hiện tại**.
- Task `deferred` không được coi là `done`, không được xóa khỏi roadmap và phải được hoàn tất trước Phase 13 — hardening/release hoặc sớm hơn nếu trở thành dependency/blocker.
- Không được defer các kiểm tra tối thiểu đang bảo vệ workflow hiện tại, gồm branch-name validation, commit-message validation, CI test hiện hữu và bất kỳ check nào cần để chứng minh task nghiệp vụ an toàn.
- Khi chọn task tiếp theo, dependency trực tiếp của task nghiệp vụ là điều kiện quyết định; không chặn tiến độ chỉ vì một CI enhancement không liên quan vẫn còn `todo/deferred`.
- Nếu một task `deferred` bắt đầu gây lỗi, thiếu bằng chứng kiểm thử, rủi ro security hoặc chặn deployment cần thiết, phải quay lại xử lý task đó trước khi tiếp tục nghiệp vụ.

## Phase 0 — Nền tảng repository, CI/CD và security

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T0001 | maint | Thêm workflow quản lý trạng thái task | — | done |
| T0002 | docs | Thêm task template dùng lại | T0001 | done |
| T0003 | ci | Validate branch-name format trong CI | T0002 | done |
| T0004 | ci | Validate các section bắt buộc của commit message trong CI | T0002 | review |
| T0005 | ci | Thêm Ruff configuration và lint command | — | deferred |
| T0006 | ci | Thêm XML validation cho Odoo views | T0005 | deferred |
| T0007 | security | Thêm Gitleaks configuration | — | deferred |
| T0008 | security | Thêm dependency/container vulnerability scan | T0007 | deferred |
| T0009 | ci | Chạy Odoo module install trong CI | — | deferred |
| T0010 | ci | Chạy tagged Odoo tests trong CI | T0009 | deferred |
| T0011 | ci | Upload Odoo logs khi CI failure | T0010 | deferred |
| T0012 | ci | Thêm CI concurrency cancellation | T0010 | deferred |
| T0013 | ci | Build container image trên approved branches | T0009 | deferred |
| T0014 | ci | Push immutable SHA image lên GHCR | T0013 | deferred |
| T0015 | docs | Tài liệu hóa protected production environment | T0014 | deferred |
| T0016 | docs | Thiết lập BRD/SRS project blueprint và phased roadmap | T0002 | done |

> Ghi chú Phase 0: các task `deferred` ở trên được tạm hoãn để ưu tiên bài toán nghiệp vụ. Chúng phải được đánh giá lại khi dependency thực tế cần đến và bắt buộc hoàn tất trước release/hardening cuối dự án. Những capability CI hiện đang hoạt động và bảo vệ PR không được phép vô hiệu hóa.

## Phase 1 — Master data và shared configuration

### Product master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1001 | feat | Thêm trường phân loại F&B | T0010 | done |
| T1002 | feat | Thêm trường storage condition | T1001 | done |
| T1003 | feat | Thêm trường shelf-life-days | T1001 | done |
| T1004 | feat | Thêm cờ traceability-required | T1003 | done |
| T1005 | fix | Validate shelf life không âm | T1003 | done |
| T1006 | feat | Bắt buộc F&B SKU unique theo company | T1001 | done |
| T1007 | test | Test SKU unique trong cùng company | T1006 | done |
| T1008 | test | Test cùng SKU ở các company khác nhau | T1006 | done |
| T1009 | test | Test reject shelf-life âm | T1005 | review |
| T1010 | docs | Thêm product import template và field guide | T1004 | todo |

### UoM và partner master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1101 | docs | Xác định cấu hình UoM theo hướng Standard First | T0016 | todo |
| T1102 | test | Test UoM conversion hợp lệ trong cùng category | T1101 | todo |
| T1103 | test | Test UoM conversion sai giữa các category | T1101 | todo |
| T1104 | docs | Xác định cấu hình customer/vendor master data | T0016 | todo |
| T1105 | test | Test demo setup cho vendor/customer master | T1104 | todo |
| T1106 | docs | Thêm partner import template và field guide | T1104 | todo |

### Warehouse foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1201 | docs | Xác định cấu trúc kho Raw Materials, Production, Finished Goods | T0016 | todo |
| T1202 | feat | Thêm demo configuration cho warehouse/location | T1201 | todo |
| T1203 | test | Test internal transfer giữa các location đã cấu hình | T1202 | todo |

## Phase 2 — Purchase và Procure-to-Stock

### Purchase approval

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T2001 | feat | Thêm company approval threshold | T0010 | done |
| T2002 | feat | Thêm purchase approver group | T2001 | done |
| T2003 | feat | Compute trạng thái approval-required | T2001 | done |
| T2004 | feat | Thêm approve action | T2002,T2003 | done |
| T2005 | security | Bảo vệ approval audit fields khỏi direct write | T2004 | done |
| T2006 | feat | Reset approval khi commercial fields thay đổi | T2004 | done |
| T2007 | feat | Chặn confirmation trước khi được approval | T2004 | done |
| T2008 | feat | Thêm rejection wizard | T2002 | done |
| T2009 | test | Test unauthorized approval | T2004 | todo |
| T2010 | test | Test luồng approval và confirmation | T2007 | todo |
| T2011 | test | Test reset approval sau khi đổi vendor | T2006 | todo |
| T2012 | test | Test reset approval sau khi đổi order line | T2006 | todo |
| T2013 | test | Test validation của rejection reason | T2008 | todo |
| T2014 | test | Test rejected order không được confirm | T2007,T2008 | todo |
| T2015 | test | Test approval records giữ company scope | T2004 | todo |
| T2016 | docs | Tài liệu hóa purchase approval workflow | T2015 | todo |

### Standard purchase flow và traceability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T2101 | docs | Xác định cấu hình RFQ và PO theo hướng Standard First | T1105 | todo |
| T2102 | test | Test manual RFQ to PO flow | T2101 | todo |
| T2103 | test | Test partial purchase receipt | T2101 | todo |
| T2104 | test | Test traceability từ PO đến receipt | T2103 | todo |
| T2105 | test | Test traceability từ receipt về PO và lot | T2104,T3004 | todo |
| T2106 | docs | Tài liệu hóa vendor bill linkage trong Procure-to-Stock | T2104 | todo |

## Phase 3 — Inventory lot, expiry, FEFO và reporting

### Lot và expiry

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3001 | feat | Thêm dependency `product_expiry` | T0010 | done |
| T3002 | feat | Đồng bộ traceability flag sang lot tracking | T1004,T3001 | done |
| T3003 | feat | Bật expiration handling cho traceable products | T3002 | done |
| T3004 | feat | Tự suy ra expiration mặc định từ shelf life | T3003 | done |
| T3005 | feat | Phát hiện inbound moves yêu cầu lot data | T3002 | done |
| T3006 | feat | Chặn receipt validation khi thiếu lot | T3005 | done |
| T3007 | feat | Chặn receipt validation khi thiếu expiration | T3005 | done |
| T3008 | test | Test receipt của untracked product thành công | T3006 | todo |
| T3009 | test | Test traceable receipt thiếu lot phải fail | T3006 | todo |
| T3010 | test | Test traceable receipt thiếu expiry phải fail | T3007 | todo |
| T3011 | test | Test traceable receipt đầy đủ thành công | T3007 | todo |
| T3012 | test | Test receipt checks giữ company scope | T3011 | todo |
| T3013 | docs | Tài liệu hóa inbound lot và expiry workflow | T3012 | todo |

### FEFO và expired-stock protection

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3101 | feat | Thêm demo configuration cho FEFO removal strategy | T3013 | todo |
| T3102 | feat | Phát hiện expired lots trên outbound moves | T3101 | todo |
| T3103 | feat | Chặn delivery của expired lots | T3102 | todo |
| T3104 | feat | Chặn manufacturing consumption của expired lots | T3102 | todo |
| T3105 | feat | Thêm expired-stock override group | T3103 | todo |
| T3106 | feat | Thêm mandatory override-reason wizard | T3105 | todo |
| T3107 | security | Log override user, time, reason và affected lots | T3106 | todo |
| T3108 | test | Test normal FEFO selection | T3101 | todo |
| T3109 | test | Test expired delivery bị chặn | T3103 | todo |
| T3110 | test | Test expired consumption bị chặn | T3104 | todo |
| T3111 | test | Test unauthorized override phải fail | T3106 | todo |
| T3112 | test | Test authorized override được audit | T3107 | todo |
| T3113 | docs | Tài liệu hóa FEFO và override governance | T3112 | todo |

### Inventory reporting

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3201 | feat | Thêm near-expiry lot search filter | T3013 | todo |
| T3202 | feat | Thêm expired-lot search filter | T3201 | todo |
| T3203 | feat | Thêm configurable near-expiry day threshold | T3201 | todo |
| T3204 | feat | Thêm near-expiry list action | T3203 | todo |
| T3205 | feat | Thêm stock-by-warehouse pivot | T3204 | todo |
| T3206 | performance | Review indexes cho expiry list domains | T3204 | todo |
| T3207 | test | Test near-expiry boundary dates | T3203 | todo |
| T3208 | test | Test report company isolation | T3205 | todo |
| T3209 | docs | Tài liệu hóa inventory reports | T3208 | todo |

## Phase 4 — Inventory operations

### Inventory count và variance approval

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3301 | docs | Xác định inventory-count approval policy và threshold | T1203 | todo |
| T3302 | feat | Thêm inventory variance approval configuration | T3301 | todo |
| T3303 | feat | Chặn large inventory adjustment trước approval | T3302 | todo |
| T3304 | security | Audit inventory adjustment approval metadata | T3303 | todo |
| T3305 | test | Test small variance adjustment path | T3302 | todo |
| T3306 | test | Test large variance yêu cầu approval | T3303 | todo |
| T3307 | test | Test inventory adjustment company isolation | T3304 | todo |

### Reordering

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3401 | docs | Xác định reordering rules theo hướng Standard First | T1202 | todo |
| T3402 | feat | Thêm F&B reordering demo configuration | T3401 | todo |
| T3403 | feat | Log nguồn tạo procurement proposal | T3402 | todo |
| T3404 | test | Test below-minimum purchase proposal | T3402 | todo |
| T3405 | test | Test manufacturing proposal khi route được cấu hình | T3402,T4001 | todo |
| T3406 | docs | Tài liệu hóa replenishment decision flow | T3405 | todo |

### Barcode demo

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T3501 | docs | Xác định barcode demo scope và standard capabilities | T1202 | todo |
| T3502 | feat | Thêm product barcode demo data | T3501 | todo |
| T3503 | test | Test barcode-assisted receipt và transfer demo | T3502 | todo |
| T3504 | docs | Tài liệu hóa barcode limitations và demo steps | T3503 | todo |

## Phase 5 — Manufacturing

### Manufacturing foundation và traceability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4001 | feat | Thêm MRP dependency | T3113 | todo |
| T4002 | docs | Xác định BOM configuration theo hướng Standard First | T4001 | todo |
| T4003 | feat | Thêm F&B BOM demo data | T4002 | todo |
| T4004 | feat | Bắt buộc lot tracking cho consumed ingredients | T4001 | todo |
| T4005 | feat | Bắt buộc lot tracking cho finished output | T4001 | todo |
| T4006 | feat | Liên kết ingredient lots với finished-product lot traceability | T4004,T4005 | todo |
| T4007 | test | Test production với đầy đủ lot traceability | T4006 | todo |
| T4008 | test | Test production thiếu ingredient lot phải fail | T4004 | todo |
| T4009 | test | Test production thiếu finished lot phải fail | T4005 | todo |
| T4010 | test | Test MRP company isolation | T4007 | todo |
| T4011 | docs | Tài liệu hóa manufacturing traceability flow | T4010 | todo |

### BOM và MO coverage

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4101 | test | Test multi-level BOM demo | T4003 | todo |
| T4102 | test | Test BOM component UoM handling | T4003,T1102 | todo |
| T4103 | docs | Tài liệu hóa optional by-product configuration | T4003 | todo |
| T4104 | test | Test manual Manufacturing Order creation | T4001 | todo |
| T4105 | test | Test material reservation và actual consumption | T4004 | todo |
| T4106 | test | Test finished output quantity và lot | T4005 | todo |
| T4107 | test | Test scrap recording | T4001 | todo |
| T4108 | docs | Tài liệu hóa MO lifecycle và exception paths | T4105,T4107 | todo |

### Work orders

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4201 | docs | Xác định Prepare Cook Pack work-center flow | T4001 | todo |
| T4202 | feat | Thêm demo configuration cho work order ba công đoạn | T4201 | todo |
| T4203 | test | Test work-order sequence và completion | T4202 | todo |
| T4204 | test | Test work-order duration capture | T4202 | todo |
| T4205 | docs | Tài liệu hóa work-order demo flow | T4203 | todo |

### Manufacturing costing

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4301 | docs | Xác định planned-versus-actual costing formula | T4108,T4205 | todo |
| T4302 | feat | Thêm F&B manufacturing costing calculation | T4301 | todo |
| T4303 | feat | Thêm operation-cost contribution | T4302 | todo |
| T4304 | test | Test planned material cost | T4302 | todo |
| T4305 | test | Test actual cost bao gồm operation variance | T4303 | todo |
| T4306 | docs | Tài liệu hóa costing assumptions và limitations | T4305 | todo |

## Phase 6 — Quality

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T5001 | feat | Thêm Quality dependency | T4001 | todo |
| T5002 | feat | Thêm inbound quality-control point demo | T5001 | todo |
| T5003 | feat | Thêm manufacturing quality-control point demo | T5001 | todo |
| T5004 | feat | Chặn receipt khi mandatory quality check fail | T5002 | todo |
| T5005 | feat | Chặn production completion khi mandatory check fail | T5003 | todo |
| T5006 | test | Test inbound pass path | T5004 | todo |
| T5007 | test | Test inbound fail path | T5004 | todo |
| T5008 | test | Test manufacturing fail path | T5005 | todo |
| T5009 | docs | Tài liệu hóa quality checkpoints | T5008 | todo |
| T5101 | feat | Thêm quality alert severity và owner data | T5001 | todo |
| T5102 | feat | Thêm root-cause và corrective-action fields | T5101 | todo |
| T5103 | feat | Tạo quality alert từ failed mandatory check | T5004,T5102 | todo |
| T5104 | test | Test quality alert creation và ownership | T5103 | todo |
| T5105 | test | Test corrective action lifecycle | T5102 | todo |
| T5106 | docs | Tài liệu hóa quality alert và corrective action | T5105 | todo |

## Phase 7 — Sales và returns

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6001 | feat | Thêm Sales dependency | T3113 | todo |
| T6002 | feat | Xác định return quarantine location | T6001,T1202 | todo |
| T6003 | feat | Route sales return vào quarantine | T6002 | todo |
| T6004 | feat | Thêm return inspection outcome | T6003 | todo |
| T6005 | feat | Route accepted return về stock | T6004 | todo |
| T6006 | feat | Route rejected return sang scrap | T6004 | todo |
| T6007 | test | Test accepted return flow | T6005 | todo |
| T6008 | test | Test rejected return flow | T6006 | todo |
| T6009 | test | Test return company isolation | T6007 | todo |
| T6010 | docs | Tài liệu hóa sales-return quarantine flow | T6009 | todo |
| T6101 | docs | Xác định standard quotation/SO/pricelist flow | T6001 | todo |
| T6102 | test | Test ATP/reservation trước delivery | T6101 | todo |
| T6103 | test | Test partial delivery | T6101 | todo |
| T6104 | test | Test SO to delivery and invoice linkage | T6103 | todo |
| T6105 | docs | Tài liệu hóa Order-to-Cash flow | T6104 | todo |

## Phase 8 — POS và accounting cơ bản

### POS

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6501 | docs | Xác định POS scope theo hướng Standard First | T1202 | todo |
| T6502 | feat | Thêm POS demo configuration | T6501 | todo |
| T6503 | test | Test POS session open/close | T6502 | todo |
| T6504 | test | Test POS order, payment và stock deduction | T6502 | todo |
| T6505 | test | Test pricelist/discount permission demo | T6502 | todo |
| T6506 | test | Test POS return/refund và stock movement | T6502 | todo |
| T6507 | test | Test closing balance/reconciliation demo | T6502 | todo |
| T6508 | docs | Tài liệu hóa POS-to-Inventory flow | T6507 | todo |

### Accounting basic

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6601 | docs | Xác định accounting basic scope và simulation boundary | T6105,T6508 | todo |
| T6602 | test | Test customer invoice từ Sales Order | T6601 | todo |
| T6603 | test | Test customer invoice từ POS flow | T6601 | todo |
| T6604 | test | Test vendor bill linkage từ PO | T2106,T6601 | todo |
| T6605 | test | Test draft/posted/paid invoice states | T6601 | todo |
| T6606 | test | Test basic payment/reconciliation demo | T6605 | todo |
| T6607 | docs | Tài liệu hóa accounting assumptions và demo flow | T6606 | todo |

## Phase 9 — Approval và audit

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6701 | docs | Xác định generic approval rules theo model/amount/company/role | T2016,T3307 | todo |
| T6702 | feat | Thêm generic approval rule model | T6701 | todo |
| T6703 | feat | Thêm pending/approved/rejected lifecycle | T6702 | todo |
| T6704 | feat | Ghi approver/timestamp/comment | T6703 | todo |
| T6705 | test | Test approval rule company isolation | T6704 | todo |
| T6706 | test | Test unauthorized generic approval | T6704 | todo |
| T6707 | docs | Tài liệu hóa approval governance | T6706 | todo |

## Phase 10 — API và integration

### Existing Product/Stock API foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7001 | feat | Thêm API module foundation | T0010 | todo |
| T7002 | security | Thêm API authentication boundary | T7001 | todo |
| T7003 | security | Bắt buộc company scope cho API | T7002 | todo |
| T7004 | feat | Thêm Product GET list/detail | T7003 | todo |
| T7005 | feat | Thêm filter và pagination cho Product API | T7004 | todo |
| T7006 | feat | Thêm Stock GET theo warehouse/product | T7003 | todo |
| T7007 | test | Test Product API positive path | T7005 | todo |
| T7008 | test | Test Stock API company isolation | T7006 | todo |
| T7009 | security | Validate external IDs/domain/field allowlist | T7003 | todo |
| T7010 | test | Test unauthorized API request | T7002 | todo |
| T7011 | performance | Review Product/Stock API query performance | T7005,T7006 | todo |
| T7012 | docs | Thêm Product API documentation | T7007 | todo |
| T7013 | docs | Thêm Stock API documentation | T7008 | todo |
| T7014 | test | Test API pagination boundary | T7005 | todo |

### Sales Order API và idempotency

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7101 | docs | Xác định Sales Order API contract | T6105,T7003 | todo |
| T7102 | feat | Thêm POST Sales Order API | T7101 | todo |
| T7103 | feat | Thêm idempotency-key persistence và lookup | T7102 | todo |
| T7104 | security | Scope idempotency key theo integration/company | T7103 | todo |
| T7105 | feat | Thêm GET Sales Order status API | T7102 | todo |
| T7106 | test | Test duplicate idempotency key không tạo duplicate SO | T7104 | todo |
| T7107 | docs | Tài liệu hóa Sales Order API examples/errors | T7106 | todo |

### Webhook, retry và dead-letter

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7201 | docs | Xác định event contract và retry policy | T7107 | todo |
| T7202 | feat | Thêm integration event log/queue model | T7201 | todo |
| T7203 | feat | Emit event khi SO confirmed | T7202 | todo |
| T7204 | feat | Emit event khi delivery done | T7202 | todo |
| T7205 | feat | Emit event khi stock below minimum | T7202,T3404 | todo |
| T7206 | feat | Thêm retry và dead-letter state simulation | T7202 | todo |
| T7207 | test | Test retry isolation và dead-letter transition | T7206 | todo |
| T7208 | docs | Tài liệu hóa webhook/queue operations | T7207 | todo |

### API security và observability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7301 | security | Thêm warehouse record rule cho integration scope | T7003,T1202 | todo |
| T7302 | test | Test API warehouse isolation | T7301 | todo |
| T7303 | security | Redact sensitive integration payloads trong logs | T7202 | todo |
| T7304 | test | Test log redaction cho auth/sensitive fields | T7303 | todo |
| T7501 | feat | Thêm request/correlation ID cho integration log | T7202 | todo |
| T7502 | feat | Thêm failed-job search/action | T7206 | todo |
| T7503 | test | Test correlation ID propagation | T7501 | todo |
| T7504 | test | Test failed-job observability | T7502 | todo |
| T7505 | docs | Tài liệu hóa integration observability | T7504 | todo |

## Phase 11 — Dashboard và analytics

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8001 | feat | Thêm inventory KPI model/action | T3209 | todo |
| T8002 | feat | Thêm on-hand/forecast/below-min KPI | T8001,T3404 | todo |
| T8003 | feat | Thêm near-expiry KPI | T8001,T3204 | todo |
| T8004 | feat | Thêm MRP state/delay/scrap KPI | T4108 | todo |
| T8005 | feat | Thêm planned-vs-actual MRP KPI | T4305 | todo |
| T8006 | feat | Thêm sales revenue/top-product KPI | T6105 | todo |
| T8007 | test | Test dashboard company isolation | T8002,T8006 | todo |
| T8008 | docs | Tài liệu hóa dashboard baseline | T8007 | todo |
| T8101 | feat | Thêm open/late PO KPI | T2106 | todo |
| T8102 | feat | Thêm quality defect-rate KPI | T5105 | todo |
| T8103 | feat | Thêm POS revenue theo store/channel | T6507 | todo |
| T8104 | feat | Thêm return-rate KPI | T6009,T6506 | todo |
| T8105 | feat | Thêm material-loss/scrap KPI | T4107 | todo |
| T8106 | test | Test KPI fixture với deterministic demo data | T8508 | todo |
| T8107 | docs | Tài liệu hóa KPI definitions và business meaning | T8106 | todo |

## Phase 12 — Demo data, E2E và UAT

### Representative demo data

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8501 | docs | Xác định synthetic data dictionary và naming convention | T0016 | todo |
| T8502 | feat | Thêm tối thiểu 30 raw-material demo records | T8501,T1101 | todo |
| T8503 | feat | Thêm tối thiểu 15 finished-product demo records | T8501,T1101 | todo |
| T8504 | feat | Thêm 10 vendors và 20 customers synthetic | T1105,T8501 | todo |
| T8505 | feat | Thêm 3 warehouse demo dataset | T1202,T8501 | todo |
| T8506 | feat | Thêm tối thiểu 10 BOM demo records | T4003,T8501 | todo |
| T8507 | feat | Thêm tối thiểu 50 raw-material lot records | T3011,T8501 | todo |
| T8508 | feat | Thêm tối thiểu 100 synthetic business transactions | T8502,T8503,T8504,T8505,T8506,T8507 | todo |

### Automated acceptance và UAT

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8601 | test | Chạy và ghi evidence bộ automated acceptance tối thiểu | T8508 | todo |
| T8602 | test | UAT-01 Purchase + receipt | T2106,T8508 | todo |
| T8603 | test | UAT-02 BOM manufacturing | T4305,T8508 | todo |
| T8604 | test | UAT-03 Quality fail và corrective action | T5105,T8508 | todo |
| T8605 | test | UAT-04 Sale + delivery | T6105,T8508 | todo |
| T8606 | test | UAT-05 POS sale + return | T6507,T8508 | todo |
| T8607 | test | UAT-06 Inventory count approval | T3307,T8508 | todo |
| T8608 | test | UAT-07 External Sales Order API | T7106,T8508 | todo |

### Portfolio acceptance evidence

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8701 | docs | Tài liệu hóa system architecture cuối cùng | T8601 | todo |
| T8702 | docs | Thêm module map và dependency diagram | T8701 | todo |
| T8703 | docs | Thêm ERD cho custom data/model extensions | T8701 | todo |
| T8704 | docs | Thêm role/permission matrix | T8601 | todo |
| T8705 | docs | Thêm API contract tổng hợp | T8608 | todo |
| T8706 | docs | Thêm end-to-end demo script | T8602,T8603,T8605,T8606,T8608 | todo |
| T8707 | docs | Thêm video/demo evidence guide | T8706 | todo |
| T8708 | docs | Cập nhật README setup/demo/acceptance summary | T8707 | todo |

## Phase 13 — Hardening và release

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T9001 | security | Define final group model | T8601 | todo |
| T9002 | security | Add read ACLs | T9001 | todo |
| T9003 | security | Add user write ACLs | T9002 | todo |
| T9004 | security | Add manager delete ACLs | T9003 | todo |
| T9005 | security | Add company record rule | T9002 | todo |
| T9006 | test | Test cross-company access denial | T9005 | todo |
| T9007 | security | Audit all `sudo()` usage | T9006 | todo |
| T9008 | security | Audit all raw SQL usage | T9007 | todo |
| T9009 | docs | Document environment variables | T9008 | todo |
| T9010 | ci | Finalize Dev image | T9009 | todo |
| T9011 | ci | Finalize CI image | T9010 | todo |
| T9012 | ci | Verify clean database install | T9011 | todo |
| T9013 | ci | Verify upgrade path | T9012 | todo |
| T9014 | security | Run final secret and dependency scan | T9013 | todo |
| T9015 | test | Run full automated test suite | T9014 | todo |
| T9016 | docs | Write release checklist and rollback guide | T9015 | todo |

## Completion rule

A task chỉ chuyển sang `done` sau khi PR đã merge và CI của task đã xanh. `review` chỉ dùng khi implementation/test/docs của task đã sẵn sàng để review. `deferred` chỉ dùng cho task không blocking và không được tính là hoàn tất.
