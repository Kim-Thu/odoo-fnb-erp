# T1102 — Test UoM conversion hợp lệ trong cùng category

## Metadata

- Type: `test`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T1101
- Dependencies ready: yes — T1101/PR #24 đã merge và CI xanh
- Source requirements: BR-01 / FR-MD-02; SRS data-quality rule cho UoM
- Branch: `test/T1102-uom-valid-conversion-20260811-1809`

## Goal

Xác minh conversion chuẩn của Odoo hoạt động đúng khi hai UoM thuộc cùng category, dùng ví dụ Weight `kg ↔ g` theo tài liệu T1101.

## In scope

- Dùng UoM chuẩn `kg` và `g` của Odoo.
- Assert hai UoM cùng category.
- Assert `1 kg = 1000 g` và chiều ngược lại.

## Out of scope

- Cross-category rejection; thuộc T1103.
- Custom UoM model hoặc conversion engine.
- Packaging theo product/vendor.

## Implementation notes

- Dùng API chuẩn `_compute_quantity` của `uom.uom`.
- Không thêm business logic mới.
- Không dùng `sudo()` hoặc raw SQL.

## Required tests

- [x] Positive path: same-category conversion.
- [ ] Validation/error path: T1103.
- [x] Permission path: không áp dụng, chỉ đọc shared UoM chuẩn trong test.
- [x] Multi-company path: không áp dụng, UoM là shared configuration chuẩn.
- [x] Regression coverage cho requirement FR-MD-02.

## Security checklist

- [x] No secret, token, password or real personal data.
- [x] ACL reviewed — không thay đổi.
- [x] Record rules reviewed — không thay đổi.
- [x] Company scope — không có company-owned custom data.
- [x] Input validated — test dùng XML IDs chuẩn.
- [x] No unsafe `sudo()`.
- [x] No unsafe raw SQL.
- [x] Logs/errors không expose sensitive data.

## Definition of done

- [x] Code chỉ giới hạn trong task T1102.
- [ ] CI passes.
- [x] Task evidence ghi nhận bên dưới.
- [x] Task file ở `tasks/review/` trước khi mở PR.

## Evidence

- Commit: pending until commit creation.
- Pull request: pending until PR creation.
- CI run: pending.
- Test command: Odoo automated tests via repository CI.
- Dependency evidence: T1101/PR #24 merged with green CI.
- Review notes: chỉ thêm automated test cho conversion hợp lệ trong cùng category.
