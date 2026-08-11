# T1202 — Demo configuration cho warehouse/location

## Metadata

- Type: `feat`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T1201
- Dependencies ready: yes — T1201/PR #30 đã merge và CI xanh
- Source requirements: BR-01 / FR-INV-01
- Branch: `feat/T1202-warehouse-demo-20260811-2340`

## Goal

Tạo demo configuration tối thiểu bằng model chuẩn `stock.warehouse` để biểu diễn ba khu vực Raw Materials, Production và Finished Goods theo baseline T1201.

## In scope

- Tạo ba warehouse demo bằng standard Odoo data XML.
- Dùng code ổn định `RM`, `PROD`, `FG`.
- Gắn warehouse vào company demo hiện hành.
- Đăng ký data file trong manifest.

## Out of scope

- Custom warehouse/location model.
- Route, procurement rule, MRP flow hoặc automation.
- Automated internal-transfer test; thuộc T1203.

## Security

- Standard Odoo records only.
- Không `sudo()`.
- Không raw SQL.
- Không ACL/record-rule changes.
- Không secret hoặc production data.

## Test evidence

- CI phải xác minh manifest/XML/module install/upgrade và các automated test hiện hữu.
- T1203 sẽ xác minh internal transfer giữa các warehouse/location đã tạo.

## Definition of done

- [x] Scope chỉ giới hạn T1202.
- [x] Demo records dùng standard `stock.warehouse`.
- [x] Manifest load data file.
- [ ] CI passes.
- [x] Task file ở `tasks/review/` trước khi mở PR.
