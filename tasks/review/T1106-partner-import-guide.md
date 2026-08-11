# T1106 — Partner import template và field guide

## Metadata

- Type: `docs`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T1104
- Dependencies ready: yes — T1104/PR #27 đã merge và CI xanh
- Source requirements: BR-01 / FR-MD-03
- Branch: `docs/T1106-partner-import-guide-20260811-2301`

## Goal

Thêm template import và field guide cho customer/vendor master theo contract T1104, dùng standard `res.partner` và synthetic data.

## In scope

- Tài liệu import partner master.
- CSV template synthetic cho các field baseline Phase 1.
- Mapping rõ BR-01 / FR-MD-03.
- Ghi rõ field module-dependent như payment terms/pricelist chỉ áp dụng khi dependency tương ứng active.

## Out of scope

- Custom partner field/model.
- Runtime demo data mới.
- Sales/Accounting/Purchase dependency mới chỉ để expose field import.
- Thay đổi ACL/record rule.

## Security checklist

- [x] Synthetic data only.
- [x] No secret, token, password or real personal data.
- [x] No `sudo()`.
- [x] No raw SQL.
- [x] No ACL/record-rule bypass.
- [x] No architecture or business-flow change.

## Definition of done

- [x] Có partner import guide.
- [x] Có CSV template synthetic.
- [x] MASTER_TASK_PLAN cập nhật T1105 `done`, T1106 `review`.
- [x] PROJECT_STATUS cập nhật active T1106.
- [x] RTM không đổi vì coverage đã map T1104-T1106.
- [ ] CI passes.

## Evidence

- Dependency: T1104/PR #27 merged green.
- Prior test evidence: T1105/PR #28 merged green.
- PR: pending until creation.
- CI: pending.
