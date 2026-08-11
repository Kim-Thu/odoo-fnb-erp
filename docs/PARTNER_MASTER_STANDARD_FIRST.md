# T1104 — Customer/vendor master data theo hướng Standard First

## Mục tiêu

Xác định cấu hình partner master chuẩn của Odoo cho customer/vendor trong dự án F&B, bám BR-01 / FR-MD-03 và nguyên tắc Standard First.

## Phạm vi

- Dùng model chuẩn `res.partner` của Odoo làm nguồn dữ liệu customer/vendor.
- Không tạo custom partner model trong task này.
- Chuẩn hóa các trường tối thiểu phục vụ nghiệp vụ mua hàng, bán hàng và hóa đơn cơ bản.
- Chuẩn hóa cách phân biệt vai trò customer/vendor theo standard Odoo behavior và dữ liệu giao dịch thay vì tạo taxonomy riêng không cần thiết.

## Trường dữ liệu tối thiểu

Các dữ liệu cần được quản lý trên partner master khi áp dụng:

- Tên partner.
- Loại contact/company.
- Địa chỉ, quốc gia, điện thoại, email.
- Mã số thuế / VAT.
- Thông tin hóa đơn và địa chỉ invoice/delivery khi cần.
- Điều khoản thanh toán customer/vendor theo capability chuẩn của Odoo khi module liên quan được cài.
- Pricelist customer khi Sales/Pricelist capability được cài.
- Thông tin vendor phục vụ Purchase và lịch sử giao dịch chuẩn của Odoo.

## Customer/vendor role

Không thêm boolean custom `is_customer` / `is_vendor` nếu standard Odoo đã đáp ứng bằng partner rank, commercial relationship hoặc behavior chuẩn của module nghiệp vụ.

Task demo/test kế tiếp phải dùng cách tạo dữ liệu tương thích với Odoo version hiện tại và không phụ thuộc vào internal field không ổn định nếu không cần thiết.

## Payment terms và pricelist

- Customer payment term dùng field/capability chuẩn khi Accounting/Sales dependency phù hợp đã có.
- Vendor payment term dùng field/capability chuẩn khi Purchase/Accounting dependency phù hợp đã có.
- Customer pricelist dùng cấu hình chuẩn của Sales khi phase Sales được active.
- Task T1104 chỉ định nghĩa master-data contract; không tự thêm dependency lớn chỉ để hiển thị field chưa cần ở Phase 1.

## VAT và billing information

- VAT/tax identifier lưu trên field chuẩn của partner.
- Billing information ưu tiên address/contact hierarchy chuẩn của Odoo.
- Không lưu dữ liệu thật; demo/test phải dùng synthetic values.

## Multi-company và security

- Không dùng `sudo()` hoặc raw SQL.
- Không bypass ACL/record rule.
- Partner có thể được share hoặc company-scoped tùy cấu hình chuẩn; task implementation/test phải tôn trọng company semantics hiện tại của Odoo thay vì tự mở quyền.
- Không chứa secret, credential hoặc production contact data.

## Mapping yêu cầu

- BR-01: quản lý tập trung nhà cung cấp, khách hàng, bảng giá và điều khoản thanh toán.
- FR-MD-03: customer/vendor, payment terms, pricelist, mã số thuế và thông tin hóa đơn.

## Bằng chứng cho task kế tiếp

- T1105: test demo setup cho vendor/customer master theo contract này.
- T1106: partner import template và field guide.

## Giới hạn

Task này là documentation/configuration contract. Không thêm custom field, custom model, ACL, record rule hoặc demo data runtime.
