# T1201 — Định nghĩa cấu trúc kho Raw Materials / Production / Finished Goods

## Metadata

- Type: `docs`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T0016
- Dependencies ready: yes — T0016 đã `done`
- Source requirements: BR-01 / FR-INV-01
- Branch: `docs/T1201-warehouse-structure-20260811-2333`

## Goal

Định nghĩa baseline warehouse/location Standard First để T1202 cấu hình demo và T1203 kiểm thử internal transfer.

## In scope

- Ba khu vực Raw Materials, Production, Finished Goods.
- Internal location semantics.
- Baseline transfer Raw Materials → Production → Finished Goods.
- Company/security expectations cho task implementation/test kế tiếp.

## Out of scope

- Demo runtime records; thuộc T1202.
- Automated internal-transfer test; thuộc T1203.
- Manufacturing dependency, work order, route hoặc procurement automation.

## Required evidence

- [x] Đối chiếu BR-01.
- [x] Đối chiếu FR-INV-01.
- [x] Standard First: dùng `stock.warehouse` / `stock.location` chuẩn.
- [x] Không architecture/package/business-flow change ngoài requirement.

## Security checklist

- [x] No secret, token, credential or production data.
- [x] No `sudo()`.
- [x] No raw SQL.
- [x] No ACL/record-rule changes.
- [x] Company scope được nêu rõ cho T1202/T1203.

## Definition of done

- [x] Warehouse structure guidance được thêm.
- [x] Master plan cập nhật T1106 `done`, T1201 `review`.
- [x] Project Status chuyển active task sang T1201.
- [x] RTM không đổi vì BR-01 / FR-INV-01 đã map T1201–T1203.
- [ ] CI passes.

## Evidence

- T1106/PR #29 merged green trước khi bắt đầu task.
- Pull request và CI: pending sau commit.
