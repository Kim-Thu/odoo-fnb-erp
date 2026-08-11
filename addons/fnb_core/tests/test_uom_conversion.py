from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestUomConversion(TransactionCase):
    def test_same_category_weight_conversion_is_valid(self):
        uom_kg = self.env.ref("uom.product_uom_kgm")
        uom_g = self.env.ref("uom.product_uom_gram")

        self.assertEqual(uom_kg.category_id, uom_g.category_id)
        self.assertAlmostEqual(uom_kg._compute_quantity(1.0, uom_g), 1000.0)
        self.assertAlmostEqual(uom_g._compute_quantity(1000.0, uom_kg), 1.0)

    def test_cross_category_conversion_is_rejected(self):
        uom_kg = self.env.ref("uom.product_uom_kgm")
        uom_unit = self.env.ref("uom.product_uom_unit")

        self.assertNotEqual(uom_kg.category_id, uom_unit.category_id)
        with self.assertRaises(UserError):
            uom_kg._compute_quantity(1.0, uom_unit)
