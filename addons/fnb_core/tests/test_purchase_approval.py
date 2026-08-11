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
        cls.regular_user = cls.env["res.users"].create(
            {
                "name": "Regular Purchase User",
                "login": "purchase.user@example.test",
                "email": "purchase.user@example.test",
                "groups_id": [(6, 0, [cls.env.ref("base.group_user").id])],
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

    def test_approval_confirmation_full_flow(self):
        order = self.env["purchase.order"].create(
            {
                "partner_id": self.vendor.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": self.product.id,
                            "name": self.product.name,
                            "product_qty": 2.0,
                            "product_uom": self.product.uom_po_id.id,
                            "price_unit": 1500.0,
                            "date_planned": "2026-08-12 08:00:00",
                        },
                    )
                ],
            }
        )

        self.assertTrue(order.approval_required)
        self.assertEqual(order.approval_state, "pending")
        with self.assertRaises(ValidationError):
            order.button_confirm()

        order = order.with_user(self.approver)
        order.action_approve_fnb()
        self.assertEqual(order.approval_state, "approved")
        self.assertEqual(order.approved_by_id, self.approver)
        self.assertTrue(order.approved_at)

        order.button_confirm()
        self.assertEqual(order.state, "purchase")
        self.assertEqual(order.approval_state, "approved")

    def test_regular_user_cannot_approve(self):
        order = self.order.with_user(self.regular_user)

        with self.assertRaises(AccessError):
            order.action_approve_fnb()

        self.assertFalse(self.order.approved_by_id)
        self.assertFalse(self.order.approved_at)
        self.assertEqual(self.order.approval_state, "pending")

    def test_direct_audit_field_write_is_blocked(self):
        with self.assertRaises(AccessError):
            self.order.write({"approved_by_id": self.env.user.id})

    def test_business_change_resets_existing_approval(self):
        order = self.order.with_user(self.approver)
        order.action_approve_fnb()
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

    def test_vendor_change_resets_existing_approval(self):
        order = self.order.with_user(self.approver)
        order.action_approve_fnb()
        approved_at = order.approved_at
        self.assertEqual(order.approval_state, "approved")

        replacement_vendor = self.env["res.partner"].create(
            {"name": "Replacement Ingredient Supplier", "supplier_rank": 1}
        )
        order.write({"partner_id": replacement_vendor.id})

        self.assertEqual(order.partner_id, replacement_vendor)
        self.assertFalse(order.approved_by_id)
        self.assertFalse(order.approved_at)
        self.assertTrue(approved_at)
        self.assertEqual(order.approval_state, "pending")

    def test_order_line_change_resets_existing_approval(self):
        order = self.order.with_user(self.approver)
        order.action_approve_fnb()
        approved_at = order.approved_at
        self.assertEqual(order.approval_state, "approved")

        line = order.order_line
        line.write({"price_unit": 2000.0})

        self.assertEqual(line.price_unit, 2000.0)
        self.assertFalse(order.approved_by_id)
        self.assertFalse(order.approved_at)
        self.assertTrue(approved_at)
        self.assertEqual(order.approval_state, "pending")

    def test_rejection_wizard_requires_meaningful_reason(self):
        wizard = self.env["fnb.purchase.rejection.wizard"].with_user(
            self.approver
        ).create(
            {
                "purchase_order_id": self.order.id,
                "reason": " no ",
            }
        )
        with self.assertRaises(ValidationError):
            wizard.action_confirm_rejection()

    def test_regular_user_cannot_reject(self):
        with self.assertRaises(AccessError):
            self.order.with_user(self.regular_user).action_reject_fnb(
                reason="Budget is not approved"
            )

    def test_approver_can_reject_with_wizard(self):
        wizard = self.env["fnb.purchase.rejection.wizard"].with_user(
            self.approver
        ).create(
            {
                "purchase_order_id": self.order.id,
                "reason": "  Supplier quotation exceeds approved budget.  ",
            }
        )
        result = wizard.action_confirm_rejection()
        self.assertEqual(result, {"type": "ir.actions.act_window_close"})
        self.assertEqual(self.order.approval_state, "rejected")
        self.assertEqual(
            self.order.rejection_reason,
            "Supplier quotation exceeds approved budget.",
        )
        with self.assertRaises(ValidationError):
            self.order.button_confirm()
