# T1101 — Xác định cấu hình UoM theo hướng Standard First

## Metadata

- Type: `docs`
- Epic: `Phase 1 — Master data và shared configuration`
- Status: `review`
- Depends on: `T0016`
- Dependencies ready: `yes` — T0016 đã merge vào `master`
- Source requirements: `BR-01`, `FR-MD-02`, SRS Data Quality
- Branch: `docs/T1101-uom-standard-first-20260811-1742`

## Goal

Xác định cấu hình UoM chuẩn của Odoo cho nghiệp vụ F&B và ranh giới khi nào dùng UoM conversion, khi nào dùng packaging.

## In scope

- Tài liệu hóa `uom.category` và `uom.uom` theo Standard First.
- Quy tắc conversion trong cùng category.
- Ví dụ kg ↔ g.
- Làm rõ giới hạn thùng ↔ chai.

## Out of scope

- Không thêm custom model hay conversion engine.
- Không thêm automated test; thuộc T1102/T1103.
- Không thêm partner hoặc warehouse config.

## Implementation notes

- Ưu tiên hành vi chuẩn Odoo.
- Không dùng `sudo()`.
- Không dùng raw SQL.

## Required tests

- [x] Documentation consistency với BRD/SRS.
- [x] Validation/error path được mô tả cho cross-category conversion.
- [x] Permission path không áp dụng vì không thay đổi quyền.
- [x] Multi-company path không áp dụng vì không thêm company-owned data.

## Security checklist

- [x] No secret, token, password or real personal data.
- [x] ACL reviewed — no changes.
- [x] Record rules reviewed — no changes.
- [x] Company scope reviewed — shared standard configuration only.
- [x] Input validation semantics documented.
- [x] No unsafe `sudo()`.
- [x] No unsafe raw SQL.
- [x] No sensitive logging.

## Definition of done

- [x] Scope chỉ thuộc T1101.
- [x] Tài liệu UoM Standard First được thêm.
- [x] MASTER_TASK_PLAN và PROJECT_STATUS được cập nhật.
- [x] Task record đặt trong `tasks/review/`.
- [ ] CI passes.

## Evidence

- Pull request: sẽ mở sau commit.
- Tests: documentation-only; CI repository checks.
- Dependency evidence: T0016 đã merge trong PR #21.
