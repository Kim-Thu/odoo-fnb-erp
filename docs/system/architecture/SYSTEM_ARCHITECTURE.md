# Kiến trúc hệ thống hiện tại

## 1. Phạm vi tài liệu

Tài liệu này mô tả kiến trúc **đã quan sát được từ source trên `master`**. Không coi roadmap chưa triển khai là kiến trúc hiện hữu.

## 2. Module custom

### `fnb_core`

Manifest hiện khai báo:

- Odoo version: `18.0.1.3.0`
- Category: `Operations/Inventory`
- Dependencies: `base`, `product`, `stock`, `product_expiry`, `purchase`
- Data: security, warehouse demo và các view Product/Purchase.

Module dùng cách mở rộng model chuẩn của Odoo (`_inherit`) thay vì tạo lại các domain model lõi.

## 3. Model extension hiện có

| Python class | Odoo model | Vai trò custom |
|---|---|---|
| `ProductTemplate` | `product.template` | F&B SKU, shelf life, storage condition, classification, traceability |
| `PurchaseOrder` | `purchase.order` | approval state, audit fields, approve/reject, confirmation guard |
| `ResCompany` | `res.company` | purchase approval threshold |
| `ResConfigSettings` | `res.config.settings` | cấu hình threshold theo company |
| `StockLot` | `stock.lot` | tự suy ra expiration date từ shelf life khi tạo lot |
| `StockPicking` | `stock.picking` | validate lot + expiration cho incoming receipt cần traceability |

## 4. Security hiện có

Custom group `fnb_core.group_fnb_purchase_approver` có tên `Purchase Approver` và imply `purchase.group_purchase_manager`.

Purchase approval action kiểm tra group bằng `has_group`. Các audit field `approved_by_id`, `approved_at`, `rejection_reason` bị chặn direct write trừ internal context `fnb_approval_action`.

## 5. Luồng kiến trúc chính

### Purchase approval

`purchase.order` → compute threshold requirement → `pending/not_required` → approver approve hoặc reject → confirmation guard → standard Odoo `button_confirm()`.

### F&B traceability

`product.template` cấu hình traceability → lot tracking + expiration enabled → tạo `stock.lot` → expiration có thể được tính từ shelf life → incoming `stock.picking` validation kiểm tra lot/expiration → standard Odoo stock validation tiếp tục.

## 6. Nguyên tắc thiết kế quan sát được

- Standard Odoo model trước, custom bằng `_inherit`.
- Business validation đặt tại model layer.
- Approval audit fields không cho direct write từ caller thông thường.
- Company-specific approval threshold đặt trên `res.company`.
- Dữ liệu test/demo dùng synthetic data.

## 7. Chưa được xem là kiến trúc hiện hữu

Các domain Manufacturing, Quality, Sales/POS, API, Dashboard, generic approval/audit và release architecture có trong roadmap/BRD/SRS nhưng source hiện tại chưa đủ để mô tả implementation architecture chi tiết. Chúng sẽ được bổ sung khi source tương ứng được triển khai.