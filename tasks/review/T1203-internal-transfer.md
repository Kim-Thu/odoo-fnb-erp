# T1203 — Test internal transfer giữa các location đã cấu hình

## Mục tiêu

Xác minh warehouse demo T1202 đáp ứng FR-INV-01 bằng một internal transfer thực tế từ Raw Materials sang Production, dùng standard Odoo stock models.

## Phạm vi

- Dùng ba warehouse demo `RM`, `PROD`, `FG` từ T1202.
- Xác minh `lot_stock_id` của từng warehouse là internal location.
- Tạo synthetic storable product trên company hiện hành.
- Tạo tồn demo tại Raw Materials bằng standard stock quant helper.
- Tạo và hoàn tất stock move từ Raw Materials sang Production.
- Xác minh số lượng nguồn giảm và đích tăng đúng.

## Requirement mapping

- BR-01 — Quản lý kho và vị trí kho.
- FR-INV-01 — Có ba khu vực Raw Materials / Production / Finished Goods và hỗ trợ transfer giữa location.

## Security

- Không dùng `sudo()`.
- Không raw SQL.
- Không ACL/record-rule bypass.
- Dữ liệu test hoàn toàn synthetic.
- Test chạy trong company hiện hành và kiểm tra warehouse demo cùng company.

## Test evidence

- `addons/fnb_core/tests/test_warehouse_internal_transfer.py`
- Scenario: 5 units ở RM, transfer 2 units sang PROD, kỳ vọng RM còn 3 và PROD có 2.

## Definition of done

- Test được register trong `addons/fnb_core/tests/__init__.py`.
- CI/Odoo automated tests xanh.
- T1202 được cập nhật `done`, T1203 chuyển `review`.
- Không thay đổi route, procurement rule, MRP flow hoặc business architecture.
