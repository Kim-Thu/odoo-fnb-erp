# Source Research Log

## Mục tiêu

Theo dõi những gì đã đọc trực tiếp từ repository và những gì chưa đủ evidence, để tài liệu kỹ thuật không bị viết theo suy đoán.

## 2026-08-12 — Baseline

### Nguồn đã đối chiếu

- `docs/BRD_Odoo_FnB_ERP.md`
- `docs/SRS_Odoo_FnB_ERP.md`
- `docs/REQUIREMENT_TRACEABILITY_MATRIX.md`
- `MASTER_TASK_PLAN.md`
- `docs/DEVELOPMENT_RULES.md`
- `addons/fnb_core/__manifest__.py`
- `addons/fnb_core/models/product_template.py`
- `addons/fnb_core/models/purchase_order.py`
- `addons/fnb_core/models/stock_lot.py`
- `addons/fnb_core/models/stock_picking.py`
- `addons/fnb_core/security/fnb_security.xml`
- purchase approval automated tests hiện có.

### Kết luận chắc chắn từ source

1. Custom module hiện tại tập trung vào master data, purchase approval và traceability foundation.
2. Kiến trúc chủ đạo là extend standard Odoo models bằng `_inherit`.
3. Purchase approval threshold là company-specific.
4. Approval audit fields được bảo vệ khỏi direct write.
5. Commercial PO changes reset approval/rejection evidence.
6. Product traceability liên kết F&B product configuration với standard lot/expiration behavior.
7. Incoming receipt validation có custom guard cho lot và expiration.

### Gap giữa requirement và implementation cần tiếp tục nghiên cứu

- BRD: approval theo giá trị hoặc nhóm hàng; chưa thấy group/category-based approval implementation.
- FR-PUR-02: cần E2E evidence cho việc receipt không thể đi trước approval.
- FR-PUR-01: manual RFQ → PO và partial receipt còn roadmap.
- FR-PUR-03: PO ↔ receipt ↔ vendor bill/lot traceability còn roadmap.
- ERD vật lý đầy đủ cần nghiên cứu model chuẩn Odoo, không thể suy ra chỉ từ custom module.
- Menu/navigation thực tế cần đọc XML views/actions và kiểm chứng trên Odoo UI trước khi viết hướng dẫn click-by-click.

### Các nhóm source cần đọc tiếp

1. `addons/fnb_core/views/` — UI fields/buttons/settings.
2. `addons/fnb_core/wizards/` — rejection interaction.
3. `addons/fnb_core/data/warehouse_demo.xml` — warehouse/location baseline.
4. `addons/fnb_core/tests/` — behavioral evidence và edge cases.
5. Security access CSV — quyền wizard/model custom.
6. Standard Odoo 18 Purchase/Stock/Product source tương ứng — quan hệ chuẩn và lifecycle mà custom module kế thừa.

## Quy tắc cập nhật log

Mỗi kết luận mới phải ghi nguồn file. Nếu kết luận dựa trên BRD/SRS nhưng chưa có code, đánh dấu `Requirement only`. Nếu dựa trên source đã merge, đánh dấu `Implemented`. Nếu cần kiểm chứng runtime/UI, đánh dấu `Needs runtime verification`.