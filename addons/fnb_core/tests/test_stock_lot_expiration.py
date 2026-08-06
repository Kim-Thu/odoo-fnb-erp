from datetime import timedelta

from odoo import fields
from odoo.tests.common import TransactionCase


class TestStockLotExpiration(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company_a = cls.env.company
        cls.company_b = cls.env["res.company"].create({"name": "T3004 Company B"})

    def _create_product(self, company, **values):
        defaults = {
            "name": "T3004 Product",
            "company_id": company.id,
            "tracking": "lot",
            "use_expiration_date": True,
            "fnb_requires_traceability": True,
            "fnb_shelf_life_days": 5,
        }
        defaults.update(values)
        return self.env["product.product"].create(defaults)

    def test_traceable_product_gets_default_expiration(self):
        product = self._create_product(self.company_a)
        before = fields.Datetime.now() + timedelta(days=5)

        lot = self.env["stock.lot"].create(
            {"name": "T3004-DEFAULT", "product_id": product.id}
        )

        after = fields.Datetime.now() + timedelta(days=5)
        self.assertGreaterEqual(lot.expiration_date, before)
        self.assertLessEqual(lot.expiration_date, after)

    def test_existing_expiration_is_preserved(self):
        product = self._create_product(self.company_a)
        expected = fields.Datetime.now() + timedelta(days=30)

        lot = self.env["stock.lot"].create(
            {
                "name": "T3004-EXISTING",
                "product_id": product.id,
                "expiration_date": expected,
            }
        )

        self.assertEqual(lot.expiration_date, expected)

    def test_zero_shelf_life_uses_standard_odoo_default(self):
        product = self._create_product(self.company_a, fnb_shelf_life_days=0)
        before = fields.Datetime.now()

        lot = self.env["stock.lot"].create(
            {"name": "T3004-ZERO", "product_id": product.id}
        )

        after = fields.Datetime.now()
        self.assertGreaterEqual(lot.expiration_date, before)
        self.assertLessEqual(lot.expiration_date, after)

    def test_untracked_product_does_not_set_expiration(self):
        product = self._create_product(
            self.company_a,
            tracking="none",
            use_expiration_date=False,
            fnb_requires_traceability=False,
        )

        lot = self.env["stock.lot"].create(
            {"name": "T3004-UNTRACKED", "product_id": product.id}
        )

        self.assertFalse(lot.expiration_date)

    def test_company_specific_shelf_life_is_used(self):
        product_a = self._create_product(self.company_a, fnb_shelf_life_days=3)
        product_b = self._create_product(self.company_b, fnb_shelf_life_days=9)
        now = fields.Datetime.now()

        lot_a = self.env["stock.lot"].create(
            {"name": "T3004-COMPANY-A", "product_id": product_a.id}
        )
        lot_b = self.env["stock.lot"].create(
            {"name": "T3004-COMPANY-B", "product_id": product_b.id}
        )

        self.assertLess(lot_a.expiration_date, now + timedelta(days=4))
        self.assertGreater(lot_b.expiration_date, now + timedelta(days=8))
