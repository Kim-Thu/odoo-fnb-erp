# Software Design Description (SDD)

## 1. Mục tiêu

Tài liệu mô tả thiết kế phần mềm quan sát được từ source hiện tại của repository. Nội dung Planned được tách rõ khỏi thiết kế đã triển khai.

## 2. Kiến trúc tổng quan

Hệ thống hiện dùng Odoo 18 làm application platform và PostgreSQL làm database. Custom business logic nằm trong addon `fnb_core`.

```text
Browser / Odoo Web Client
          |
          v
     Odoo 18 Server
          |
          +------------------------------+
          | standard modules             |
          | base/product/stock/purchase  |
          | product_expiry               |
          +------------------------------+
          |
          v
       fnb_core
          |
          +-- model extensions
          +-- views
          +-- security
          +-- wizard
          +-- demo data
          +-- automated tests
          |
          v
      PostgreSQL
```

Không thấy custom HTTP controller trong source hiện tại, nên chưa có custom REST layer được xem là Implemented.

## 3. Module design

### 3.1 Product domain

`product.template` được mở rộng thay vì tạo F&B product model riêng.

Responsibilities:

- lưu metadata F&B;
- validate shelf life;
- enforce SKU uniqueness per company;
- đồng bộ traceability flag với standard lot/expiration configuration.

Design decision: reuse standard Product lifecycle và stock integration của Odoo.

### 3.2 Purchase approval domain

`purchase.order` được mở rộng bằng computed approval state và audit fields.

State model:

```text
             amount < threshold
draft RFQ ------------------------> not_required
   |
   | amount >= threshold
   v
 pending
  /   \
 /     \
approve reject
 |       |
 v       v
approved rejected
```

`button_confirm()` là enforcement point: PO cần approval chỉ được đi tiếp khi state = `approved`.

Approval state không được set trực tiếp; state được compute từ threshold + audit fields.

### 3.3 Rejection wizard

Transient model `fnb.purchase.rejection.wizard` chịu trách nhiệm interaction nhập reason.

Validation được đặt cả ở wizard và domain action `purchase.order.action_reject_fnb()`, giúp model action vẫn tự bảo vệ nếu được gọi ngoài UI wizard.

### 3.4 Traceability domain

`product.template` định nghĩa business configuration.

`stock.lot` dùng shelf-life configuration để derive expiration date khi tạo lot nếu caller chưa truyền ngày hết hạn.

`stock.picking.button_validate()` kiểm tra incoming stock line của product traceable phải có lot và expiration date.

## 4. Security design

### 4.1 Authorization

Custom role:

`fnb_core.group_fnb_purchase_approver`

Role này imply standard `purchase.group_purchase_manager`.

Approve/reject actions kiểm tra `has_group()` tại server-side; UI group restriction chỉ là lớp hiển thị bổ sung, không phải enforcement duy nhất.

### 4.2 Audit-field protection

Protected fields:

- `approved_by_id`
- `approved_at`
- `rejection_reason`

Direct `write()` bị từ chối trừ khi internal context chứa `fnb_approval_action=True`.

### 4.3 Reset integrity

Nếu approval/rejection đã có và commercial data thay đổi, server reset audit evidence trước khi lưu commercial change.

Commercial basis hiện gồm:

- `partner_id`
- `currency_id`
- `company_id`
- `order_line`

## 5. UI design

### Product

Product Template form kế thừa standard form và thêm tab `F&B Operations`.

### Purchase

Purchase Order form thêm:

- `Approve F&B` button;
- `Reject F&B` button;
- approval badge;
- approver;
- approval timestamp;
- rejection reason.

Settings form thêm app/block `F&B ERP` → `Purchase Approval` → `Approval threshold`.

## 6. Persistence design

Custom source chủ yếu thêm field vào bảng chuẩn Odoo thông qua `_inherit`.

Không có custom persistent model mới trong phần đã nghiên cứu ngoài field mở rộng. `fnb.purchase.rejection.wizard` là TransientModel.

Database physical schema đầy đủ phụ thuộc ORM mapping của Odoo chuẩn; không suy đoán tên/index ngoài những constraint khai báo trực tiếp.

## 7. Error handling

Domain validation sử dụng `ValidationError` cho business invalid state và `AccessError` cho authorization/direct-write violation.

Các lỗi hiện có bao gồm:

- user không được approve/reject;
- audit fields không được sửa trực tiếp;
- chỉ draft/sent RFQ được approve/reject;
- PO không thuộc diện approval;
- rejection reason quá ngắn;
- PO cần approval nhưng chưa approved;
- shelf life âm;
- traceability configuration không hợp lệ;
- receipt thiếu lot/expiration.

## 8. Transaction boundary

Các action chạy trong transaction ORM chuẩn của Odoo. Source nghiên cứu không dùng raw SQL hoặc manual transaction management.

## 9. Deployment design

Docker Compose:

- `db`: PostgreSQL 16 Alpine mặc định;
- `odoo`: Odoo 18.0 mặc định;
- custom addons mount read-only tại `/mnt/extra-addons`;
- DB password và Odoo admin password bắt buộc qua environment;
- `no-new-privileges:true` được bật cho container.

## 10. Testing design

Repository dùng Odoo `TransactionCase` cho business tests đã nghiên cứu. Makefile hỗ trợ module install và `--test-enable`.

Testing principle hiện có trong Development Rules:

- positive path;
- validation failure;
- unauthorized path;
- multi-company path khi liên quan;
- regression test cho bug fix.

## 11. Planned design areas

Chưa được xem là implemented design:

- custom API/controller layer;
- MRP extensions;
- Quality extensions;
- Sales/POS custom flow;
- generic audit subsystem;
- dashboards;
- webhook/retry/dead-letter;
- complete deployment/release architecture.

Các phần này chỉ nên đưa vào SDD chi tiết sau khi source hoặc approved design task tồn tại.