# T1105 — Test demo setup cho vendor/customer master

## Metadata

- Type: `test`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T1104
- Dependencies ready: yes — T1104/PR #27 đã merge và CI xanh
- Source requirements: BR-01 / FR-MD-03
- Branch: `test/T1105-partner-demo-20260811-2141`

## Goal

Xác minh có thể tạo synthetic customer/vendor master bằng model chuẩn `res.partner` theo contract T1104, không cần custom partner model hoặc bypass security.

## In scope

- Tạo một customer demo và một vendor demo bằng `res.partner`.
- Dùng dữ liệu synthetic: name, company type, email, phone, VAT, street, city.
- Assert các field master-data cơ bản được lưu đúng.

## Out of scope

- Custom `is_customer` / `is_vendor` boolean.
- Payment term, pricelist hoặc accounting-specific field chưa cần ở Phase 1.
- Partner import template; thuộc T1106.

## Security checklist

- [x] No `sudo()`.
- [x] No raw SQL.
- [x] No ACL/record-rule change or bypass.
- [x] Synthetic data only.
- [x] No secrets or production contact data.

## Required tests

- [x] Positive path: create synthetic customer/vendor partner records.
- [x] Validation/error path: không thêm validation custom trong task này.
- [x] Permission path: dùng standard test transaction/user context, không bypass quyền.
- [x] Multi-company path: không áp dụng custom company-owned model; partner semantics giữ nguyên standard Odoo.

## Definition of done

- [x] Test nằm trong `addons/fnb_core/tests`.
- [x] Test module được register trong `tests/__init__.py`.
- [x] Scope chỉ giới hạn T1105.
- [ ] CI passes.
- [x] Task evidence sẵn sàng cho PR.

## Evidence

- Commit: pending until commit creation.
- Pull request: pending until PR creation.
- CI run: pending.
- Test command: Odoo automated tests via repository CI.
- Dependency evidence: T1104/PR #27 merged with green CI.
