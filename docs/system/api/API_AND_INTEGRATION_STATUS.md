# API & Integration Status

## 1. Mục tiêu

Tài liệu phân biệt rõ API/integration **đã tồn tại trong source** và API **mới ở mức requirement/roadmap**.

## 2. Current implementation status

### Custom REST/HTTP API

**Status: Not implemented in current custom source baseline.**

Không có thư mục `addons/fnb_core/controllers/` trên `master` tại thời điểm nghiên cứu. Vì vậy chưa có custom endpoint nào được document như API thực tế.

Không được suy diễn standard Odoo RPC thành custom project API nếu source chưa định nghĩa contract riêng.

### Internal model API

Có các server-side model methods được custom module gọi từ UI/Odoo ORM:

| Model | Method | Purpose |
|---|---|---|
| `purchase.order` | `action_approve_fnb()` | approve PO cần phê duyệt |
| `purchase.order` | `action_open_rejection_wizard()` | mở rejection wizard |
| `purchase.order` | `action_reject_fnb(reason)` | từ chối PO với lý do |
| `purchase.order` | `button_confirm()` | chặn confirmation trước approval |
| `stock.picking` | `button_validate()` | kiểm tra lot/expiry khi incoming receipt |
| `stock.lot` | `create()` | derive expiration date khi đủ điều kiện |

Đây là **Odoo model methods**, không phải public HTTP API contract.

## 3. Planned API scope từ SRS/roadmap

Requirement traceability hiện có roadmap cho:

- Product API.
- Stock API.
- Sales Order API + idempotency.
- Webhook/retry/dead-letter.

Các phần này phải được đánh dấu `Planned` cho tới khi controller/service implementation và test evidence được merge.

## 4. Contract template cho API tương lai

Mỗi endpoint sau này phải document tối thiểu:

```text
Endpoint ID:
Method:
Path:
Authentication:
Authorization:
Company scope:
Rate limit expectation:
Idempotency:
Request headers:
Request schema:
Response schema:
Validation rules:
Error codes:
Audit/logging behavior:
Example request:
Example response:
Security considerations:
Tests/evidence:
```

## 5. Security requirements cho API tương lai

Theo Development Rules:

- không trust ID/company/domain/field name từ client;
- validate external input;
- enforce ACL, record rule và allowed companies;
- không log token/password/full request body/confidential data;
- controller phải khai báo auth, CSRF behavior, rate-limit expectation và company scope;
- không dùng `sudo()` để vượt quyền;
- mutation cần idempotency khi requirement yêu cầu.

## 6. Integration boundary hiện tại

```text
External Client
   |
   |  custom REST API: chưa có
   v
[Future integration layer]
   |
   v
Odoo ORM / business models
   |
   v
PostgreSQL
```

Hiện các business interaction được thực hiện qua standard Odoo Web/UI và ORM flow.

## 7. Documentation rule

Khi API được triển khai:

1. Update file này từ `Planned` → `Implemented`.
2. Thêm OpenAPI-like contract hoặc endpoint reference riêng.
3. Map endpoint vào SRS/RTM.
4. Link automated tests.
5. Thêm developer usage example.
6. Thêm operational/error-handling notes.

Không publish example endpoint giả trước khi implementation contract được duyệt.