# Hướng dẫn người dùng — Mục lục

## 1. Mục tiêu

Bộ user guide chỉ mô tả thao tác có căn cứ từ source/UI hiện tại. Các flow chưa triển khai sẽ ghi rõ `Planned`.

## 2. Vai trò người dùng hiện đã xác định

- Internal user.
- Purchase user / Purchase Manager theo standard Odoo Purchase.
- `Purchase Approver` — custom group của `fnb_core`.

## 3. Hướng dẫn hiện có

### Purchase Approval

Xem `PURCHASE_APPROVAL.md`.

Nội dung:

- cấu hình approval threshold;
- nhận biết trạng thái approval;
- approve PO;
- reject PO;
- confirmation guard;
- reset approval khi commercial data thay đổi;
- lỗi thường gặp.

## 4. Product master — baseline thao tác

Product Template form hiện có tab `F&B Operations` với các field:

- `F&B Internal SKU`;
- `F&B Classification`;
- `Storage Condition`;
- `Shelf Life (Days)`.

Các giá trị classification hiện có:

- Raw Material;
- Semi-finished;
- Finished Product;
- Packaging.

Storage condition:

- Ambient;
- Chilled;
- Frozen.

Validation hiện tại:

- Shelf life không được âm.
- F&B Internal SKU unique theo company.

Lưu ý: field traceability có trong model nhưng view Product hiện tại được nghiên cứu chưa hiển thị field này trong tab `F&B Operations`; cần runtime/UI verification trước khi viết thao tác click-by-click cho traceability flag.

## 5. Purchase Approval — vị trí UI đã xác minh từ XML

Purchase Order form có:

- nút `Approve F&B` trong header cho Purchase Approver;
- nút `Reject F&B` trong header cho Purchase Approver;
- block `F&B Approval` hiển thị approval state, approved by, approved at và rejection reason khi có.

Settings Purchase có block:

```text
F&B ERP
└── Purchase Approval
    └── Approval threshold
```

Tên menu điều hướng chính xác từ Odoo home tới màn hình Settings/Purchase phụ thuộc standard Odoo UI và cần runtime verification trước khi ghi từng cú click.

## 6. Planned user guides

Sẽ bổ sung khi source/evidence tương ứng đủ:

- Product master chi tiết.
- UoM và partner master.
- Warehouse/location.
- RFQ → PO.
- Partial receipt.
- Lot/expiry traceability.
- Inventory operations.
- Manufacturing.
- Quality.
- Sales/returns.
- POS.
- Accounting basic.
- API/integration operations nếu có user-facing operation.
- Dashboard.

## 7. Quy tắc viết user guide

Mỗi hướng dẫn hoàn chỉnh phải có:

1. Mục tiêu nghiệp vụ.
2. Role/quyền cần có.
3. Điều kiện trước khi thao tác.
4. Đường dẫn màn hình đã verify.
5. Các bước thực hiện.
6. Kết quả mong đợi.
7. Validation/error thường gặp.
8. Ảnh màn hình hoặc runtime evidence khi có.
9. Requirement/task liên quan.
10. Phạm vi chưa hỗ trợ.

Không mô tả nút/menu chưa được xác minh từ source hoặc runtime.