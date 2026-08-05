from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    approval_state = fields.Selection(
        selection=[
            ("not_required", "Not Required"),
            ("pending", "Pending Approval"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        string="Approval Status",
        compute="_compute_approval_state",
        store=True,
        readonly=True,
    )
    approval_required = fields.Boolean(
        compute="_compute_approval_state",
        store=True,
        readonly=True,
    )
    approved_by_id = fields.Many2one(
        "res.users",
        string="Approved By",
        readonly=True,
        copy=False,
    )
    approved_at = fields.Datetime(readonly=True, copy=False)
    rejection_reason = fields.Text(readonly=True, copy=False)

    @api.depends("amount_total", "company_id.fnb_purchase_approval_limit", "state")
    def _compute_approval_state(self):
        for order in self:
            limit = order.company_id.fnb_purchase_approval_limit
            required = bool(limit and order.amount_total >= limit)
            order.approval_required = required
            if not required:
                order.approval_state = "not_required"
            elif order.approved_by_id:
                order.approval_state = "approved"
            elif order.rejection_reason:
                order.approval_state = "rejected"
            else:
                order.approval_state = "pending"

    def action_approve_fnb(self):
        self.ensure_one()
        if not self.env.user.has_group("fnb_core.group_fnb_purchase_approver"):
            raise UserError(_("You are not allowed to approve purchase orders."))
        if self.state not in ("draft", "sent"):
            raise ValidationError(_("Only draft RFQs can be approved."))
        if not self.approval_required:
            raise ValidationError(_("This purchase order does not require approval."))

        self.write(
            {
                "approved_by_id": self.env.user.id,
                "approved_at": fields.Datetime.now(),
                "rejection_reason": False,
            }
        )
        return True

    def action_reject_fnb(self):
        self.ensure_one()
        if not self.env.user.has_group("fnb_core.group_fnb_purchase_approver"):
            raise UserError(_("You are not allowed to reject purchase orders."))
        if self.state not in ("draft", "sent"):
            raise ValidationError(_("Only draft RFQs can be rejected."))

        reason = self.env.context.get("fnb_rejection_reason")
        if not reason:
            raise ValidationError(_("A rejection reason is required."))

        self.write(
            {
                "approved_by_id": False,
                "approved_at": False,
                "rejection_reason": reason.strip(),
            }
        )
        return True

    def button_confirm(self):
        for order in self:
            if order.approval_required and order.approval_state != "approved":
                raise ValidationError(
                    _("This purchase order must be approved before confirmation.")
                )
        return super().button_confirm()


class ResCompany(models.Model):
    _inherit = "res.company"

    fnb_purchase_approval_limit = fields.Monetary(
        string="Purchase Approval Threshold",
        currency_field="currency_id",
        default=0.0,
        help="Purchase orders at or above this amount require approval.",
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    fnb_purchase_approval_limit = fields.Monetary(
        related="company_id.fnb_purchase_approval_limit",
        readonly=False,
    )
