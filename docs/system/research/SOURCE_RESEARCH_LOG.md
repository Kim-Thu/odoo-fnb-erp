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

## 2026-08-12 — UI, runtime và developer baseline

### Nguồn đã đọc thêm

- `addons/fnb_core/views/product_template_views.xml`
- `addons/fnb_core/views/purchase_order_views.xml`
- `addons/fnb_core/views/purchase_rejection_wizard_views.xml`
- `addons/fnb_core/wizards/purchase_rejection_wizard.py`
- `Makefile`
- `docker-compose.yml`
- repository root/addon directory layout.

### Implemented — UI evidence

Product form kế thừa standard Product Template form và thêm tab `F&B Operations`. XML hiện hiển thị SKU, classification, storage condition và shelf life.

Purchase Order form kế thừa standard Purchase form và thêm `Approve F&B`, `Reject F&B`, block `F&B Approval`, approval state badge, approved-by/approved-at/rejection reason.

Purchase settings thêm `F&B ERP` → `Purchase Approval` → `Approval threshold`.

### Implemented — wizard evidence

`fnb.purchase.rejection.wizard` là TransientModel. Wizard tự kiểm group, trim rejection reason, yêu cầu tối thiểu 5 ký tự và gọi domain action `purchase_order_id.action_reject_fnb()`.

### Implemented — local runtime evidence từ repository configuration

Docker Compose baseline dùng PostgreSQL 16 Alpine và Odoo 18.0 mặc định, mount custom addons read-only, lấy DB/admin password từ environment và bật `no-new-privileges:true`.

Makefile cung cấp `up`, `down`, `logs`, `shell`, `db-shell`, `install-core`, `lint`, `test`.

### API conclusion

Không có `addons/fnb_core/controllers/` trên `master` tại baseline. Vì vậy custom REST API = `Not Implemented`; Product/Stock/Sales Order API và webhook trong roadmap không được document như endpoint hiện hữu.

### Tài liệu đã sinh từ evidence này

- `srs/SRS_IMPLEMENTATION_BASELINE.md`
- `sdd/SOFTWARE_DESIGN_DESCRIPTION.md`
- `api/API_AND_INTEGRATION_STATUS.md`
- `technical-guide/DEVELOPER_GUIDE.md`
- `user-guide/USER_GUIDE_INDEX.md`

## Nguồn cần đọc tiếp

1. `addons/fnb_core/data/warehouse_demo.xml`.
2. Toàn bộ `addons/fnb_core/tests/` để lập behavioral evidence matrix.
3. `security/ir.model.access.csv`.
4. Standard Odoo 18 Purchase/Stock/Product source tương ứng để hoàn thiện lifecycle/ERD.
5. Runtime UI để xác minh đường dẫn menu chính xác và bổ sung ảnh/hướng dẫn click-by-click.

## Quy tắc cập nhật log

Mỗi kết luận mới phải ghi nguồn file. Nếu kết luận dựa trên BRD/SRS nhưng chưa có code, đánh dấu `Requirement only`. Nếu dựa trên source đã merge, đánh dấu `Implemented`. Nếu cần kiểm chứng runtime/UI, đánh dấu `Needs runtime verification`.