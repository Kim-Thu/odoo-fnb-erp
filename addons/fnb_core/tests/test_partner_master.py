from odoo.tests.common import TransactionCase


class TestPartnerMaster(TransactionCase):
    def test_demo_customer_vendor_master_setup(self):
        customer = self.env["res.partner"].create(
            {
                "name": "Demo Customer T1105",
                "company_type": "company",
                "email": "customer.t1105@example.com",
                "phone": "+840000001105",
                "vat": "T1105-CUSTOMER-VAT",
                "street": "101 Demo Street",
                "city": "Ho Chi Minh City",
            }
        )
        vendor = self.env["res.partner"].create(
            {
                "name": "Demo Vendor T1105",
                "company_type": "company",
                "email": "vendor.t1105@example.com",
                "phone": "+840000001106",
                "vat": "T1105-VENDOR-VAT",
                "street": "202 Demo Street",
                "city": "Ho Chi Minh City",
            }
        )

        self.assertEqual(customer.name, "Demo Customer T1105")
        self.assertEqual(customer.company_type, "company")
        self.assertEqual(customer.vat, "T1105-CUSTOMER-VAT")
        self.assertEqual(customer.email, "customer.t1105@example.com")

        self.assertEqual(vendor.name, "Demo Vendor T1105")
        self.assertEqual(vendor.company_type, "company")
        self.assertEqual(vendor.vat, "T1105-VENDOR-VAT")
        self.assertEqual(vendor.email, "vendor.t1105@example.com")
