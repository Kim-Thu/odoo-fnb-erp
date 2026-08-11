# T2009 — Test unauthorized approval

## Metadata

- Type: `test`
- Epic: Phase 2 — Purchase và Procure-to-Stock
- Status: `review`
- Depends on: T2004
- Dependencies ready: yes — T2004 đã `done`
- Source requirements: BR-02 / FR-PUR-02; security role boundary for purchase approval
- Branch: `test/T2009-unauthorized-approval-20260812-0110`

## Goal

Bổ sung automated security evidence rằng user không thuộc purchase approver group không thể approve Purchase Order cần phê duyệt.

## In scope

- Dùng fixture Purchase Order hiện có với approval threshold.
- Dùng regular internal user không thuộc `group_fnb_purchase_approver`.
- Assert `action_approve_fnb()` raise `AccessError`.
- Assert audit fields và approval state không bị thay đổi sau attempt bị từ chối.

## Out of scope

- Thay đổi approval business logic.
- Rejection authorization; đã có regression coverage riêng.
- Multi-company approval scope; thuộc T2015.
- Approval reset/confirmation flow; thuộc T2010–T2012.

## Implementation notes

- Test-only change; không thêm model/field/group mới.
- Dùng standard Odoo `with_user()` để kiểm tra quyền thực tế.
- Không dùng `sudo()` hoặc raw SQL.

## Required tests

- [x] Unauthorized path: regular user không approve được.
- [x] State integrity: order vẫn `pending`, audit fields không bị ghi.
- [x] Positive approver path đã có regression test trong cùng test class.
- [x] Security group boundary được kiểm chứng trực tiếp.

## Security checklist

- [x] Synthetic users/data only.
- [x] No secret, token, password or production data.
- [x] No ACL/record-rule bypass.
- [x] No unsafe `sudo()`.
- [x] No raw SQL.
- [x] Không thay đổi architecture hoặc business flow.

## Definition of done

- [x] Scope chỉ thuộc T2009.
- [ ] CI passes.
- [x] Test evidence được thêm.
- [x] Task file ở `tasks/review/` trước khi mở PR.
