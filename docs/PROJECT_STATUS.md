# Project Status

Tài liệu này là dashboard trạng thái ngắn gọn của dự án. Mục tiêu là để người đọc có thể biết ngay dự án đang ở phase nào, task nào đang active, còn thiếu gì và bước tiếp theo là gì mà không cần đọc toàn bộ `MASTER_TASK_PLAN.md`.

> Quy ước: `MASTER_TASK_PLAN.md` là nguồn sự thật cho backlog và dependency; `REQUIREMENT_TRACEABILITY_MATRIX.md` là nguồn đối chiếu BRD/SRS; `PROJECT_STATUS.md` là snapshot vận hành hiện tại. Khi có khác biệt, phải đối chiếu GitHub PR/CI và cập nhật lại ba tài liệu này cho khớp.

## Snapshot hiện tại

| Mục | Trạng thái |
|---|---|
| Phase đang active | Phase 0 — Nền tảng repository, CI/CD và security |
| Task đang active | T0016 — Thiết lập BRD/SRS project blueprint và phased roadmap |
| Branch | `docs/T0016-project-blueprint-20260811-0752` |
| PR | #21 — `docs(T0016): establish phased BRD SRS project blueprint` |
| PR state | Draft / review |
| CI gần nhất | Green: Branch name, Commit message, CI |
| Blocker hiện tại | Không có blocker kỹ thuật; cần hoàn tất T0016 và merge PR #21 |
| Business phase kế tiếp | Phase 1 — Master data và shared configuration |

## Tiến độ theo phase

Bảng dưới đây là dashboard định hướng. Số liệu chi tiết phải được cập nhật khi task chuyển trạng thái trong `MASTER_TASK_PLAN.md`.

| Phase | Trạng thái tổng | Ghi chú |
|---|---|---|
| Phase 0 — Repository / CI/CD / security | 🟡 Đang hoàn thiện | T0016 đang review; một số CI/security enhancement được phép `deferred` nếu không block nghiệp vụ |
| Phase 1 — Master data / shared configuration | 🔵 Đang mở đường | Product master T1001–T1008 đã done; còn T1009–T1010, T1101–T1106, T1201–T1203 |
| Phase 2 — Purchase / Procure-to-Stock | ⚪ Chưa active chính thức | Một số purchase approval task cũ đã done nhưng chưa chủ động tiếp tục phase này |
| Phase 3 — Inventory lot / expiry / FEFO | ⚪ Chưa active chính thức | Lot/expiry foundation đã có phần done; phần còn lại vẫn theo roadmap |
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

Sau khi T0016 merge, ưu tiên quay lại Phase 1 và khép master data trước khi chủ động mở Phase 2.

1. `T1009` — Test reject shelf-life âm.
2. `T1010` — Product import template và field guide.
3. `T1101` — Định nghĩa cấu hình UoM theo hướng Standard First.
4. `T1102` — Test UoM conversion hợp lệ trong cùng category.
5. `T1103` — Test UoM conversion sai giữa các category.
6. `T1104` — Định nghĩa customer/vendor master data.
7. `T1105` — Test demo vendor/customer master.
8. `T1106` — Partner import template và field guide.
9. `T1201` — Định nghĩa cấu trúc Raw Materials / Production / Finished Goods.
10. `T1202`–`T1203` — Demo warehouse/location và test internal transfer.

## Deferred / cố ý chưa làm

- Một số task CI/CD hoặc security hardening trong Phase 0 có thể ở trạng thái `deferred` nếu không ảnh hưởng trực tiếp đến business flow, test hiện tại hoặc an toàn tối thiểu.
- `deferred` không có nghĩa là `done`.
- Các task này phải quay lại trước Phase 13 hoặc sớm hơn nếu trở thành dependency/blocker.

## Kiểm soát bỏ sót requirement

Để tránh bỏ sót BRD/SRS:

- Mỗi requirement phải có mapping trong `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`.
- Requirement chỉ được xem là covered khi implementation/configuration, test và documentation evidence liên quan đã merge và CI xanh.
- Khi thêm hoặc thay đổi requirement, phải cập nhật cả roadmap và traceability matrix trước khi coi scope đã được kiểm soát.

## Quy tắc cập nhật trạng thái dự án

Mỗi PR làm thay đổi task hoặc requirement phải kiểm tra và cập nhật các file phù hợp:

1. `MASTER_TASK_PLAN.md` — task status, dependency, phase hoặc task mới.
2. `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` — coverage BRD/SRS nếu scope/coverage thay đổi.
3. `docs/PROJECT_STATUS.md` — phase active, task/PR hiện tại, blocker, deferred và next tasks.

Không bắt buộc sửa cả ba file nếu một PR không làm thay đổi dữ liệu tương ứng; nhưng trước khi merge phải xác nhận snapshot vẫn đúng.

## Checklist kiểm tra nhanh

- [ ] PR/task active trong file này khớp GitHub thực tế.
- [ ] `MASTER_TASK_PLAN.md` khớp trạng thái task thực tế.
- [ ] Không có hai task nghiệp vụ active chồng nhau ngoài dependency plan được phê duyệt.
- [ ] Không có requirement BRD/SRS chưa được map mà không có ghi chú rõ.
- [ ] Mọi task `deferred` đều không phải blocker hiện tại.
- [ ] Next task có dependency đã `done` hoặc thuộc trường hợp được phép tiếp tục theo quy tắc deferred.
- [ ] CI của task active đã được kiểm tra trước khi merge.

## Cách dùng

Khi cần biết dự án đang ở đâu, chỉ cần kiểm tra file này trước. Nếu cần xác minh sâu hơn:

- Xem `MASTER_TASK_PLAN.md` để biết toàn bộ task/dependency.
- Xem `docs/REQUIREMENT_TRACEABILITY_MATRIX.md` để biết BRD/SRS còn thiếu coverage nào.
- Xem GitHub PR/CI để xác nhận trạng thái thực tế mới nhất.
