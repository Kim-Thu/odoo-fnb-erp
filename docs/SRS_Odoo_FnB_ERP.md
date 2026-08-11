# Software Requirements Specification (SRS)

## 1. Tổng quan

### 1.1. Tên hệ thống

Odoo ERP cho doanh nghiệp F&B.

### 1.2. Mục đích

Tài liệu này mô tả yêu cầu chức năng, phi chức năng, dữ liệu, tích hợp, phân quyền, kiểm thử và triển khai cho hệ thống ERP F&B xây dựng trên Odoo.

### 1.3. Kiến trúc mục tiêu

- **ERP Core:** Odoo.
- **Backend customization:** Python, Odoo ORM.
- **Database:** PostgreSQL.
- **UI:** Odoo XML Views, QWeb, JavaScript khi cần.
- **Integration:** REST API, webhook/queue mô phỏng.
- **Deployment:** Docker, Nginx, Linux.
- **Quality:** pylint-odoo, unit/integration test, CI.
- **Environments:** Development, Staging, Production.

## 2. User Roles

| Mã | Vai trò | Quyền chính |
|---|---|---|
| ROLE_ADMIN | System Administrator | Toàn quyền cấu hình và kỹ thuật |
| ROLE_PURCHASE | Purchase User | RFQ, PO, nhà cung cấp |
| ROLE_PURCHASE_MANAGER | Purchase Manager | Phê duyệt PO, báo cáo mua hàng |
| ROLE_INVENTORY | Inventory User | Receipt, delivery, transfer, inventory count |
| ROLE_INVENTORY_MANAGER | Inventory Manager | Điều chỉnh tồn, cấu hình kho |
| ROLE_MRP | Manufacturing User | MO, work order, consumption |
| ROLE_MRP_MANAGER | Manufacturing Manager | BOM, planning, scrap, cancel approval |
| ROLE_QUALITY | Quality User | Quality check, alert |
| ROLE_SALES | Sales User | Quotation, SO |
| ROLE_POS | POS Cashier | POS session, order, return |
| ROLE_ACCOUNTING | Accounting User | Invoice, payment cơ bản |
| ROLE_EXECUTIVE | Executive | Dashboard và báo cáo đọc |

## 3. Functional Requirements

### FR-MD: Master Data

#### FR-MD-01. Sản phẩm

Hệ thống phải cho phép tạo sản phẩm với tên, mã SKU, loại, nhóm, đơn vị tính, giá, tracking, hạn sử dụng, route và replenishment rule.

#### FR-MD-02. Đơn vị tính

- Hỗ trợ quy đổi trong cùng category.
- Ngăn quy đổi sai category.
- Cho phép ví dụ kg ↔ g, thùng ↔ chai nếu được cấu hình hợp lệ.

#### FR-MD-03. Đối tác

- Quản lý customer/vendor.
- Điều khoản thanh toán.
- Bảng giá.
- Mã số thuế và thông tin hóa đơn.

### FR-PUR: Purchase

#### FR-PUR-01. RFQ/PO

- Tạo RFQ thủ công hoặc từ reordering rule.
- Chọn vendor và purchase price.
- Xác nhận thành PO.
- Cho phép nhận hàng từng phần.

#### FR-PUR-02. Approval

- PO dưới ngưỡng A: tự xác nhận bởi Purchase Manager.
- PO từ ngưỡng A trở lên: cần cấp duyệt bổ sung.
- Không được receipt trước khi PO được duyệt.

#### FR-PUR-03. Purchase traceability

- Từ PO phải truy ra receipt và vendor bill.
- Từ receipt phải truy lại PO và lot đã nhận.

### FR-INV: Inventory

#### FR-INV-01. Warehouse structure

- Tối thiểu ba kho: Raw Materials, Production, Finished Goods.
- Mỗi kho có location nội bộ phù hợp.
- Hỗ trợ transfer giữa các location.

#### FR-INV-02. Lot và expiry

- Nguyên vật liệu bắt buộc lot khi cấu hình tracking.
- Lot có manufacturing date, expiry date và best-before date.
- Không cho xuất lot hết hạn.
- Ưu tiên FEFO khi chọn lot.

#### FR-INV-03. Inventory count

- Tạo kỳ kiểm kê.
- Nhập số lượng thực tế.
- Tính chênh lệch.
- Chênh lệch vượt ngưỡng phải được duyệt.

#### FR-INV-04. Reordering

- Khi forecast quantity dưới minimum, hệ thống tạo đề xuất mua hoặc sản xuất.
- Log nguồn tạo đề xuất.

#### FR-INV-05. Barcode

- Mỗi sản phẩm có thể có barcode.
- Cho phép quét barcode trong receipt, transfer và delivery ở mức demo.

### FR-MRP: Manufacturing

#### FR-MRP-01. BOM

- BOM nhiều cấp.
- Hỗ trợ component quantity và UoM.
- Có thể khai báo by-product nếu cần.

#### FR-MRP-02. Manufacturing Order

- Tạo MO từ nhu cầu hoặc thủ công.
- Reserve nguyên vật liệu.
- Ghi nhận tiêu hao thực tế.
- Ghi nhận thành phẩm, scrap và lot thành phẩm.

#### FR-MRP-03. Work Orders

- Thiết lập tối thiểu ba công đoạn: Chuẩn bị, Chế biến, Đóng gói.
- Theo dõi trạng thái và thời gian.

#### FR-MRP-04. Costing

- Tính chi phí từ nguyên vật liệu và chi phí công đoạn ở mức demo.
- Cho phép so sánh chi phí dự kiến và thực tế.

### FR-QLT: Quality

#### FR-QLT-01. Quality Control Point

- Thiết lập kiểm tra theo operation, product hoặc category.
- Kiểu kiểm tra: pass/fail, measure, instruction.

#### FR-QLT-02. Quality Alert

- Khi fail, tạo quality alert.
- Có severity, root cause, corrective action và owner.
- Có thể block stock move hoặc MO completion khi cấu hình.

### FR-SAL: Sales

#### FR-SAL-01. Quotation/SO

- Tạo quotation.
- Kiểm tra available-to-promise.
- Xác nhận thành SO.
- Tạo delivery và invoice.

#### FR-SAL-02. Return

- Tạo return từ delivery hoặc POS order.
- Hàng trả được đưa vào location kiểm tra riêng trước khi nhập lại kho bán được.

### FR-POS: Point of Sale

#### FR-POS-01. POS Session

- Mở/đóng ca.
- Ghi nhận số dư đầu ca và cuối ca.

#### FR-POS-02. POS Order

- Bán sản phẩm.
- Áp dụng bảng giá hoặc giảm giá theo quyền.
- Chọn phương thức thanh toán.
- Trừ tồn kho tại cửa hàng.

### FR-ACC: Accounting Basic

#### FR-ACC-01. Invoice

- Tạo customer invoice từ SO/POS.
- Tạo vendor bill từ PO.
- Theo dõi trạng thái draft/posted/paid.

#### FR-ACC-02. Payment

- Ghi nhận thanh toán cơ bản.
- Đối chiếu đơn giản theo invoice.

### FR-APR: Approval

#### FR-APR-01. Approval Rules

- Rule theo model, amount, company và role.
- Trạng thái: draft, pending, approved, rejected.
- Lưu approver, timestamp và comment.

### FR-DASH: Dashboard

#### FR-DASH-01. Inventory Dashboard

- Stock on hand.
- Forecast stock.
- Below minimum.
- Near expiry.

#### FR-DASH-02. Manufacturing Dashboard

- MO theo trạng thái.
- Delay.
- Scrap rate.
- Planned vs actual cost.

#### FR-DASH-03. Sales/POS Dashboard

- Revenue theo ngày/cửa hàng.
- Top products.
- Return rate.

### FR-API: Integration API

#### FR-API-01. Product API

- GET danh sách sản phẩm.
- GET chi tiết sản phẩm.
- Hỗ trợ filter, pagination.

#### FR-API-02. Stock API

- GET tồn kho theo warehouse/product.
- Không cho expose dữ liệu ngoài company scope.

#### FR-API-03. Sales Order API

- POST tạo đơn từ hệ thống ngoài.
- GET trạng thái đơn.
- Idempotency key để tránh tạo trùng.

#### FR-API-04. Webhook/Event

- Phát event khi SO confirmed, delivery done, stock below minimum.
- Có retry và dead-letter log mô phỏng.

### FR-AUD: Audit và Security

#### FR-AUD-01. Access Control

- ACL theo group.
- Record rule theo company và warehouse khi cần.

#### FR-AUD-02. Audit Log

- Ghi nhận thay đổi với PO approval, inventory adjustment, MO cancel và price changes.

## 4. Data Requirements

### 4.1. Dữ liệu mẫu

- 30 nguyên vật liệu.
- 15 thành phẩm.
- 10 nhà cung cấp.
- 20 khách hàng.
- 3 kho.
- 10 BOM.
- 50 lot nguyên vật liệu.
- 100 giao dịch mẫu xuyên suốt các luồng.

### 4.2. Data quality rules

- SKU là duy nhất.
- Lot number là duy nhất theo product/company.
- UoM phải cùng category.
- Không cho quantity âm trừ khi cấu hình đặc biệt.
- Không cho xác nhận giao hàng nếu thiếu stock và policy không cho backorder.

## 5. Non-functional Requirements

### NFR-01. Performance

- Danh sách dưới 10.000 record phải phản hồi trong mức chấp nhận được trên môi trường demo.
- API list có pagination.
- Truy vấn dashboard phải có index hoặc aggregation hợp lý.

### NFR-02. Reliability

- Luồng chính phải có automated test.
- Job tích hợp phải có retry.
- Không để lỗi một bản ghi làm hỏng toàn batch.

### NFR-03. Security

- Không hard-code secret.
- Sử dụng environment variable.
- API có authentication.
- Kiểm tra quyền ở controller/service layer.

### NFR-04. Maintainability

- Module chia theo domain.
- Tuân thủ Odoo coding guideline.
- Chạy pylint-odoo.
- Có README và tài liệu kỹ thuật.

### NFR-05. Deployability

- Docker Compose chạy được hệ thống.
- Có cấu hình Development/Staging/Production mẫu.
- Có migration note khi thay đổi schema/module.

### NFR-06. Observability

- Log lỗi API và cron job.
- Có correlation/request id cho tích hợp nếu triển khai được.
- Có dashboard/log cơ bản cho failed jobs.

## 6. Module Design đề xuất

| Module | Chức năng custom |
|---|---|
| fnb_core | Master data mở rộng, cấu hình chung |
| fnb_purchase_approval | Approval PO |
| fnb_inventory_expiry | Expiry, FEFO, cảnh báo |
| fnb_inventory_adjustment | Approval chênh lệch kiểm kê |
| fnb_mrp_costing | Planned vs actual costing |
| fnb_quality | Quality rule và block flow |
| fnb_sales_api | Sales/stock/product API |
| fnb_integration | Webhook, retry, integration log |
| fnb_dashboard | KPI và dashboard |
| fnb_audit | Audit log nghiệp vụ nhạy cảm |

## 7. Test Requirements

### 7.1. Automated test tối thiểu

1. PO approval theo ngưỡng.
2. Receipt bắt buộc lot.
3. Không xuất lot hết hạn.
4. Reordering tạo đề xuất đúng.
5. MO tiêu hao nguyên vật liệu và tạo thành phẩm.
6. Quality fail chặn flow.
7. SO API idempotency.
8. Record rule theo warehouse/company.
9. Inventory adjustment cần duyệt khi vượt ngưỡng.
10. Dashboard query trả số liệu đúng với fixture.

### 7.2. UAT Scenarios

- UAT-01: Mua nguyên liệu và nhập kho.
- UAT-02: Sản xuất thành phẩm theo BOM.
- UAT-03: Quality fail và corrective action.
- UAT-04: Bán hàng và giao hàng.
- UAT-05: POS sale và return.
- UAT-06: Kiểm kê và duyệt chênh lệch.
- UAT-07: API tạo Sales Order từ hệ thống ngoài.

## 8. Deployment Requirements

- Git flow đơn giản với main/develop/feature branch.
- Pull Request bắt buộc review checklist.
- CI chạy lint và test.
- Staging dùng để UAT.
- Production deploy bằng image/tag đã kiểm thử.
- Backup database trước upgrade.
- Có rollback note.

## 9. Acceptance Criteria cấp hệ thống

Hệ thống được xem là hoàn thành giai đoạn portfolio khi:

1. Docker Compose khởi chạy được.
2. Cài được toàn bộ custom modules.
3. Có dữ liệu demo.
4. Chạy được ba luồng xuyên suốt: P2P, P2P/MRP, O2C.
5. Có ít nhất 10 automated tests.
6. Có API documentation.
7. Có CI pipeline.
8. Có video hoặc tài liệu demo nghiệp vụ.
9. Có kiến trúc và ERD mức module/custom data.
10. Có README hướng dẫn setup và demo.
