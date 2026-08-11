| T1008 | test | Test cùng SKU ở các company khác nhau | T1006 | done |
| T1009 | test | Test reject shelf-life âm | T1005 | done |
| T1010 | docs | Thêm product import template và field guide | T1004 | done |

### UoM và partner master

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1101 | docs | Xác định cấu hình UoM theo hướng Standard First | T0016 | done |
| T1102 | test | Test UoM conversion hợp lệ trong cùng category | T1101 | done |
| T1103 | test | Test UoM conversion sai giữa các category | T1101 | done |
| T1104 | docs | Xác định cấu hình customer/vendor master data | T0016 | done |
| T1105 | test | Test demo setup cho vendor/customer master | T1104 | review |
| T1106 | docs | Thêm partner import template và field guide | T1104 | todo |

### Warehouse foundation

| ID | Type | Task | Depends on | Status |
|---|---|---|---|---|
| T1201 | docs | Xác định cấu trúc kho Raw Materials, Production, Finished Goods | T0016 | todo |
| T1202 | feat | Thêm demo configuration cho warehouse/location | T1201 | todo |
| T1203 | test | Test internal transfer giữa các location đã cấu hình | T1202 | todo |

## Phase 2 — Purchase và Procure-to-Stock

### Purchase approval