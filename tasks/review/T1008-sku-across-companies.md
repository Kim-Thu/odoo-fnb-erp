# T1008 — Test same SKU across different companies

## Business goal

Verify that the F&B internal SKU uniqueness rule is scoped by company and does not block the same SKU in different companies.

## Technical scope

- Add one Odoo test to the existing product SKU uniqueness test module.
- Create two synthetic companies/products using the same `fnb_internal_sku`.
- Assert both records are created and belong to different companies.

## Security impact

- Test-only change with synthetic data.
- No `sudo()`.
- No raw SQL.
- No ACL or record-rule bypass.
- Multi-company behavior is explicitly covered.

## Files changed

- `addons/fnb_core/tests/test_product_sku_uniqueness.py`
- `MASTER_TASK_PLAN.md`
- `tasks/review/T1008-sku-across-companies.md`

## Test cases

- Same SKU in two different companies succeeds.
- Existing same-company duplicate rejection test remains unchanged.

## Definition of done

- CI static checks pass.
- Odoo module install/test jobs pass.
- PR contains only T1008 and task-status updates.
