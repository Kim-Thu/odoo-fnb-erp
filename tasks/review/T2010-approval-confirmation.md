# T2010 — Test luồng approval và confirmation

## Metadata

- Type: `test`
- Epic: Phase 2 — Purchase và Procure-to-Stock
- Status: `review`
- Depends on: T2007
- Dependencies ready: yes — T2007 đã `done`
- Source requirements: BR-02 / FR-PUR-02
- Branch: `test/T2010-approval-confirmation-20260812-0120`

## Goal

Bổ sung automated evidence cho luồng đầy đủ PO cần approval: pending → chặn confirm → approver approve → confirm thành Purchase Order.

## In scope

- Tạo synthetic Purchase Order vượt approval threshold.
- Assert order bắt đầu ở `pending` và không confirm được trước approval.
- Approver thực hiện `action_approve_fnb()`.
- Assert audit evidence `approved_by_id` và `approved_at` được ghi.
- Confirm order sau approval và assert state `purchase`.

## Out of scope

- Unauthorized approval — T2009.
- Reset approval sau business change — T2011/T2012.
- Rejection validation/confirmation — T2013/T2014.
- Multi-company approval scope — T2015.

## Security

- Synthetic data only.
- No `sudo()`.
- No raw SQL.
- No ACL/record-rule bypass.
- Không thay đổi approval business logic hoặc architecture.

## Definition of done

- [x] Scope chỉ thuộc T2010.
- [x] Test pending/blocked/approved/confirmed flow được thêm.
- [x] Audit fields được assert.
- [ ] CI passes.
