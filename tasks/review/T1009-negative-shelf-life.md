# T1009 — Test reject shelf-life âm

## Metadata

- Type: `test`
- Epic: `Phase 1 — Master data và shared configuration / Product master`
- Status: `review`
- Depends on: `T1005`
- Dependencies ready: `yes — T1005 is done on master`
- Source requirements: `MASTER_TASK_PLAN.md; BR-01 / FR-MD-01`
- Branch: `test/T1009-negative-shelf-life-20260811-0841`

## Goal

Xác minh constraint hiện có từ chối `fnb_shelf_life_days` âm bằng `ValidationError` với thông điệp nghiệp vụ mong đợi.

## In scope

- Thêm automated test cho giá trị shelf life âm.
- Đăng ký test module trong `addons/fnb_core/tests/__init__.py`.

## Out of scope

- Không thay đổi business logic hoặc constraint hiện có.
- Không thay đổi UI, import template hoặc API.

## Implementation notes

- Dùng `TransactionCase` theo test suite hiện tại.
- Test trực tiếp `product.template.create()` để bảo đảm ORM constraint được kích hoạt.
- Không dùng `sudo()` hoặc raw SQL.

## Required tests

- [x] Validation/error path: shelf life `-1` bị reject.
- [x] Regression test cho constraint T1005.
- [ ] Permission path, không áp dụng.
- [ ] Multi-company path, không áp dụng vì constraint không phụ thuộc company.

## Security checklist

- [x] Không có secret, token, password hoặc dữ liệu thật.
- [x] Không thay đổi ACL/record rules.
- [x] Không dùng `sudo()`.
- [x] Không dùng raw SQL.
- [x] Test data là synthetic.

## Definition of done

- [x] Thay đổi giới hạn trong T1009.
- [ ] CI pass.
- [x] Task evidence được ghi lại.
- [x] Task ở `tasks/review/` trước khi mở PR.

## Evidence

- Commit: pending
- Pull request: pending
- CI run: pending
- Test command: Odoo automated tests via CI
- Dependency evidence: T1005 is `done` in `MASTER_TASK_PLAN.md`
- Review notes: Test-only task; no runtime behavior change.
