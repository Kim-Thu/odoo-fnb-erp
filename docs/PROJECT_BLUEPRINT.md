# Bản thiết kế tổng thể dự án

## Mục đích

Tài liệu này là bản đồ triển khai giữa BRD, SRS, năng lực chuẩn của Odoo, các module custom, luồng dữ liệu, ranh giới bảo mật, phạm vi kiểm thử và các phase phát triển.

Mục tiêu chính là giúp người phát triển và người đọc dự án trả lời rõ các câu hỏi:

- Dự án đang giải quyết bài toán nghiệp vụ nào?
- Requirement nào được đáp ứng bằng Odoo chuẩn, requirement nào cần custom?
- Dữ liệu đi qua những model nào?
- Luồng end-to-end chạy như thế nào?
- Điểm nào cần phân quyền, audit và kiểm thử multi-company?
- Phase nào phải hoàn thành trước khi mở phase tiếp theo?

## Nguyên tắc kiến trúc

Dự án xây dựng ERP cho doanh nghiệp F&B trên Odoo. Luôn ưu tiên **Standard First**: dùng cấu hình và hành vi chuẩn của Odoo trước, chỉ custom khi BRD/SRS không thể được đáp ứng rõ ràng, an toàn hoặc đủ sâu bằng cấu hình chuẩn.

Các nguyên tắc bắt buộc:

- Không viết lại tính năng chuẩn chỉ để tạo code custom.
- Dữ liệu thuộc công ty phải được giới hạn theo company scope.
- Không dùng `sudo()` để làm biến mất lỗi quyền.
- Raw SQL chỉ được dùng khi ORM thực sự không đáp ứng và phải có giải trình.
- Mọi integration phải có authentication, validation, company scope và log an toàn.
- Demo/test data phải là dữ liệu giả lập.

## Mô hình phase

| Phase | Phạm vi | Điều kiện hoàn thành phase |
|---|---|---|
| P0 | Repository, CI/CD, nền tảng security | Branch/commit validation, lint, test và container build ổn định |
| P1 | Master data và cấu hình dùng chung | Product, UoM, partner và warehouse foundation sử dụng được |
| P2 | Purchase và Procure-to-Stock | RFQ/PO, approval, receipt traceability và vendor linkage chạy được |
| P3 | Inventory lot, expiry, FEFO và reporting | Quản lý lot/expiry và chính sách hàng hết hạn hoàn chỉnh |
| P4 | Inventory operations | Inventory count approval, reordering, barcode, internal transfer chạy được |
| P5 | Manufacturing | BOM, MO, work order, lot traceability và costing chạy được |
| P6 | Quality | QCP, alert, blocking rule và corrective action chạy được |
| P7 | Sales và returns | Quotation/SO, delivery, return quarantine và invoice handoff chạy được |
| P8 | POS và accounting cơ bản | POS session/order/return và invoice/payment baseline chạy được |
| P9 | Approval và audit | Các thao tác nhạy cảm có approval/audit phù hợp |
| P10 | API và integration | API có auth, company scope, idempotency, webhook/retry |
| P11 | Dashboard và analytics | KPI vận hành đúng dữ liệu và company isolation |
| P12 | Demo data và end-to-end UAT | Dữ liệu mẫu đầy đủ, các luồng P2S/P2P-MRP/O2C/POS pass |
| P13 | Hardening và release | Security review, staging, backup/restore, RC và release docs hoàn tất |

## Bản đồ dữ liệu cốt lõi

| Domain | Odoo model/table chính | Ý định mở rộng custom |
|---|---|---|
| Product | `product.template`, `product.product` | SKU F&B, shelf life, storage condition, traceability flag |
| UoM | `uom.uom`, `uom.category` | Ưu tiên cấu hình chuẩn; test quy đổi hợp lệ và sai category |
| Partner | `res.partner` | Dùng chuẩn cho customer/vendor/payment/tax data |
| Company | `res.company` | Approval threshold và cấu hình theo công ty |
| Warehouse | `stock.warehouse`, `stock.location` | Cấu hình demo Raw Materials, Production, Finished Goods |
| Inventory | `stock.quant`, `stock.move`, `stock.picking` | Receipt validation, inventory-count approval, stock policy |
| Lot | `stock.lot` | Default expiry và rule traceability |
| Purchase | `purchase.order`, `purchase.order.line` | Approval state, audit metadata, rejection flow |
| Manufacturing | `mrp.bom`, `mrp.production`, work-order models | Traceability và costing demo khi cần |
| Quality | Các model Quality có trong edition sử dụng | QCP, alert và blocking behavior khi chuẩn chưa đủ |
| Sales | `sale.order`, `sale.order.line` | Return governance và integration endpoint |
| POS | POS session/order models | Luồng demo Standard First |
| Accounting | `account.move`, payment models | Invoice/payment cơ bản phục vụ demo end-to-end |
| Integration | Custom API/integration log models | Idempotency, retry state, dead-letter simulation, audit metadata |
| Dashboard | ORM/report models | KPI aggregation và query an toàn theo company |

## Luồng dữ liệu chính

### 1. Procure-to-Stock

Nhu cầu mua/reordering → RFQ → approval → PO → receipt → quality check → kiểm tra lot/expiry → nhập stock → liên kết vendor bill.

Dữ liệu chính đi qua:

`product.template` → `purchase.order` / `purchase.order.line` → `stock.picking` / `stock.move` → `stock.lot` → `account.move`.

### 2. Plan-to-Produce

Nhu cầu/reordering → MO → reserve nguyên liệu → consume ingredient lot → work order → quality → finished lot → nhập stock → so sánh planned/actual cost.

Dữ liệu chính đi qua:

`mrp.bom` → `mrp.production` → stock moves/lots → work-order models → quality models → costing evidence.

### 3. Order-to-Cash

Quotation → Sales Order → availability/reservation → delivery → invoice → payment.

Dữ liệu chính đi qua:

`sale.order` / `sale.order.line` → `stock.picking` → `account.move` → payment models.

### 4. POS-to-Inventory

Mở POS session → POS order/payment → trừ tồn tại cửa hàng → return/refund nếu có → đóng session → đối soát.

### 5. Inventory Adjustment

Inventory count → nhập actual quantity → tính variance → kiểm tra threshold → approval nếu vượt ngưỡng → adjustment → audit log.

### 6. Traceability nguyên liệu đến bán hàng

Vendor/PO → receipt → ingredient lot → MO consumption → finished-product lot → delivery/POS sale → return/quarantine.

Đây là một trong các luồng quan trọng nhất của hệ thống F&B và phải có evidence end-to-end trong phase UAT.

### 7. API và event

External client → authentication → schema validation → company scope → service/ORM → response/audit.

Business event → integration queue/log → retry policy → delivery thành công hoặc dead-letter state.

## Ranh giới bảo mật

- Mọi record thuộc company phải kiểm tra against allowed companies.
- Warehouse restriction được bổ sung ở nơi BRD/SRS yêu cầu.
- Không dùng `sudo()` để bypass permission failure.
- API phải có authentication rõ ràng, input allowlist và pagination bound.
- Idempotency key phải gắn với integration identity/company context.
- Không ghi token, credential, payload nhạy cảm hoặc dữ liệu cá nhân vào log.
- Approval/audit metadata phải được bảo vệ khỏi sửa trực tiếp khi cần.

## Bộ tài liệu nguồn chuẩn

Trong giai đoạn phát triển, **bản tiếng Việt là source of truth chính**. Tên model, field, API, task ID và thuật ngữ kỹ thuật có thể giữ tiếng Anh để tránh sai nghĩa kỹ thuật.

- `docs/BRD_Odoo_FnB_ERP.md` — yêu cầu nghiệp vụ.
- `docs/SRS_Odoo_FnB_ERP.md` — yêu cầu phần mềm.
- `MASTER_TASK_PLAN.md` — roadmap phase/task và dependency.
- `docs/PROJECT_BLUEPRINT.md` — phase, kiến trúc mức hệ thống, data model và data flow.
- `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` — mapping requirement → task.
- `docs/DEVELOPMENT_RULES.md` — quy tắc thực thi task/branch/PR/CI.

Bản tiếng Anh sẽ được tạo sau khi nội dung dự án ổn định để phục vụ portfolio/public documentation, không duy trì song song trong giai đoạn implementation nhằm tránh lệch nội dung và tốn công cập nhật.