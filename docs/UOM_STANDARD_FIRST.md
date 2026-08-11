# T1101 — Cấu hình UoM theo hướng Standard First

## Mục tiêu

Xác định cách dùng UoM chuẩn của Odoo cho nghiệp vụ F&B trước khi viết custom logic, bám BR-01 / FR-MD-02 và nguyên tắc Standard First.

## Phạm vi

- Dùng model chuẩn `uom.category` và `uom.uom` của Odoo.
- Chỉ cho phép quy đổi giữa các UoM trong cùng category.
- Không thêm custom model, custom conversion engine hoặc raw SQL ở task này.
- Chuẩn hóa ví dụ nghiệp vụ cho Weight và Packaging/Unit.

## Quy tắc cấu hình

### Weight

Một category dùng cho khối lượng, với các UoM điển hình:

- kg làm reference UoM.
- g là UoM nhỏ hơn trong cùng category, quy đổi theo ratio chuẩn của Odoo.

Ví dụ nghiệp vụ:

- 1 kg = 1000 g.
- Product nguyên liệu có thể mua hoặc tồn theo kg/g miễn cùng Weight category.

### Unit / Packaging

Không coi `thùng ↔ chai` là quy đổi hợp lệ chỉ vì có quan hệ đóng gói. Chỉ dùng conversion trực tiếp khi hai UoM được cấu hình trong cùng category và business meaning thực sự là một conversion cố định.

Với trường hợp số chai mỗi thùng thay đổi theo product hoặc vendor, ưu tiên Odoo packaging/product packaging thay vì tạo UoM conversion toàn hệ thống.

## Validation kỳ vọng

- Quy đổi cùng category: hợp lệ.
- Quy đổi khác category: không được coi là conversion hợp lệ.
- Không custom để bypass validation/category semantics chuẩn của Odoo.

## Mapping yêu cầu

- BR-01: quản lý đơn vị tính và quy đổi.
- FR-MD-02: hỗ trợ quy đổi trong cùng category; ngăn quy đổi sai category; hỗ trợ ví dụ kg ↔ g và packaging khi cấu hình hợp lệ.
- SRS Data Quality: UoM phải cùng category.

## Security và multi-company

- UoM là shared configuration chuẩn; task này không thêm quyền mới, ACL, record rule hay company-owned custom data.
- Không dùng `sudo()`.
- Không dùng raw SQL.
- Không chứa secret hoặc dữ liệu thật.

## Bằng chứng cho task kế tiếp

- T1102 sẽ test conversion hợp lệ trong cùng category.
- T1103 sẽ test conversion sai giữa các category.

## Giới hạn

Task này chỉ định nghĩa cấu hình và nguyên tắc Standard First; không thêm demo data hay automated test mới.
