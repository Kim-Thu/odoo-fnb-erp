# Developer Guide

## 1. Mục tiêu

Hướng dẫn developer đọc, chạy, sửa và kiểm thử repository hiện tại mà không phá business flow hoặc security model.

## 2. Runtime stack hiện tại

- Odoo 18.0.
- PostgreSQL 16 Alpine mặc định.
- Docker Compose.
- Custom addon: `addons/fnb_core`.

Module `fnb_core` phụ thuộc `base`, `product`, `stock`, `product_expiry`, `purchase`.

## 3. Cấu trúc repository cần biết

```text
addons/fnb_core/
├── __manifest__.py
├── data/
├── models/
├── security/
├── tests/
├── views/
└── wizards/

docs/
tasks/
.github/
Dockerfile
docker-compose.yml
Makefile
```

Không có custom `controllers/` trong baseline hiện tại.

## 4. Chạy môi trường local

Repository cung cấp Makefile dựa trên `.env`.

Các lệnh chính:

```bash
make up
make logs
make shell
make db-shell
make install-core
make test
make down
```

`make up` gọi Docker Compose với `.env`.

Các secret bắt buộc trong compose hiện tại gồm PostgreSQL password và Odoo admin password. Không commit `.env` thật.

Odoo được bind mặc định vào loopback host qua port 8069, không expose trực tiếp toàn mạng từ compose baseline.

## 5. Cài module

`make install-core` cài `fnb_core` vào database `fnb_dev` với `--stop-after-init`.

Khi thay manifest, model, XML hoặc security, developer phải xác nhận module install/upgrade vẫn thành công trước khi PR Ready.

## 6. Thêm hoặc sửa model

Nguyên tắc hiện tại:

- ưu tiên standard Odoo model;
- dùng `_inherit` khi business object đã tồn tại;
- không tạo model mới chỉ để copy behavior chuẩn;
- business validation đặt server-side;
- không dùng `sudo()` để chữa lỗi ACL;
- không dùng raw SQL nếu ORM xử lý được.

Ví dụ hiện tại:

```python
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
```

## 7. Field và constraint

Khi thêm field:

1. xác định ownership/company scope;
2. xác định readonly/copy/index/store;
3. thêm constraint nếu dữ liệu invalid có thể đi vào DB;
4. thêm security impact;
5. thêm positive/error/multi-company tests phù hợp.

SQL constraint chỉ dùng khi invariant phù hợp với database-level constraint. Business condition phức tạp dùng `@api.constrains` hoặc action validation.

## 8. View development

Current views kế thừa standard Odoo forms bằng XML `inherit_id` + `xpath`.

Không replace toàn bộ standard view nếu chỉ cần thêm field/button.

UI visibility không được xem là security enforcement. Nếu button bị giới hạn group, server method vẫn phải tự kiểm quyền khi action nhạy cảm.

## 9. Wizard development

Wizard dùng `models.TransientModel` cho interaction tạm thời.

Purchase rejection wizard hiện validate authorization và reason trước khi gọi domain action trên `purchase.order`.

Rule: business invariant quan trọng không được chỉ nằm trong wizard; model/action được gọi cuối cùng cũng phải tự bảo vệ.

## 10. Security development

Checklist bắt buộc:

- ACL/record rule có đúng actor không?
- company scope có bị lẫn không?
- server action có authorization check không?
- caller có thể direct write audit/protected field không?
- có `sudo()` không? nếu có phải giải trình và test.
- có raw SQL không? nếu có phải parameterized, documented và reviewed.
- có log secret/PII/business confidential data không?

Purchase approval hiện dùng custom approver group + `has_group()` server-side.

## 11. Automated tests

Development Rules yêu cầu tùy scope:

- positive path;
- validation failure;
- unauthorized-user path;
- multi-company path;
- regression test cho bug fix.

Business tests hiện dùng `TransactionCase`.

Chạy baseline:

```bash
make test
```

Makefile hiện chạy Odoo với `--test-enable` và install `fnb_core` vào `fnb_test`.

## 12. Static checks

Makefile `lint` hiện chạy:

```bash
python -m compileall addons
```

CI repository còn có các check khác như branch-name, commit-message và workflow tests. Developer phải lấy CI thực tế làm final evidence.

## 13. Git workflow

Canonical branch:

```text
<type>/T<4-digit-task-id>-<short-name>-<yyyyMMdd-HHmm>
```

Một task = một branch = một PR.

Không làm task khác trên branch đang review.

Commit phải có subject theo type/scope và body chứa Changes, Reason, Security, Tests, Rules checked theo `docs/DEVELOPMENT_RULES.md`.

## 14. Quy trình thêm feature

```text
Requirement
  ↓
RTM / Master Task
  ↓
Dependency check
  ↓
Branch
  ↓
Implementation
  ↓
Automated tests
  ↓
Documentation update
  ↓
PR
  ↓
CI
  ↓
Merge
```

## 15. Debugging

Ưu tiên:

- `make logs` để xem Odoo/Postgres logs;
- test nhỏ tái hiện behavior;
- đọc standard Odoo model trước khi override;
- kiểm tra context/user/company khi lỗi permission hoặc state.

Không sửa bằng `sudo()` hoặc bypass validation nếu chưa hiểu root cause.

## 16. Documentation responsibility

Mỗi behavior mới phải kiểm tra có cần cập nhật:

- SRS implementation baseline;
- SDD;
- data model;
- data flow;
- API contract;
- user guide;
- RTM;
- project status.

Tài liệu phải phân biệt `Implemented`, `Planned`, `Needs Runtime Verification`.