from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestProductShelfLife(TransactionCase):
    def test_negative_shelf_life_is_rejected(self):
        with self.assertRaisesRegex(ValidationError, "Shelf life cannot be negative"):
            self.env["product.template"].create(
                {
                    "name": "T1009 Negative Shelf Life",
                    "company_id": self.env.company.id,
                    "fnb_shelf_life_days": -1,
                }
            )
