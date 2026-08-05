from odoo import _, fields, models
from odoo.exceptions import AccessError, ValidationError


class PurchaseRejectionWizard(models.TransientModel):
    _name = "fnb.purchase.rejection.wizard"
    _description = "F&B Purchase Rejection Wizard"

    purchase_order_id = fields.Many2one(
        "purchase.order",
        required=True,
        readonly=True,
        ondelete="cascade",
    )
    reason = fields.Text(required=True)

    def action_confirm_rejection(self):
        self.ensure_one()
        if not self.env.user.has_group("fnb_core.group_fnb_purchase_approver"):
            raise AccessError(_("You are not allowed to reject purchase orders."))

        reason = (self.reason or "").strip()
        if len(reason) < 5:
            raise ValidationError(
                _("The rejection reason must contain at least 5 characters.")
            )

        self.purchase_order_id.action_reject_fnb(reason=reason)
        return {"type": "ir.actions.act_window_close"}
