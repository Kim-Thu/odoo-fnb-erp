# T2011 — Test reset approval sau khi đổi vendor

## Metadata

- Type: `test`
- Epic: Phase 2 — Purchase và Procure-to-Stock
- Status: `review`
- Depends on: T2006
- Dependencies ready: yes — T2006 đã `done`
- Source requirements: BR-02 / FR-PUR-02
- Branch: `test/T2011-reset-vendor-20260812-0130`

## Goal

Bổ sung automated evidence rằng Purchase Order đã được approve phải mất approval khi vendor thay đổi, vì vendor là commercial field thuộc approval basis.

## In scope

- Dùng Purchase Order vượt approval threshold.
- Approver thực hiện approval trước khi thay vendor.
- Thay `partner_id` sang synthetic vendor khác.
- Assert vendor mới được lưu.
- Assert `approved_by_id` và `approved_at` được reset.
- Assert order trở lại `pending`.

## Out of scope

- Reset approval sau khi đổi order line — T2012.
- Rejection reason validation — T2013.
- Rejected order confirmation — T2014.
- Multi-company approval scope — T2015.
- Thay đổi approval business logic.

## Security

- Synthetic partner data only.
- No `sudo()`.
- No raw SQL.
- No ACL/record-rule bypass.
- Không thay đổi architecture hoặc business flow.

## Definition of done

- [x] Scope chỉ thuộc T2011.
- [x] Vendor change reset test được thêm.
- [x] Audit fields và pending state được assert.
- [ ] CI passes.
