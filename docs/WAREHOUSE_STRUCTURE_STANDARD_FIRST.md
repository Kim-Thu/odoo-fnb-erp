# T1201 — Cấu trúc kho Raw Materials / Production / Finished Goods

## Mục tiêu

Xác định cấu trúc warehouse/location tối thiểu cho dự án F&B theo hướng Standard First, bám BR-01 và FR-INV-01 trước khi tạo demo configuration ở T1202.

## Nguyên tắc

- Ưu tiên dùng `stock.warehouse` và `stock.location` chuẩn của Odoo.
- Không tạo custom warehouse/location model.
- Không thêm route, rule hoặc automation ngoài nhu cầu của task này.
- Cấu trúc phải đủ rõ để T1202 tạo demo configuration và T1203 kiểm thử internal transfer.

## Cấu trúc tối thiểu

Dự án yêu cầu tối thiểu ba khu vực nghiệp vụ tách biệt:

1. **Raw Materials (RM)** — lưu nguyên vật liệu đầu vào.
2. **Production (PROD)** — khu vực nội bộ phục vụ cấp phát/nhận bán thành phẩm trong luồng sản xuất.
3. **Finished Goods (FG)** — lưu thành phẩm hoàn tất trước bán/giao.

Theo Standard First, T1202 có thể triển khai ba `stock.warehouse` riêng hoặc một warehouse với các internal locations tương ứng nếu vẫn đáp ứng được requirement và luồng transfer. T1201 không khóa cứng implementation khi Odoo standard cho phép nhiều cách tương đương; tiêu chí bắt buộc là ba khu vực phải phân biệt được trong dữ liệu và thao tác tồn kho.

## Location semantics

- Mỗi khu vực phải có internal location dùng được cho tồn kho thực tế.
- Location phải dùng `usage = internal` khi giữ stock thực tế.
- Không dùng supplier/customer/production virtual location để thay thế cho ba khu vực tồn kho được yêu cầu.
- T1202 phải đặt tên/code dễ đọc và ổn định cho demo/test.

## Transfer baseline

T1203 phải có thể chứng minh internal transfer giữa các khu vực đã cấu hình, tối thiểu một luồng như:

`Raw Materials → Production → Finished Goods`

Task này chỉ xác định baseline cấu trúc; không tự thêm manufacturing dependency hoặc work-order flow.

## Company scope

- Warehouse/location demo ở T1202 phải thuộc company demo hiện hành và không bypass company scope.
- Test T1203 phải tôn trọng `allowed_company_ids` và security chuẩn của Odoo.
- Không dùng `sudo()` để vượt ACL/record rule.

## Mapping yêu cầu

- BR-01: quản lý tập trung kho và vị trí kho.
- FR-INV-01: tối thiểu ba kho/khu vực Raw Materials, Production, Finished Goods; có internal location phù hợp; hỗ trợ transfer giữa location.

## Security

- Documentation-only task.
- Không raw SQL.
- Không secret hoặc production data.
- Không thay đổi ACL/record rule.

## Bằng chứng cho task kế tiếp

- T1202: thêm demo configuration cho warehouse/location theo baseline này.
- T1203: test internal transfer giữa các location đã cấu hình.

## Giới hạn

Không thêm demo records runtime, route, procurement rule, manufacturing logic hoặc test mới trong T1201.
