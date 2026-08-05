from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    fnb_internal_sku = fields.Char(
        string="F&B Internal SKU",
        index=True,
        copy=False,
        help="Internal business identifier used by the F&B operation.",
    )
    fnb_shelf_life_days = fields.Integer(
        string="Shelf Life (Days)",
        default=0,
        help="Expected shelf life in days. Must be zero or greater.",
    )
    fnb_storage_condition = fields.Selection(
        selection=[
            ("ambient", "Ambient"),
            ("chilled", "Chilled"),
            ("frozen", "Frozen"),
        ],
        string="Storage Condition",
        default="ambient",
        required=True,
    )
    fnb_ingredient_classification = fields.Selection(
        selection=[
            ("raw", "Raw Material"),
            ("semi_finished", "Semi-finished"),
            ("finished", "Finished Product"),
            ("packaging", "Packaging"),
        ],
        string="F&B Classification",
        index=True,
    )
    fnb_requires_traceability = fields.Boolean(
        string="Require Lot & Expiry Traceability",
        help="Require lot tracking and an expiry date for stock receipts.",
    )

    _sql_constraints = [
        (
            "fnb_internal_sku_company_unique",
            "unique(fnb_internal_sku, company_id)",
            "The F&B Internal SKU must be unique per company.",
        ),
    ]

    @api.onchange("fnb_requires_traceability")
    def _onchange_fnb_requires_traceability(self):
        if self.fnb_requires_traceability:
            self.tracking = "lot"
            self.use_expiration_date = True

    @api.constrains("fnb_shelf_life_days")
    def _check_fnb_shelf_life_days(self):
        for record in self:
            if record.fnb_shelf_life_days < 0:
                raise ValidationError("Shelf life cannot be negative.")

    @api.constrains("fnb_requires_traceability", "tracking", "use_expiration_date")
    def _check_fnb_traceability_configuration(self):
        for record in self:
            if not record.fnb_requires_traceability:
                continue
            if record.tracking != "lot":
                raise ValidationError(
                    "Products requiring F&B traceability must use lot tracking."
                )
            if not record.use_expiration_date:
                raise ValidationError(
                    "Products requiring F&B traceability must use expiration dates."
                )
