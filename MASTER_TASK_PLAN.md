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
| T1009 | test | Test reject shelf-life âm | T1005 | done |
| T1010 | docs | Thêm product import template và field guide | T1004 | done |

### UoM và partner master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1101 | docs | Xác định cấu hình UoM theo hướng Standard First | T0016 | done |
| T1102 | test | Test UoM conversion hợp lệ trong cùng category | T1101 | done |
| T1103 | test | Test UoM conversion sai giữa các category | T1101 | done |
| T1104 | docs | Xác định cấu hình customer/vendor master data | T0016 | done |
| T1105 | test | Test demo setup cho vendor/customer master | T1104 | done |
| T1106 | docs | Thêm partner import template và field guide | T1104 | review |

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
