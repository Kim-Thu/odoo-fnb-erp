# Data Model hiện tại

## 1. Mục tiêu

Ghi lại các field và constraint custom thực sự tồn tại trong `fnb_core`. Đây chưa phải ERD toàn bộ Odoo database.

## 2. `product.template`

Custom fields:

| Field | Type | Ý nghĩa |
|---|---|---|
| `fnb_internal_sku` | Char | mã nghiệp vụ nội bộ F&B |
| `fnb_shelf_life_days` | Integer | shelf life kỳ vọng, không âm |
| `fnb_storage_condition` | Selection | `ambient`, `chilled`, `frozen` |
| `fnb_ingredient_classification` | Selection | `raw`, `semi_finished`, `finished`, `packaging` |
| `fnb_requires_traceability` | Boolean | yêu cầu lot + expiry traceability |

Constraint custom:

- `(fnb_internal_sku, company_id)` unique.
- `fnb_shelf_life_days >= 0`.
- Nếu `fnb_requires_traceability = True` thì `tracking = lot` và `use_expiration_date = True`.

## 3. `purchase.order`

Custom fields:

| Field | Type | Ý nghĩa |
|---|---|---|
| `approval_state` | computed Selection | `not_required`, `pending`, `approved`, `rejected` |
| `approval_required` | computed Boolean | PO có vượt threshold cần approval hay không |
| `approved_by_id` | Many2one → `res.users` | người duyệt |
| `approved_at` | Datetime | thời điểm duyệt |
| `rejection_reason` | Text | lý do từ chối |

Approval phụ thuộc `amount_total`, company threshold, approver audit và rejection reason.

Các thay đổi `partner_id`, `currency_id`, `company_id`, `order_line` sẽ reset approval/rejection hiện hữu.

## 4. `res.company`

| Field | Type | Ý nghĩa |
|---|---|---|
| `fnb_purchase_approval_limit` | Monetary | ngưỡng PO cần approval theo company |

`res.config.settings.fnb_purchase_approval_limit` là related field cho phép cấu hình giá trị này.

## 5. `stock.lot`

Không thêm field mới trong source hiện tại. Override `create()` để tự điền field chuẩn `expiration_date` khi:

- caller chưa truyền expiration date;
- có `product_id`;
- product yêu cầu F&B traceability;
- `fnb_shelf_life_days > 0`.

Giá trị được tính từ thời điểm hiện tại + shelf life days.

## 6. `stock.picking`

Không thêm field mới trong source hiện tại. Override validation cho incoming picking để yêu cầu move line có quantity > 0 của product traceable phải có:

- `lot_id`;
- `lot_id.expiration_date`.

## 7. Quan hệ dữ liệu chính

```text
res.company
  └─ fnb_purchase_approval_limit
       ↓
purchase.order ── approved_by_id ──> res.users

product.template
  ├─ F&B classification / storage / shelf life
  └─ traceability config
       ↓
product.product
       ↓
stock.lot ── expiration_date
       ↓
stock.move.line
       ↓
stock.picking
```

## 8. Giới hạn

Các bảng vật lý, index chuẩn Odoo, field inherited từ module chuẩn và quan hệ đầy đủ của Purchase/Stock chưa được liệt kê ở đây. Cần nghiên cứu sâu source Odoo chuẩn tương ứng trước khi xuất ERD vật lý hoàn chỉnh.