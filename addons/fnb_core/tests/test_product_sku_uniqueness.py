from psycopg2 import IntegrityError

from odoo.tests.common import TransactionCase


class TestProductSkuUniqueness(TransactionCase):
    def test_same_sku_in_same_company_is_rejected(self):
        values = {
            "name": "T1007 Product A",
            "company_id": self.env.company.id,
            "fnb_internal_sku": "T1007-SKU",
        }
        self.env["product.template"].create(values)

        with self.assertRaises(IntegrityError), self.env.cr.savepoint():
            self.env["product.template"].create(
                {
                    **values,
                    "name": "T1007 Product B",
                }
            )
