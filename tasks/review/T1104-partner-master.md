# T1104 — Customer/vendor master data

## Metadata

- Type: `docs`
- Epic: Phase 1 — Master data và shared configuration
- Status: `review`
- Depends on: T0016
- Dependencies ready: yes — T0016 đã merge
- Source requirements: BR-01 / FR-MD-03
- Branch: `docs/T1104-partner-master-20260811-2103`

## Goal

Xác định contract cấu hình customer/vendor master theo hướng Standard First để T1105 và T1106 triển khai/test trên cùng assumptions.

## In scope

- Standard `res.partner`.
- Customer/vendor role semantics.
- Payment terms, pricelist, VAT, billing information ở mức cấu hình contract.
- Multi-company/security notes.

## Out of scope

- Custom partner model/fields.
- Partner demo data test; thuộc T1105.
- Partner import template; thuộc T1106.
- Sales/POS/Accounting workflow runtime.

## Security checklist

- [x] No `sudo()`.
- [x] No raw SQL.
- [x] No ACL/record-rule changes.
- [x] No secrets or production data.
- [x] Company semantics documented rather than bypassed.

## Definition of done

- [x] Documentation aligned with BR-01 / FR-MD-03.
- [x] Standard First boundary explicit.
- [x] T1105/T1106 assumptions documented.
- [ ] CI passes.

## Evidence

- Commit: pending until commit creation.
- Pull request: pending until PR creation.
- CI: pending.
