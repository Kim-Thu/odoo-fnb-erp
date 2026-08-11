# T1010 — Product import template và field guide

## Metadata

- Type: `docs`
- Epic: Phase 1 — Master data và shared configuration / Product master
- Status: `review`
- Depends on: `T1004`
- Dependencies ready: `yes` — T1004 đã `done` trong `MASTER_TASK_PLAN.md`
- Source requirements: `BR-01`, `FR-MD-01`, `SRS 4.2 Data quality rules`
- Branch: `docs/T1010-product-import-guide-20260811-1730`

## Goal

Tạo hướng dẫn import Product master và template CSV tối thiểu để dữ liệu F&B được nhập nhất quán với các field custom hiện có.

## In scope

- Tài liệu mapping field chuẩn Odoo và field F&B custom cần dùng khi import.
- Quy tắc dữ liệu cho SKU, shelf life, storage condition, classification và traceability.
- Template CSV synthetic có header và một số dòng mẫu.
- Cập nhật trạng thái roadmap/project dashboard cho T1010.

## Out of scope

- Không custom import engine của Odoo.
- Không thêm field/model mới.
- Không thay đổi UoM configuration; phần đó thuộc T1101–T1103.
- Không thêm partner/warehouse demo data.

## Implementation notes

- Ưu tiên import chuẩn của Odoo (Standard First).
- Giữ technical field names để dễ đối chiếu khi import.
- Không dùng dữ liệu thật.

## Required tests

- [x] Review header/template khớp field hiện có trong `product.template` extension.
- [x] Negative shelf-life rule đã có regression test tại T1009.
- [x] SKU uniqueness theo company đã có coverage T1007/T1008.
- [x] Không có permission/runtime behavior mới cần test.

## Security checklist

- [x] Không có secret, token, password hoặc dữ liệu cá nhân thật.
- [x] Không thay đổi ACL.
- [x] Không thay đổi record rule.
- [x] Company scope của SKU được nêu rõ trong hướng dẫn.
- [x] Không dùng `sudo()`.
- [x] Không dùng raw SQL.

## Definition of done

- [x] Scope chỉ giới hạn ở tài liệu/template của T1010.
- [x] Có product import field guide bằng tiếng Việt.
- [x] Có CSV template synthetic.
- [x] `MASTER_TASK_PLAN.md` chuyển T1009 `done`, T1010 `review`.
- [x] `PROJECT_STATUS.md` phản ánh T1010 đang review.
- [ ] CI xanh.
- [ ] PR merge.

## Evidence

- Commit: pending
- Pull request: pending
- CI run: pending
- Dependency evidence: T1004 `done`; T1009 PR #22 merged trước khi bắt đầu T1010.
- Notes: documentation-only task.
