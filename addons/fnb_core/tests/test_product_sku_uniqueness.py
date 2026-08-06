from odoo.tests.common import TransactionCase
from psycopg2 import IntegrityError


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

    def test_same_sku_across_different_companies_is_allowed(self):
        company_b = self.env["res.company"].create({"name": "T1008 Company B"})
        sku = "T1008-SKU"

        product_a = self.env["product.template"].create(
            {
                "name": "T1008 Product A",
                "company_id": self.env.company.id,
                "fnb_internal_sku": sku,
            }
        )
        product_b = self.env["product.template"].create(
            {
                "name": "T1008 Product B",
                "company_id": company_b.id,
                "fnb_internal_sku": sku,
            }
        )

        self.assertEqual(product_a.fnb_internal_sku, product_b.fnb_internal_sku)
        self.assertNotEqual(product_a.company_id, product_b.company_id)
