# Tài liệu hệ thống F&B ERP

Thư mục này là bộ tài liệu kỹ thuật và hướng dẫn sử dụng được xây dựng từ source code, BRD, SRS và requirement traceability của repository.

## Nguyên tắc

- `BRD_Odoo_FnB_ERP.md` và `SRS_Odoo_FnB_ERP.md` mô tả yêu cầu gốc.
- Source code trên `master` mô tả hành vi đã triển khai thực tế.
- `REQUIREMENT_TRACEABILITY_MATRIX.md` dùng để nối requirement với task/evidence.
- Không mô tả một chức năng là đã có nếu source hiện tại chưa chứng minh được.
- Phần nào còn roadmap ghi rõ `Planned`; phần cần kiểm chứng UI/runtime ghi `Needs Runtime Verification`.

## Cấu trúc tài liệu

- `srs/` — SRS implementation baseline, đối chiếu requirement với trạng thái source thực tế.
- `sdd/` — Software Design Description: architecture, model, security, transaction, UI và deployment design.
- `architecture/` — kiến trúc module, dependency, extension points và technical decisions.
- `data-model/` — model, field, relationship, constraint và ownership.
- `data-flow/` — luồng dữ liệu nghiệp vụ/end-to-end.
- `api/` — trạng thái API/integration, contract template và security requirements.
- `technical-guide/` — hướng dẫn developer/maintainer.
- `user-guide/` — hướng dẫn người dùng theo nghiệp vụ.
- `research/` — ghi chép nghiên cứu source, gap và câu hỏi cần xác minh.

## Tài liệu chính hiện có

| Nhóm | File | Nội dung |
|---|---|---|
| SRS | `srs/SRS_IMPLEMENTATION_BASELINE.md` | trạng thái Implemented/Partial/Planned theo source |
| SDD | `sdd/SOFTWARE_DESIGN_DESCRIPTION.md` | thiết kế phần mềm hiện tại |
| Architecture | `architecture/SYSTEM_ARCHITECTURE.md` | architecture baseline |
| Data Model | `data-model/CURRENT_DATA_MODEL.md` | custom field/model/constraint hiện hữu |
| Data Flow | `data-flow/PURCHASE_APPROVAL_FLOW.md` | purchase approval flow |
| API | `api/API_AND_INTEGRATION_STATUS.md` | API hiện hữu và planned integration scope |
| Developer | `technical-guide/DEVELOPER_GUIDE.md` | setup, coding, security, testing, Git workflow |
| User | `user-guide/USER_GUIDE_INDEX.md` | mục lục và baseline thao tác người dùng |
| User | `user-guide/PURCHASE_APPROVAL.md` | hướng dẫn purchase approval |
| Research | `research/SOURCE_RESEARCH_LOG.md` | source evidence và gap log |

## Trạng thái nghiên cứu hiện tại

Module custom hiện tại là `fnb_core`, phụ thuộc `base`, `product`, `stock`, `product_expiry`, `purchase`. Source đã có extension cho Product, Purchase Order, Stock Lot và Stock Picking; purchase approval và F&B traceability là hai flow custom chính đang hiện hữu.

Không có custom `controllers/` trong baseline source hiện tại, nên chưa có custom REST API nào được coi là Implemented. API Product/Stock/Sales Order và webhook vẫn thuộc roadmap cho tới khi có controller/service/test evidence.

## Quy tắc cập nhật

Khi một feature mới merge, cần kiểm tra tối thiểu:

1. SRS implementation status có thay đổi không.
2. SDD/data model/data flow có thay đổi không.
3. API contract có thay đổi không.
4. Developer Guide có cần thêm extension/testing rule không.
5. User Guide có thao tác mới không.
6. RTM có đủ traceability requirement → task → test → docs không.

Tài liệu sẽ tiếp tục được mở rộng theo source thực tế và từng phase của `MASTER_TASK_PLAN.md`.