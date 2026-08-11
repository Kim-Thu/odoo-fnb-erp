# Project Status

Tài liệu này là dashboard trạng thái ngắn gọn của dự án. Mục tiêu là để người đọc biết ngay dự án đang ở phase nào, task nào đang active, còn thiếu gì và bước tiếp theo là gì mà không cần đọc toàn bộ `MASTER_TASK_PLAN.md`.

> Quy ước: `MASTER_TASK_PLAN.md` là nguồn sự thật cho backlog và dependency; `REQUIREMENT_TRACEABILITY_MATRIX.md` là nguồn đối chiếu BRD/SRS; `PROJECT_STATUS.md` là snapshot vận hành hiện tại. Khi có khác biệt, phải đối chiếu GitHub PR/CI và cập nhật lại ba tài liệu này cho khớp.

## Snapshot hiện tại

| Mục | Trạng thái |
|---|---|
| Phase đang active | Phase 1 — Master data và shared configuration |
| Task đang active | T1009 — Test reject shelf-life âm |
| Branch | `test/T1009-negative-shelf-life-20260811-0841` |
| PR | Chưa mở — sẽ mở sau khi commit hoàn tất |
| PR state | Chưa có |
| CI gần nhất | T0016/PR #21 đã green và merged |
| Blocker hiện tại | Không có |
| Business phase kế tiếp | Tiếp tục khép Phase 1 |

## Tiến độ theo phase

| Phase | Trạng thái tổng | Ghi chú |
|---|---|---|
| Phase 0 — Repository / CI/CD / security | 🟡 Nền tảng đủ để tiếp tục nghiệp vụ | T0016 done; một số CI/security enhancement vẫn `deferred` |
| Phase 1 — Master data / shared configuration | 🔵 Đang triển khai | Product master T1001–T1008 done; T1009 đang review sau implementation; còn T1010, T1101–T1106, T1201–T1203 |
| Phase 2 — Purchase / Procure-to-Stock | ⚪ Chưa active chính thức | Một số purchase approval task cũ đã done |
| Phase 3 — Inventory lot / expiry / FEFO | ⚪ Chưa active chính thức | Lot/expiry foundation đã có phần done |
| Phase 4 — Inventory operations | ⚪ Chưa active | Inventory count, reordering, barcode |
| Phase 5 — Manufacturing | ⚪ Chưa active | BOM, MO, work order, costing |
| Phase 6 — Quality | ⚪ Chưa active | QCP, alert, corrective action |
| Phase 7 — Sales / returns | ⚪ Chưa active | Quotation, SO, delivery, return, quarantine |
| Phase 8 — POS / accounting basic | ⚪ Chưa active | POS session/order/return và invoice/payment baseline |
| Phase 9 — Approval / audit | ⚪ Chưa active | Generic approval và business audit |
| Phase 10 — API / integration | ⚪ Chưa active | Product/Stock/Sales Order API, idempotency, webhook/retry |
| Phase 11 — Dashboard / analytics | ⚪ Chưa active | KPI nghiệp vụ và company isolation |
| Phase 12 — Demo data / E2E / UAT | ⚪ Chưa active | Synthetic data, acceptance flow, UAT |
| Phase 13 — Hardening / release | ⚪ Chưa active | Security review, staging, backup/restore, release evidence |

## Task tiếp theo dự kiến

Sau khi T1009 merge, tiếp tục Phase 1:

1. `T1010` — Product import template và field guide.
2. `T1101` — Định nghĩa cấu hình UoM theo hướng Standard First.
3. `T1102` — Test UoM conversion hợp lệ trong cùng category.
4. `T1103` — Test UoM conversion sai giữa các category.
5. `T1104` — Định nghĩa customer/vendor master data.
6. `T1105` — Test demo vendor/customer master.
7. `T1106` — Partner import template và field guide.
8. `T1201` — Định nghĩa cấu trúc Raw Materials / Production / Finished Goods.
9. `T1202`–`T1203` — Demo warehouse/location và test internal transfer.

## Deferred / cố ý chưa làm

- Một số task CI/CD hoặc security hardening trong Phase 0 ở trạng thái `deferred` vì chưa ảnh hưởng trực tiếp đến business flow hoặc test hiện tại.
- `deferred` không có nghĩa là `done`.
- Các task này phải quay lại trước Phase 13 hoặc sớm hơn nếu trở thành dependency/blocker.

## Kiểm soát bỏ sót requirement

- Mỗi requirement phải có mapping trong `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.
- Requirement chỉ được xem là covered khi implementation/configuration, test và documentation evidence liên quan đã merge và CI xanh.
- Khi thêm hoặc thay đổi requirement, phải cập nhật cả roadmap và traceability matrix trước khi coi scope đã được kiểm soát.

## Quy tắc cập nhật trạng thái dự án

Mỗi PR làm thay đổi task hoặc requirement phải kiểm tra và cập nhật các file phù hợp:

1. `MASTER_TASK_PLAN.md` — task status, dependency, phase hoặc task mới.
2. `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` — coverage BRD/SRS nếu scope/coverage thay đổi.
3. `docs/PROJECT_STATUS.md` — phase active, task/PR hiện tại, blocker, deferred và next tasks.

## Checklist kiểm tra nhanh

- [x] T0016/PR #21 đã merge và CI xanh.
- [x] Chỉ có một task nghiệp vụ active: T1009.
- [x] Dependency T1005 của T1009 đã `done`.
- [x] T1009 không thay đổi coverage mapping BRD/SRS nên traceability matrix chưa cần sửa.
- [x] Các task `deferred` hiện không phải blocker.
- [ ] T1009 PR đã merge.
- [ ] T1009 CI đã xanh.
