# Business Requirements Document (BRD)

## 1. Thông tin tài liệu

- **Tên dự án:** Odoo ERP cho doanh nghiệp F&B
- **Phiên bản:** 1.0
- **Mục tiêu:** Xây dựng một hệ thống ERP nội bộ trên Odoo để quản lý xuyên suốt quy trình mua hàng, kho, sản xuất, chất lượng, bán hàng, POS và báo cáo vận hành.
- **Đối tượng sử dụng:** Ban giám đốc, mua hàng, kho, sản xuất, kiểm soát chất lượng, bán hàng, cửa hàng/POS, kế toán và quản trị hệ thống.

## 2. Bối cảnh kinh doanh

Doanh nghiệp F&B đang vận hành nhiều quy trình bằng Excel, tin nhắn và thao tác thủ công. Dữ liệu nguyên vật liệu, tồn kho, đơn mua, lệnh sản xuất, chất lượng và doanh thu chưa được đồng bộ. Điều này gây ra:

- Sai lệch tồn kho giữa thực tế và báo cáo.
- Khó truy vết nguyên vật liệu theo lô và hạn sử dụng.
- Chậm lập kế hoạch mua hàng và sản xuất.
- Thiếu kiểm soát định mức nguyên liệu và hao hụt.
- Khó kiểm soát chất lượng đầu vào, trong quá trình sản xuất và đầu ra.
- Dữ liệu bán hàng và POS không được liên kết đầy đủ với kho và sản xuất.
- Báo cáo quản trị chậm, phụ thuộc Excel.

## 3. Mục tiêu kinh doanh

1. Chuẩn hóa quy trình mua hàng, nhập kho, sản xuất, xuất bán và kiểm soát chất lượng.
2. Quản lý tồn kho theo nhiều kho, vị trí, lô, hạn sử dụng và đơn vị tính.
3. Tự động đề xuất mua hàng hoặc sản xuất khi tồn kho xuống dưới ngưỡng.
4. Theo dõi nguyên vật liệu từ lúc nhập kho đến thành phẩm và bán ra.
5. Giảm thao tác nhập liệu lặp lại và phụ thuộc Excel.
6. Cung cấp dashboard vận hành gần thời gian thực.
7. Tạo nền tảng tích hợp với POS, ứng dụng giao hàng, hóa đơn điện tử và hệ thống bên ngoài.
8. Đảm bảo hệ thống có thể kiểm thử, triển khai, giám sát và nâng cấp an toàn.

## 4. Phạm vi dự án

### 4.1. Trong phạm vi

- Quản lý danh mục dùng chung.
- Purchase.
- Inventory.
- Manufacturing (MRP).
- Quality.
- Sales.
- POS.
- Accounting ở mức cơ bản phục vụ hóa đơn và thanh toán.
- Dashboard vận hành.
- Approval workflow.
- REST API tích hợp.
- Phân quyền và nhật ký thay đổi.
- Import dữ liệu ban đầu.
- Automated test, CI và triển khai ba môi trường.

### 4.2. Ngoài phạm vi giai đoạn 1

- Payroll.
- Recruitment.
- Performance appraisal.
- Kế toán tài chính chuyên sâu theo toàn bộ chuẩn Việt Nam.
- AI dự báo nhu cầu ở mức production.
- Tích hợp thật với cổng thanh toán, hóa đơn điện tử hoặc nền tảng giao hàng nếu không có sandbox/API.
- Ứng dụng mobile native.

## 5. Các bên liên quan

| Nhóm | Trách nhiệm |
|---|---|
| Ban giám đốc | Phê duyệt phạm vi, chính sách và KPI |
| Mua hàng | Quản lý RFQ, PO, nhà cung cấp, giá mua |
| Kho | Nhập, xuất, chuyển kho, kiểm kê, lot/expiry |
| Sản xuất | BOM, MO, work order, tiêu hao, thành phẩm |
| Quality | Điểm kiểm tra, tiêu chí, lỗi và xử lý |
| Sales | Báo giá, đơn bán, giao hàng, hóa đơn |
| POS/Cửa hàng | Giao dịch tại điểm bán, trả hàng, đóng ca |
| Kế toán | Hóa đơn, thanh toán, đối chiếu cơ bản |
| IT/Admin | Phân quyền, cấu hình, tích hợp, triển khai |

## 6. Quy trình nghiệp vụ mục tiêu

### 6.1. Procure-to-Stock

Nhu cầu mua hàng → RFQ → phê duyệt → Purchase Order → nhận hàng → kiểm tra chất lượng → nhập kho → ghi nhận công nợ nhà cung cấp.

### 6.2. Plan-to-Produce

Nhu cầu bán hàng hoặc mức tồn kho → kế hoạch sản xuất → Manufacturing Order → cấp phát nguyên liệu → sản xuất → kiểm tra chất lượng → nhập kho thành phẩm.

### 6.3. Order-to-Cash

Báo giá → Sales Order → giữ hàng → giao hàng → hóa đơn → thanh toán.

### 6.4. POS-to-Inventory

Đơn POS → trừ tồn kho → ghi nhận doanh thu → trả hàng/hoàn tiền nếu có → đóng ca và đối soát.

## 7. Business Requirements

### BR-01. Quản lý Master Data

Hệ thống phải quản lý tập trung:

- Sản phẩm, nguyên vật liệu, thành phẩm.
- Nhóm sản phẩm.
- Đơn vị tính và quy đổi.
- Nhà cung cấp, khách hàng.
- Kho, vị trí kho.
- Bảng giá, thuế, điều khoản thanh toán.
- BOM và công đoạn sản xuất.

### BR-02. Quản lý mua hàng

- Tạo RFQ và Purchase Order.
- Hỗ trợ nhiều nhà cung cấp cho một sản phẩm.
- Lưu lịch sử giá mua.
- Phê duyệt PO theo giá trị hoặc nhóm hàng.
- Nhận hàng từng phần.
- Liên kết PO với receipt và vendor bill.

### BR-03. Quản lý kho

- Quản lý nhiều kho và vị trí.
- Theo dõi tồn khả dụng, tồn dự kiến và tồn giữ chỗ.
- Theo dõi lot/serial và hạn sử dụng.
- Hỗ trợ FIFO/FEFO theo cấu hình.
- Kiểm kê và điều chỉnh tồn.
- Chuyển kho nội bộ.
- Reordering rule.
- Cảnh báo hàng sắp hết hạn hoặc dưới mức tối thiểu.

### BR-04. Quản lý sản xuất

- Quản lý BOM nhiều cấp.
- Tạo Manufacturing Order.
- Theo dõi cấp phát và tiêu hao nguyên vật liệu.
- Ghi nhận hao hụt, phế phẩm và thành phẩm.
- Theo dõi work order/công đoạn.
- Tính chi phí sản xuất ở mức phục vụ vận hành.

### BR-05. Quản lý chất lượng

- Thiết lập quality control point.
- Kiểm tra nguyên liệu đầu vào, bán thành phẩm và thành phẩm.
- Ghi nhận kết quả pass/fail.
- Ghi nhận lỗi, nguyên nhân và hành động xử lý.
- Chặn nhập kho hoặc xuất bán khi chất lượng không đạt.

### BR-06. Quản lý bán hàng

- Quotation và Sales Order.
- Bảng giá theo khách hàng hoặc kênh bán.
- Kiểm tra tồn trước khi xác nhận đơn.
- Giao hàng từng phần.
- Trả hàng.
- Liên kết đơn bán, delivery và invoice.

### BR-07. Quản lý POS

- Bán hàng tại cửa hàng.
- Chọn bảng giá, khuyến mãi và phương thức thanh toán.
- Trừ kho theo điểm bán.
- Đổi/trả hàng.
- Đóng ca và đối soát doanh thu.

### BR-08. Approval Workflow

- Phê duyệt Purchase Order theo ngưỡng giá trị.
- Phê duyệt điều chỉnh tồn lớn.
- Phê duyệt hủy Manufacturing Order hoặc Sales Order theo điều kiện.
- Lưu người duyệt, thời gian và ghi chú.

### BR-09. Dashboard và báo cáo

Tối thiểu gồm:

- Tồn kho theo kho, nhóm hàng và hạn sử dụng.
- Hàng dưới mức tối thiểu.
- PO đang mở và PO trễ.
- MO theo trạng thái.
- Tỷ lệ lỗi chất lượng.
- Doanh thu theo cửa hàng/kênh.
- Top sản phẩm.
- Hao hụt nguyên vật liệu.

### BR-10. Tích hợp

- REST API cho sản phẩm, tồn kho, đơn bán và trạng thái đơn.
- Webhook hoặc queue mô phỏng cho đồng bộ sự kiện.
- Cơ chế retry và log lỗi tích hợp.
- API key hoặc token-based authentication.

### BR-11. Bảo mật và phân quyền

- Phân quyền theo vai trò.
- Record rule theo công ty/kho/bộ phận khi cần.
- Audit log cho thao tác nhạy cảm.
- Không cho người dùng xem hoặc sửa dữ liệu ngoài phạm vi.

### BR-12. Vận hành hệ thống

- Có môi trường Development, Staging và Production.
- Có quy trình backup và restore.
- Có log ứng dụng và giám sát lỗi.
- Có automated test cho các luồng quan trọng.
- Có CI trước khi merge.

## 8. KPI thành công

- Giảm tối thiểu 50% file Excel vận hành chính.
- Sai lệch tồn kho dưới 2% trong giai đoạn chạy thử.
- 100% PO, MO, SO trọng yếu được theo dõi trên hệ thống.
- 100% sản phẩm cần truy xuất được quản lý lot/expiry.
- Có thể truy vết từ nguyên liệu đến thành phẩm và đơn bán.
- Luồng chính có automated test và chạy thành công trên CI.
- Người dùng hoàn thành UAT cho các quy trình trọng yếu.

## 9. Ràng buộc và giả định

- Sử dụng Odoo Community hoặc môi trường phù hợp để phát triển.
- Dữ liệu mẫu được mô phỏng, không dùng dữ liệu thật của doanh nghiệp.
- Một số nghiệp vụ kế toán hoặc tích hợp bên thứ ba chỉ được mô phỏng.
- Dự án ưu tiên Standard First, chỉ custom khi tính năng chuẩn không đáp ứng.
- Phạm vi phải đủ sâu để trình bày trong phỏng vấn, nhưng vẫn hoàn thành được bởi một developer cá nhân.
