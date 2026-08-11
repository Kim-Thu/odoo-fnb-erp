# Master Task Plan

Backlog này là nguồn sự thật duy nhất (single source of truth) cho việc triển khai dự án. Kế hoạch được tổ chức theo từng phase và được đối chiếu với BRD/SRS trong `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.

## Giá trị trạng thái

- `todo`
- `in_progress`
- `review`
- `blocked`
- `done`

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

## Phase 0 — Nền tảng repository, CI/CD và security

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T0001 | maint | Thêm workflow quản lý trạng thái task | — | done |
| T0002 | docs | Thêm task template dùng lại | T0001 | done |
| T0003 | ci | Validate branch-name format trong CI | T0002 | done |
| T0004 | ci | Validate các section bắt buộc của commit message trong CI | T0002 | review |
| T0005 | ci | Thêm Ruff configuration và lint command | — | todo |
| T0006 | ci | Thêm XML validation cho Odoo views | T0005 | todo |
| T0007 | security | Thêm Gitleaks configuration | — | todo |
| T0008 | security | Thêm dependency/container vulnerability scan | T0007 | todo |
| T0009 | ci | Chạy Odoo module install trong CI | — | todo |
| T0010 | ci | Chạy tagged Odoo tests trong CI | T0009 | todo |
| T0011 | ci | Upload Odoo logs khi CI failure | T0010 | todo |
| T0012 | ci | Thêm CI concurrency cancellation | T0010 | todo |
| T0013 | ci | Build container image trên approved branches | T0009 | todo |
| T0014 | ci | Push immutable SHA image lên GHCR | T0013 | todo |
| T0015 | docs | Tài liệu hóa protected production environment | T0014 | todo |
| T0016 | docs | Thiết lập BRD/SRS project blueprint và phased roadmap | T0002 | review |

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
| T1009 | test | Test reject shelf-life âm | T1005 | todo |
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
| T4201 | docs | Xác định work-center flow Prepare → Cook → Pack | T4001 | todo |
| T4202 | feat | Thêm demo configuration cho work order 3 operations | T4201 | todo |
| T4203 | test | Test work-order sequence và completion | T4202 | todo |
| T4204 | test | Test work-order duration capture | T4202 | todo |
| T4205 | docs | Tài liệu hóa work-order demo flow | T4203 | todo |

### Manufacturing costing

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T4301 | docs | Xác định công thức planned-versus-actual costing | T4108,T4205 | todo |
| T4302 | feat | Thêm F&B manufacturing costing calculation | T4301 | todo |
| T4303 | feat | Thêm operation-cost contribution | T4302 | todo |
| T4304 | test | Test planned material cost | T4302 | todo |
| T4305 | test | Test actual cost gồm operation variance | T4303 | todo |
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
| T5104 | test | Test failed check tạo quality alert | T5103 | todo |
| T5105 | test | Test quality alert company isolation | T5103 | todo |
| T5106 | docs | Tài liệu hóa quality alert và corrective-action flow | T5104 | todo |

## Phase 7 — Sales và returns

### Sales và return governance

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6001 | feat | Thêm Sales dependency | T3113 | todo |
| T6002 | feat | Validate expired-stock rule trên sales delivery | T6001 | todo |
| T6003 | feat | Thêm return reason field | T6001 | todo |
| T6004 | feat | Yêu cầu original lot cho traceable returns | T6003 | todo |
| T6005 | feat | Thêm quarantine destination cho returned food goods | T6004 | todo |
| T6006 | test | Test valid sales delivery | T6002 | todo |
| T6007 | test | Test expired sales delivery bị chặn | T6002 | todo |
| T6008 | test | Test return thiếu original lot phải fail | T6004 | todo |
| T6009 | test | Test return đi vào quarantine | T6005 | todo |
| T6010 | docs | Tài liệu hóa sales và returns flow | T6009 | todo |

### Quotation, ATP và invoice linkage

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6101 | docs | Xác định quotation/SO flow theo hướng Standard First | T6001 | todo |
| T6102 | test | Test available-to-promise trước SO confirmation | T6101 | todo |
| T6103 | test | Test partial sales delivery | T6101 | todo |
| T6104 | test | Test SO to delivery traceability | T6103 | todo |
| T6105 | docs | Tài liệu hóa customer invoice linkage từ SO | T6104 | todo |

## Phase 8 — POS và Accounting basic

### POS

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6501 | docs | Xác định POS demo scope và standard configuration | T1202,T6001 | todo |
| T6502 | feat | Thêm POS shop/session demo configuration | T6501 | todo |
| T6503 | test | Test mở và đóng POS session | T6502 | todo |
| T6504 | test | Test POS order/payment và stock deduction | T6502 | todo |
| T6505 | test | Test POS pricelist/discount permission demo | T6502 | todo |
| T6506 | test | Test POS return/refund flow | T6504 | todo |
| T6507 | test | Test POS stock giữ company/location scope | T6504 | todo |
| T6508 | docs | Tài liệu hóa POS-to-Inventory flow | T6506 | todo |

### Accounting basic

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6601 | docs | Xác định accounting-basic demo scope | T2106,T6105,T6508 | todo |
| T6602 | test | Test customer invoice từ SO | T6601 | todo |
| T6603 | test | Test vendor bill linkage từ PO | T6601 | todo |
| T6604 | test | Test POS accounting handoff ở mức demo | T6601 | todo |
| T6605 | test | Test basic invoice payment registration | T6601 | todo |
| T6606 | test | Test simple reconciliation theo invoice | T6605 | todo |
| T6607 | docs | Tài liệu hóa giới hạn accounting và giả định demo | T6606 | todo |

## Phase 9 — Approval và audit governance

### Generic approval

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T6701 | docs | Xác định generic approval rule model theo model/amount/company/role | T0016 | todo |
| T6702 | feat | Thêm reusable approval metadata cho sensitive operations | T6701 | todo |
| T6703 | feat | Thêm approval flow cho inventory variance | T3303,T6702 | todo |
| T6704 | feat | Thêm approval flow cho conditional MO cancellation | T4108,T6702 | todo |
| T6705 | feat | Thêm approval flow cho conditional SO cancellation | T6101,T6702 | todo |
| T6706 | test | Test generic approval lifecycle draft/pending/approved/rejected | T6702 | todo |
| T6707 | test | Test generic approval company isolation | T6702 | todo |

### Business audit log

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7401 | docs | Xác định audit event schema và retention scope | T6702 | todo |
| T7402 | feat | Audit PO approval events | T7401,T2004 | todo |
| T7403 | feat | Audit inventory adjustment events | T7401,T3304 | todo |
| T7404 | feat | Audit MO cancellation events | T7401,T6704 | todo |
| T7405 | feat | Audit price-change events | T7401,T1104 | todo |
| T7406 | test | Test audit log company scope và sensitive-data exclusion | T7402,T7403,T7404,T7405 | todo |

## Phase 10 — API và integration

### API foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7001 | docs | Xác định API contract và threat model | T6010 | todo |
| T7002 | security | Thêm API authentication mechanism | T7001 | todo |
| T7003 | security | Enforce company scope trên mọi API request | T7002 | todo |
| T7004 | feat | Thêm paginated product endpoint | T7003 | todo |
| T7005 | feat | Thêm paginated stock endpoint | T7003 | todo |
| T7006 | feat | Thêm lot-expiry endpoint | T7003 | todo |
| T7007 | security | Thêm input schema validation | T7004 | todo |
| T7008 | security | Thêm rate-limit/replay-protection design | T7002 | todo |
| T7009 | security | Thêm structured audit log không chứa sensitive payloads | T7003 | todo |
| T7010 | test | Test unauthenticated API rejection | T7002 | todo |
| T7011 | test | Test cross-company API denial | T7003 | todo |
| T7012 | test | Test pagination bounds | T7004 | todo |
| T7013 | test | Test invalid input rejection | T7007 | todo |
| T7014 | docs | Publish API examples chỉ dùng fake data | T7013 | todo |

### Sales Order API và idempotency

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7101 | docs | Xác định Sales Order API schema và idempotency contract | T7003,T6101 | todo |
| T7102 | feat | Thêm POST Sales Order endpoint | T7101 | todo |
| T7103 | feat | Thêm GET Sales Order status endpoint | T7101 | todo |
| T7104 | security | Validate field allowlist và company/customer scope | T7102 | todo |
| T7105 | feat | Thêm idempotency-key storage và replay handling | T7102 | todo |
| T7106 | test | Test duplicate Sales Order request không tạo order trùng | T7105 | todo |
| T7107 | test | Test Sales Order API cross-company denial | T7104 | todo |

### Webhook/event và retry

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7201 | docs | Xác định event contract cho SO confirmed, delivery done, stock below minimum | T7103,T3404 | todo |
| T7202 | feat | Thêm integration event/log model | T7201 | todo |
| T7203 | feat | Emit configured business events | T7202 | todo |
| T7204 | feat | Thêm retry state và backoff policy | T7202 | todo |
| T7205 | feat | Thêm simulated dead-letter state | T7204 | todo |
| T7206 | test | Test event retry sau transient failure | T7204 | todo |
| T7207 | test | Test event chuyển sang dead-letter sau retry limit | T7205 | todo |
| T7208 | docs | Tài liệu hóa integration event operations | T7207 | todo |

### API security và observability

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T7301 | security | Xác định warehouse-scoped API authorization | T7003,T1202 | todo |
| T7302 | test | Test warehouse-scoped API denial | T7301 | todo |
| T7303 | security | Thêm correlation/request id cho integration logs | T7202 | todo |
| T7304 | test | Test API logs loại bỏ credentials và sensitive payloads | T7303 | todo |
| T7501 | docs | Xác định application/integration observability baseline | T7208 | todo |
| T7502 | feat | Thêm failed integration job view/report | T7501 | todo |
| T7503 | ci | Giữ failed-job logs/artifacts trong CI | T7501 | todo |
| T7504 | test | Test batch processing cô lập lỗi từng record | T7204 | todo |
| T7505 | docs | Tài liệu hóa troubleshooting và correlation workflow | T7502,T7503 | todo |

## Phase 11 — Dashboard và analytics

### Core KPI

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8001 | docs | Xác định operational KPIs và source models | T3209,T4011,T6010 | todo |
| T8002 | feat | Thêm inventory-aging KPI | T8001 | todo |
| T8003 | feat | Thêm near-expiry value KPI | T8001 | todo |
| T8004 | feat | Thêm purchase lead-time KPI | T8001 | todo |
| T8005 | feat | Thêm manufacturing yield KPI | T8001 | todo |
| T8006 | performance | Review ORM queries và query plans | T8002,T8003,T8004,T8005 | todo |
| T8007 | test | Test KPI company isolation | T8006 | todo |
| T8008 | docs | Tài liệu hóa KPI definitions và limitations | T8007 | todo |

### Dashboard coverage theo BRD/SRS

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8101 | feat | Thêm stock on hand/forecast/below-minimum dashboard metrics | T8001,T3404 | todo |
| T8102 | feat | Thêm MO status/delay dashboard metrics | T8001,T4108 | todo |
| T8103 | feat | Thêm scrap-rate và planned-vs-actual-cost metrics | T8001,T4305 | todo |
| T8104 | feat | Thêm revenue/top-products/return-rate metrics | T8001,T6508 | todo |
| T8105 | feat | Thêm quality-failure-rate metric | T8001,T5104 | todo |
| T8106 | test | Test dashboard fixture calculations | T8101,T8102,T8103,T8104,T8105 | todo |
| T8107 | docs | Tài liệu hóa dashboard source-of-truth và refresh assumptions | T8106 | todo |

## Phase 12 — Demo data, end-to-end và portfolio evidence

### Representative demo data

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8501 | docs | Xác định synthetic demo-data catalog và naming rules | T0016 | todo |
| T8502 | feat | Thêm 30 raw materials và 15 finished products demo | T8501,T1010 | todo |
| T8503 | feat | Thêm 10 vendors và 20 customers demo | T8501,T1106 | todo |
| T8504 | feat | Thêm 3 warehouses/locations và 10 BOMs demo | T8501,T1202,T4003 | todo |
| T8505 | feat | Thêm 50 ingredient lots với expiry demo | T8502,T3004 | todo |
| T8506 | feat | Thêm representative transactional demo data | T8503,T8504,T8505 | todo |
| T8507 | security | Validate demo data chỉ là synthetic data | T8506 | todo |
| T8508 | docs | Tài liệu hóa demo dataset và reset/reload procedure | T8507 | todo |

### Automated acceptance và UAT

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8601 | test | Chạy/ghi nhận minimum automated acceptance scenarios từ SRS 7.1 | T8508 | todo |
| T8602 | test | UAT-01: mua nguyên liệu và nhập kho | T8601 | todo |
| T8603 | test | UAT-02: sản xuất thành phẩm theo BOM | T8601 | todo |
| T8604 | test | UAT-03: Quality fail và corrective action | T8601 | todo |
| T8605 | test | UAT-04: bán hàng và giao hàng | T8601 | todo |
| T8606 | test | UAT-05: POS sale và return | T8601 | todo |
| T8607 | test | UAT-06: kiểm kê và duyệt chênh lệch | T8601 | todo |
| T8608 | test | UAT-07: API tạo Sales Order từ external system | T8601 | todo |

### Portfolio acceptance evidence

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T8701 | docs | Viết system architecture document cuối cùng | T8608 | todo |
| T8702 | docs | Viết module/custom-data ERD | T8701 | todo |
| T8703 | docs | Hoàn thiện role/permission matrix | T8701 | todo |
| T8704 | docs | Hoàn thiện API documentation và fake examples | T7014,T7107,T7208 | todo |
| T8705 | docs | Hoàn thiện README setup/demo guide | T8701 | todo |
| T8706 | docs | Chuẩn bị end-to-end demo script | T8608 | todo |
| T8707 | docs | Ghi nhận P2S, P2P/MRP, O2C và POS demo evidence | T8706 | todo |
| T8708 | docs | Đối chiếu toàn bộ SRS system acceptance criteria | T8702,T8703,T8704,T8705,T8707 | todo |

## Phase 13 — Security hardening và release

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T9001 | security | Review toàn bộ ACLs | T7014,T8708 | todo |
| T9002 | security | Review toàn bộ record rules | T9001 | todo |
| T9003 | security | Tìm và justify mọi `sudo()` | T9002 | todo |
| T9004 | security | Tìm và review mọi raw SQL call | T9002 | todo |
| T9005 | security | Review sensitive logging và error messages | T9002 | todo |
| T9006 | security | Test multi-company isolation end to end | T9002 | todo |
| T9007 | performance | Chạy representative-data performance tests | T9006,T8508 | todo |
| T9008 | test | Chạy complete regression suite | T9007 | todo |
| T9009 | docs | Chuẩn bị UAT/release sign-off checklist | T9008 | todo |
| T9010 | docs | Chuẩn bị final demo script và architecture diagram | T9009 | todo |
| T9011 | ci | Build release candidate image | T9008 | todo |
| T9012 | security | Generate và review SBOM | T9011 | todo |
| T9013 | docs | Viết backup, restore và rollback runbook | T9011 | todo |
| T9014 | ci | Deploy lên protected staging environment | T9012,T9013 | todo |
| T9015 | test | Chạy staging smoke test | T9014 | todo |
| T9016 | docs | Publish release notes | T9015 | todo |

## Thuật toán tiếp tục task theo lịch

1. Đọc file này và `docs/DEVELOPMENT_RULES.md`.
2. Tìm task `todo` đầu tiên mà toàn bộ dependencies đã `done`.
3. Tạo branch theo task type, ID, short name và timestamp hiện tại.
4. Tạo hoặc chuyển task file tương ứng sang `tasks/in-progress/`.
5. Chỉ triển khai đúng task đó.
6. Chạy các test đã khai báo và global security checks.
7. Commit với các section chi tiết `Added/Changed/Fixed/Tests/Security`.
8. Chuyển task sang `tasks/review/` và cập nhật bảng này thành `review`.
9. Dừng khi CI fail hoặc requirement còn mơ hồ; đánh dấu `blocked` kèm evidence.
10. Chỉ chuyển `done` sau khi merge và CI thành công.
