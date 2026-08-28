# Hướng dẫn sử dụng — Purchase Approval

> Tài liệu này chỉ mô tả chức năng đã có trong source hiện tại. Tên menu cụ thể có thể phụ thuộc view/menu chuẩn của Odoo Purchase.

## 1. Cấu hình ngưỡng duyệt

Hệ thống lưu ngưỡng tại company qua field `Purchase Approval Threshold` (`fnb_purchase_approval_limit`).

PO có `amount_total >= threshold` sẽ cần approval nếu threshold khác 0.

## 2. Nhận biết trạng thái

Purchase Order có các trạng thái approval:

- `Not Required` — không cần duyệt.
- `Pending Approval` — đang chờ duyệt.
- `Approved` — đã duyệt.
- `Rejected` — đã từ chối.

## 3. Duyệt PO

Người dùng phải thuộc group `Purchase Approver`.

Điều kiện:

- RFQ đang ở `draft` hoặc `sent`.
- PO thực sự thuộc diện cần approval.

Khi duyệt thành công, hệ thống ghi:

- `Approved By`.
- `Approved At`.
- xóa rejection reason cũ nếu có.

## 4. Từ chối PO

Purchase Approver có thể mở rejection wizard và nhập lý do.

Lý do sau khi trim phải có tối thiểu 5 ký tự. Khi từ chối, hệ thống xóa thông tin approval cũ và lưu `rejection_reason`.

## 5. Xác nhận PO

Nếu PO cần approval mà chưa ở trạng thái `approved`, hệ thống chặn confirmation.

PO không cần approval hoặc PO đã approved tiếp tục qua flow confirmation chuẩn của Odoo.

## 6. Khi thay đổi nội dung thương mại

Approval cũ không còn hiệu lực nếu thay:

- vendor;
- currency;
- company;
- order lines.

Sau thay đổi, người dùng phải kiểm tra trạng thái approval và thực hiện duyệt lại nếu PO vẫn vượt threshold.

## 7. Quyền và lỗi thường gặp

**Không có quyền approve/reject:** user chưa thuộc `Purchase Approver`.

**Only draft RFQs can be approved/rejected:** document không còn ở `draft`/`sent`.

**This purchase order does not require approval:** PO dưới threshold hoặc threshold chưa được cấu hình.

**This purchase order must be approved before confirmation:** PO cần approval nhưng chưa được duyệt.

## 8. Phạm vi chưa tài liệu hóa như chức năng hoàn chỉnh

- Approval theo nhóm hàng chưa thấy implementation evidence trong source hiện tại.
- Multi-company approval behavior đang còn test roadmap.
- Full RFQ → partial receipt → vendor bill sẽ có user guide riêng khi Phase 2 tương ứng hoàn tất.