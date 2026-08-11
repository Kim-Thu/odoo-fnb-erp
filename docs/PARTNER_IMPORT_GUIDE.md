# Partner Import Guide

## Mục tiêu

Tài liệu này hướng dẫn import customer/vendor master bằng dữ liệu chuẩn của Odoo, bám BR-01 / FR-MD-03 và contract T1104. Template chỉ dùng dữ liệu synthetic và không tạo custom partner model.

## Template

File mẫu: `docs/templates/partner_import_template.csv`.

Các cột tối thiểu:

- `name`: tên partner, bắt buộc.
- `company_type`: dùng `company` hoặc `person` theo dữ liệu.
- `email`: email liên hệ synthetic.
- `phone`: số điện thoại synthetic.
- `vat`: mã số thuế / tax identifier synthetic.
- `street`: địa chỉ dòng 1.
- `city`: thành phố.
- `country_id/id`: XML ID quốc gia chuẩn khi cần xác định quốc gia.

## Customer và vendor

Không import boolean custom `is_customer` / `is_vendor`. Customer/vendor dùng cùng model `res.partner`; vai trò nghiệp vụ được hình thành theo standard Odoo behavior và giao dịch tương ứng.

Nếu cần seed dữ liệu trước nghiệp vụ Purchase/Sales, import partner master trước rồi để module nghiệp vụ cập nhật relationship/rank chuẩn thay vì tự dựng taxonomy riêng.

## Payment terms và pricelist

BRD/SRS yêu cầu payment terms và pricelist, nhưng các capability này phụ thuộc module nghiệp vụ liên quan. Ở Phase 1, template baseline không ép các field module-dependent nếu dependency chưa active.

Khi Sales/Accounting/Purchase capability tương ứng được bật, bổ sung field chuẩn qua import mapping của Odoo; không thêm custom field chỉ để phục vụ import.

## Invoice và delivery address

Khi cần nhiều địa chỉ, ưu tiên hierarchy contact/address chuẩn của Odoo. Import child contacts theo mapping chuẩn và liên kết `parent_id` thay vì nhồi nhiều địa chỉ vào một record.

## Quy trình import

1. Sao chép template và chỉ dùng dữ liệu synthetic.
2. Kiểm tra `name`, `company_type`, `email`, `phone`, `vat`, địa chỉ và quốc gia.
3. Import vào Contacts/`res.partner` bằng import UI chuẩn của Odoo.
4. Kiểm tra preview mapping trước khi xác nhận import.
5. Xác minh một sample customer và một sample vendor có thể được dùng ở các flow downstream mà không cần custom partner model.

## Data quality và security

- Không dùng dữ liệu thật, secret hoặc production contact data.
- Không dùng `sudo()` hoặc raw SQL để import.
- Không bypass ACL/record rule.
- Không tự gán company hoặc field nội bộ ngoài phạm vi import nếu không có requirement.
- VAT/email/phone trong template chỉ là synthetic fixture.

## Mapping yêu cầu

- BR-01: customer/vendor, bảng giá, thuế và điều khoản thanh toán trong master data.
- FR-MD-03: customer/vendor, payment terms, pricelist, mã số thuế và thông tin hóa đơn.
- T1104: partner master Standard First contract.
- T1105: automated demo setup cho customer/vendor master.

## Giới hạn

Template này là baseline Phase 1. Các field module-dependent như payment terms/pricelist sẽ được cấu hình/import khi dependency nghiệp vụ tương ứng active; không mở rộng architecture ở task này.
