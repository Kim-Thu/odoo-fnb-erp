# T1103 — Test UoM conversion sai giữa các category

## Metadata

- Type: `test`
- Epic: `Phase 1 — Master data và shared configuration`
- Status: `review`
- Depends on: `T1101`
- Dependencies ready: `yes — T1101 merged and green`
- Source requirements: `BR-01 / FR-MD-02 / SRS data quality UoM same category`
- Branch: `test/T1103-uom-cross-category-20260811-2005`

## Goal

Xác minh Odoo chuẩn reject conversion giữa hai UoM thuộc category khác nhau, không cần custom validation engine.

## In scope

- Dùng UoM chuẩn `kg` và `Units` thuộc hai category khác nhau.
- Gọi standard `_compute_quantity` và xác minh `UserError` được raise.

## Out of scope

- Không thay đổi UoM configuration.
- Không custom conversion logic.
- Không xử lý packaging semantics.

## Required tests

- [x] Validation/error path cho cross-category conversion.
- [x] Positive path đã có ở T1102 và được giữ nguyên.
- [x] Permission path không áp dụng vì test dùng shared standard UoM config.
- [x] Multi-company path không áp dụng vì UoM chuẩn là shared configuration.

## Security checklist

- [x] No secret, token, password or real personal data.
- [x] ACL reviewed — no change.
- [x] Record rules reviewed — no change.
- [x] Company scope reviewed — not company-owned custom data.
- [x] Input validated by standard Odoo UoM category semantics.
- [x] No unsafe `sudo()`.
- [x] No unsafe raw SQL.
- [x] Logs and errors do not expose sensitive data.

## Definition of done

- [x] Code limited to T1103.
- [x] Regression/error-path test added.
- [x] Documentation/status updated.
- [x] Commit message uses repository validator format.
- [x] Task evidence recorded.
- [ ] CI green.

## Evidence

- Test: `test_cross_category_conversion_is_rejected`.
- Expected result: converting `kg` to `Units` via standard `_compute_quantity` raises `UserError` because categories differ.
- Dependency evidence: T1101 merged in PR #24; T1102 merged in PR #25.
- Security: test-only, no runtime/security changes.
