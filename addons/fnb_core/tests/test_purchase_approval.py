from odoo.exceptions import AccessError, ValidationError
from odoo.tests.common import TransactionCase


class TestPurchaseApproval(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.company.fnb_purchase_approval_limit = 1000.0

        cls.vendor = cls.env["res.partner"].create(
            {"name": "Demo Ingredient Supplier", "supplier_rank": 1}
        )
        cls.product = cls.env["product.product"].create(
            {
                "name": "Demo Ingredient",
                "purchase_ok": True,
                "standard_price": 1500.0,
            }
        )
        cls.order = cls.env["purchase.order"].create(
            {
                "partner_id": cls.vendor.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": cls.product.id,
                            "name": cls.product.name,
                            "product_qty": 1.0,
                            "product_uom": cls.product.uom_po_id.id,
                            "price_unit": 1500.0,
                            "date_planned": "2026-08-06 08:00:00",
                        },
                    )
                ],
            }
        )

        cls.approver = cls.env["res.users"].create(
            {
                "name": "Purchase Approver",
                "login": "purchase.approver@example.test",
                "email": "purchase.approver@example.test",
                "groups_id": [
                    (
                        6,
                        0,
                        [
                            cls.env.ref("base.group_user").id,
                            cls.env.ref("fnb_core.group_fnb_purchase_approver").id,
                        ],
                    )
                ],
            }
        )

    def test_confirmation_requires_approval(self):
        self.assertTrue(self.order.approval_required)
        self.assertEqual(self.order.approval_state, "pending")
        with self.assertRaises(ValidationError):
            self.order.button_confirm()

    def test_approver_can_approve_then_confirm(self):
        order = self.order.with_user(self.approver)
        order.action_approve_fnb()
        self.assertEqual(order.approval_state, "approved")
        self.assertEqual(order.approved_by_id, self.approver)
        order.button_confirm()
        self.assertEqual(order.state, "purchase")

    def test_direct_audit_field_write_is_blocked(self):
        with self.assertRaises(AccessError):
            self.order.write({"approved_by_id": self.env.user.id})

    def test_business_change_resets_existing_approval(self):
        order = self.order.with_user(self.approver)
        order.action_approve_fnb()
        order.write({"partner_ref": "Changed after approval"})
        self.assertEqual(order.approval_state, "approved")

        order.write(
            {
                "order_line": [
                    (
                        1,
                        order.order_line.id,
                        {"price_unit": 2000.0},
                    )
                ]
            }
        )
        self.assertFalse(order.approved_by_id)
        self.assertEqual(order.approval_state, "pending")
