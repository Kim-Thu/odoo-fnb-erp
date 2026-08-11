# Data Flow — Purchase Approval

## Requirement basis

BR-02 yêu cầu phê duyệt PO theo giá trị hoặc nhóm hàng. SRS FR-PUR-02 hiện mô tả PO từ ngưỡng A trở lên cần cấp duyệt bổ sung và không được receipt trước khi được duyệt.

Source hiện tại đã triển khai **approval theo ngưỡng giá trị**. Chưa có evidence trong source hiện tại cho approval theo nhóm hàng.

## Actors

- Purchase user / Purchase Manager.
- `Purchase Approver` (`fnb_core.group_fnb_purchase_approver`).
- Odoo Purchase Order model.

## Flow

```text
[User creates/edits RFQ]
          |
          v
[purchase.order amount_total]
          |
          v
[Compare company.fnb_purchase_approval_limit]
       /      \
      /        \
not required   required
    |             |
    v             v
not_required    pending
                  |
          +-------+-------+
          |               |
          v               v
       Approve          Reject
          |               |
          v               v
 approved_by_id       rejection_reason
 approved_at              |
          |               v
          v            rejected
       approved            |
          |                |
          +-------+--------+
                  |
          button_confirm()
                  |
        approved required?
           /           \
         yes/no       required but
          |           not approved
          v               |
 standard Odoo            v
 confirmation       ValidationError
```

## State derivation

`approval_required = bool(limit and amount_total >= limit)`.

- Không required → `not_required`.
- Required + `approved_by_id` → `approved`.
- Required + `rejection_reason` → `rejected`.
- Còn lại → `pending`.

## Approval write protection

`approved_by_id`, `approved_at`, `rejection_reason` không được direct write bình thường. Internal approve/reject/reset dùng context `fnb_approval_action=True`.

## Reset flow

Nếu PO đã approved/rejected và thay một trong các commercial fields:

- `partner_id`
- `currency_id`
- `company_id`
- `order_line`

thì audit approval được reset:

```text
approved/rejected PO
       |
commercial change
       |
       v
approved_by_id = False
approved_at    = False
rejection_reason = False
       |
       v
approval_state recomputed
```

## Gap cần theo dõi

- BRD nói approval theo giá trị **hoặc nhóm hàng**; source hiện chỉ chứng minh threshold theo amount.
- SRS nói không được receipt trước khi PO được duyệt; source hiện chặn `button_confirm()` trước approval, do đó receipt chuẩn phát sinh sau confirmation, nhưng cần E2E evidence riêng cho receipt guard/flow.
- Multi-company approval isolation vẫn cần test roadmap tương ứng.