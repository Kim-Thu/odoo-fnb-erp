# Tài liệu hệ thống F&B ERP

Thư mục này là bộ tài liệu kỹ thuật và hướng dẫn sử dụng được xây dựng từ source code, BRD, SRS và requirement traceability của repository.

## Nguyên tắc

- `BRD_Odoo_FnB_ERP.md` và `SRS_Odoo_FnB_ERP.md` mô tả yêu cầu.
- Source code trên `master` mô tả hành vi đã triển khai thực tế.
- `REQUIREMENT_TRACEABILITY_MATRIX.md` dùng để nối requirement với task/evidence.
- Không mô tả một chức năng là đã có nếu source hiện tại chưa chứng minh được.
- Phần nào còn roadmap sẽ ghi rõ `Planned`, không trộn với `Implemented`.

## Cấu trúc tài liệu

- `architecture/` — kiến trúc module, dependency, extension points và technical decisions.
- `data-model/` — model, field, relationship, constraint và ownership.
- `data-flow/` — luồng dữ liệu nghiệp vụ/end-to-end.
- `user-guide/` — hướng dẫn người dùng theo nghiệp vụ.
- `technical-guide/` — hướng dẫn developer/maintainer.
- `research/` — ghi chép nghiên cứu source, gap và câu hỏi cần xác minh.

## Trạng thái nghiên cứu ban đầu

Module custom hiện tại là `fnb_core`, phụ thuộc `base`, `product`, `stock`, `product_expiry`, `purchase`. Source đã có extension cho Product, Purchase Order, Stock Lot và Stock Picking; purchase approval và F&B traceability là hai flow custom chính đang hiện hữu.

Tài liệu sẽ được mở rộng theo source thực tế và theo từng phase của `MASTER_TASK_PLAN.md`.