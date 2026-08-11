# Hướng dẫn import Product master

Tài liệu này mô tả cách chuẩn bị và import Product master cho dự án F&B theo hướng **Standard First**: ưu tiên cơ chế import chuẩn của Odoo, chỉ dùng các field custom đã có trong `fnb_core`.

## Phạm vi

T1010 chỉ bao phủ import Product master và field guide. UoM chi tiết thuộc T1101–T1103; partner master thuộc T1104–T1106; warehouse/location thuộc T1201–T1203.

Nguồn requirement: BR-01 / FR-MD-01 yêu cầu quản lý tập trung sản phẩm với SKU, loại/nhóm, UoM, tracking, hạn sử dụng, route/replenishment. Phần này tập trung vào các field Product master đã hiện hữu trong dự án.

## Template

Template synthetic đặt tại `docs/templates/product_import_template.csv`.

Header hiện dùng:

```text
name,default_code,fnb_internal_sku,fnb_ingredient_classification,fnb_storage_condition,fnb_shelf_life_days,fnb_requires_traceability
```

## Mapping field

| CSV column | Odoo field | Ý nghĩa | Quy tắc |
|---|---|---|---|
| `name` | `product.template.name` | Tên sản phẩm/nguyên vật liệu | Bắt buộc về mặt nghiệp vụ cho template |
| `default_code` | standard internal reference | Mã tham chiếu chuẩn Odoo | Có thể dùng song song với F&B SKU |
| `fnb_internal_sku` | `product.template.fnb_internal_sku` | SKU nội bộ F&B | Unique theo `company_id`; T1007/T1008 đã có test |
| `fnb_ingredient_classification` | custom Selection | Phân loại F&B | `raw`, `semi_finished`, `finished`, `packaging` |
| `fnb_storage_condition` | custom Selection | Điều kiện bảo quản | `ambient`, `chilled`, `frozen`; default là `ambient` |
| `fnb_shelf_life_days` | custom Integer | Shelf life theo ngày | Phải >= 0; T1009 đã có regression test |
| `fnb_requires_traceability` | custom Boolean | Yêu cầu lot + expiry traceability | Khi bật, business logic hiện tại yêu cầu lot tracking và expiration handling |

## Quy tắc dữ liệu

### SKU

- `fnb_internal_sku` là mã nghiệp vụ F&B.
- SKU phải unique trong cùng company.
- Cùng một SKU có thể tồn tại ở company khác nếu company scope khác nhau.
- Không dùng dữ liệu production hoặc SKU thật của doanh nghiệp trong demo.

### Classification

Các giá trị hợp lệ:

- `raw` — Raw Material.
- `semi_finished` — Semi-finished.
- `finished` — Finished Product.
- `packaging` — Packaging.

Không tự thêm selection value mới trong file import; thay đổi classification taxonomy là thay đổi model/scope khác.

### Storage condition

Các giá trị hợp lệ:

- `ambient`
- `chilled`
- `frozen`

### Shelf life

- Dùng số nguyên theo ngày.
- `0` hợp lệ nếu chưa có shelf life dương.
- Giá trị âm phải bị reject bởi constraint hiện có.

### Traceability

- `fnb_requires_traceability=true` dùng cho sản phẩm cần lot/expiry traceability.
- Logic hiện tại đồng bộ requirement này với `tracking = lot` và bật expiration handling.
- Không dùng template này để bỏ qua constraint tracking/expiry.

## Trình tự import khuyến nghị

1. Chuẩn hóa category/UoM cần dùng trước khi import dữ liệu production-like demo; phần UoM chi tiết sẽ được chốt trong T1101–T1103.
2. Copy `docs/templates/product_import_template.csv` thành file làm việc riêng.
3. Chỉ dùng synthetic data.
4. Kiểm tra SKU trùng trong cùng company.
5. Kiểm tra selection value đúng technical value ở bảng mapping.
6. Kiểm tra `fnb_shelf_life_days >= 0`.
7. Import bằng chức năng import chuẩn của Odoo.
8. Review các record lỗi; không chỉnh constraint/code chỉ để làm dữ liệu import đi qua.

## Ví dụ synthetic

```csv
name,default_code,fnb_internal_sku,fnb_ingredient_classification,fnb_storage_condition,fnb_shelf_life_days,fnb_requires_traceability
T1010 Fresh Milk,RM-MILK-001,FNB-RM-MILK-001,raw,chilled,7,true
T1010 Sugar,RM-SUGAR-001,FNB-RM-SUGAR-001,raw,ambient,365,false
T1010 Bottled Tea,FG-TEA-001,FNB-FG-TEA-001,finished,chilled,30,true
```

## Validation evidence liên quan

- T1007: reject cùng SKU trong cùng company.
- T1008: cho phép cùng SKU ở company khác nhau.
- T1009: reject shelf life âm.

## Không thuộc T1010

- Không định nghĩa conversion UoM.
- Không cấu hình route/reordering rule.
- Không tạo warehouse/location.
- Không custom import parser hoặc API import.
- Không thay đổi ACL/record rules.
