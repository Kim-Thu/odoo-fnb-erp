# SRS Implementation Baseline

## 1. Mục đích

Tài liệu này không thay thế `docs/SRS_Odoo_FnB_ERP.md`. Nó là lớp đối chiếu giữa yêu cầu SRS và phần mềm **đã được triển khai trên `master`** tại thời điểm nghiên cứu.

Quy ước:

- `Implemented` — có evidence trực tiếp trong source đã merge.
- `Partially Implemented` — có một phần hành vi nhưng chưa đủ requirement.
- `Planned` — có trong SRS/roadmap nhưng source hiện tại chưa chứng minh implementation.
- `Needs Runtime Verification` — source có nhưng cần kiểm chứng trên UI/runtime để mô tả chính xác thao tác người dùng.

## 2. System context hiện tại

Custom addon duy nhất được quan sát là `fnb_core`. Addon phụ thuộc:

- `base`
- `product`
- `stock`
- `product_expiry`
- `purchase`

Source hiện tại tập trung vào master data F&B, purchase approval và traceability foundation.

## 3. Functional requirements baseline

### FR-MD-01 — Product master

**Status: Implemented / partial coverage theo SRS tổng.**

Evidence custom hiện có:

- F&B Internal SKU.
- F&B classification.
- Storage condition.
- Shelf life days.
- Traceability flag.
- SKU unique theo company.
- Shelf life không âm.

UI hiện có tab `F&B Operations` trong Product Template form cho SKU, classification, storage condition và shelf life.

### FR-MD-02 — UoM

**Status: Standard Odoo + documented configuration/test evidence.**

Không thấy custom UoM model trong addon hiện tại. Thiết kế chủ trương dùng standard Odoo UoM và validation theo category.

### FR-MD-03 — Customer/Vendor master

**Status: Standard Odoo + documented configuration baseline.**

Không thấy custom `res.partner` model trong source hiện tại. Requirement được đáp ứng theo hướng Standard First và tài liệu import/configuration.

### FR-PUR-01 — RFQ/PO

**Status: Partially Implemented / standard Odoo foundation.**

Standard Purchase dependency đã có. Custom source hiện chưa thêm flow RFQ/PO riêng. Roadmap còn task manual RFQ → PO và partial receipt evidence.

### FR-PUR-02 — Purchase Approval

**Status: Implemented phần approval-by-value; còn gap requirement.**

Implemented:

- company-level monetary approval threshold;
- computed `approval_required`;
- approval states `not_required`, `pending`, `approved`, `rejected`;
- purchase approver group;
- approve/reject action;
- rejection reason validation;
- audit fields;
- protected direct write;
- commercial changes reset approval;
- block `button_confirm()` nếu PO cần approval mà chưa approved.

Gap:

- BRD nói approval theo giá trị hoặc nhóm hàng; source hiện chỉ chứng minh theo giá trị.
- Multi-company evidence vẫn còn roadmap.
- E2E evidence cho receipt sau approval cần hoàn thiện cùng procure-to-stock flow.

### FR-PUR-03 — Purchase Traceability

**Status: Planned / partial standard foundation.**

Source hiện có stock lot và receipt traceability guard, nhưng chưa đủ evidence cho PO ↔ receipt ↔ vendor bill ↔ lot theo requirement đầy đủ.

### FR-INV-01 — Warehouse structure

**Status: Implemented baseline.**

Repo có demo warehouse configuration Raw Materials / Production / Finished Goods và test internal transfer đã merge trước workstream tài liệu.

### FR-INV-02 — Lot và expiry

**Status: Partially Implemented.**

Implemented:

- product traceability configuration yêu cầu lot tracking và expiration;
- `stock.lot.create()` có thể tự tính expiration date từ shelf life;
- incoming receipt validation kiểm tra lot và expiration cho product cần traceability.

Chưa khẳng định hoàn tất FEFO hoặc tất cả rule expiry cho outbound vì cần source/task Phase 3 tương ứng.

### Các domain Phase 4 trở đi

Inventory count, reordering, barcode, MRP, Quality, Sales, POS, Accounting, generic approval/audit, API, Dashboard, UAT và release/hardening: **Planned**, trừ khi có source mới được merge sau baseline này.

## 4. Non-functional baseline

### Security

Đã quan sát:

- custom approval group;
- explicit authorization check bằng `has_group`;
- protected approval audit fields;
- không dùng `sudo()` trong flow đã nghiên cứu;
- Docker `no-new-privileges:true` cho db và odoo containers;
- repository có Gitleaks configuration.

### Deployment / Environment

Docker Compose hiện định nghĩa PostgreSQL 16 Alpine mặc định và Odoo 18.0 mặc định. Odoo chỉ bind host `127.0.0.1:${ODOO_PORT:-8069}`.

### Testing

Makefile có command compile, install module và automated Odoo test. CI workflow là source xác nhận cuối cho task merge.

## 5. Traceability rule

Mỗi requirement nên truy được theo chuỗi:

```text
BRD/SRS
  → MASTER_TASK_PLAN
  → implementation/configuration
  → automated test/evidence
  → technical documentation
  → user guide/UAT
```

Không chuyển requirement sang `Implemented` chỉ vì có mô tả trong SRS.