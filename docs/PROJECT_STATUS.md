# Project Status

Tài liệu này là dashboard trạng thái ngắn gọn của dự án. Mục tiêu là để người đọc biết ngay dự án đang ở phase nào, task nào đang active, còn thiếu gì và bước tiếp theo là gì mà không cần đọc toàn bộ `MASTER_TASK_PLAN.md`.

> Quy ước: `MASTER_TASK_PLAN.md` là nguồn sự thật cho backlog và dependency; `REQUIREMENT_TRACEABILITY_MATRIX.md` là nguồn đối chiếu BRD/SRS; `PROJECT_STATUS.md` là snapshot vận hành hiện tại. Khi có khác biệt, phải đối chiếu GitHub PR/CI và cập nhật lại ba tài liệu này cho khớp.

## Snapshot hiện tại

| Mục | Trạng thái |
|---|---|
| Phase đang active | Phase 2 — Purchase và Procure-to-Stock |
| Task đang active | T2010 — Test luồng approval và confirmation |
| Branch | `test/T2010-approval-confirmation-20260812-0120` |
| PR | Chưa mở — sẽ mở sau commit |
| PR state | Chưa có |
| CI gần nhất | T2009/PR #33 green và đã merged |
| Blocker hiện tại | Không có |
| Business phase kế tiếp | Tiếp tục Phase 2 theo dependency |

## Tiến độ theo phase

| Phase | Trạng thái tổng | Ghi chú |
|---|---|---|
| Phase 0 — Repository / CI/CD / security | 🟡 Nền tảng đủ để tiếp tục nghiệp vụ | T0016 done; một số CI/security enhancement vẫn `deferred` |
| Phase 1 — Master data / shared configuration | ✅ Hoàn tất nghiệp vụ | Product, UoM, partner và warehouse foundation T1001–T1203 đã merge/CI xanh |
| Phase 2 — Purchase / Procure-to-Stock | 🔵 Đang triển khai | Purchase approval T2001–T2009 done; T2010 đang review; T2011–T2016 và T2101–T2106 còn todo |
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

Sau khi T2010 merge, chọn task Phase 2 nhỏ nhất có dependency đã `done`; hiện ứng viên kế tiếp là T2011.

## Deferred / cố ý chưa làm

- Một số task CI/CD hoặc security hardening trong Phase 0 ở trạng thái `deferred` vì chưa ảnh hưởng trực tiếp đến business flow hoặc test hiện tại.
- `deferred` không có nghĩa là `done`.
- Các task này phải quay lại trước Phase 13 hoặc sớm hơn nếu trở thành dependency/blocker.

## Kiểm soát bỏ sót requirement

- Mỗi requirement phải có mapping trong `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.
- Requirement chỉ được xem là covered khi implementation/configuration, test và documentation evidence liên quan đã merge và CI xanh.
- T2009 đã bổ sung permission evidence cho BR-02 / FR-PUR-02; mapping RTM vẫn T2001–T2016.
- T2010 bổ sung full-flow evidence pending → approval → confirmation cho BR-02 / FR-PUR-02; RTM mapping không đổi.

## Quy tắc cập nhật trạng thái dự án

Mỗi PR làm thay đổi task hoặc requirement phải kiểm tra và cập nhật các file phù hợp:

1. `MASTER_TASK_PLAN.md` — task status, dependency, phase hoặc task mới.
2. `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` — coverage BRD/SRS nếu scope/coverage thay đổi.
3. `docs/PROJECT_STATUS.md` — phase active, task/PR hiện tại, blocker, deferred và next tasks.

## Checklist kiểm tra nhanh

- [x] T2009/PR #33 đã merge và CI xanh.
- [x] Chỉ có một task nghiệp vụ active: T2010.
- [x] Dependency T2007 của T2010 đã `done`.
- [x] T2010 nằm trong mapping BR-02 / FR-PUR-02; RTM chưa cần đổi.
- [x] Các task `deferred` hiện không phải blocker.
- [ ] T2010 PR đã merge.
- [ ] T2010 CI đã xanh.
