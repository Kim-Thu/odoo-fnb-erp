from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class StockLot(models.Model):
    _inherit = "stock.lot"

    @api.model_create_multi
    def create(self, vals_list):
        now = fields.Datetime.now()
        for vals in vals_list:
            if vals.get("expiration_date") or not vals.get("product_id"):
                continue

            product = self.env["product.product"].browse(vals["product_id"])
            template = product.product_tmpl_id
            if (
                template.fnb_requires_traceability
                and template.fnb_shelf_life_days > 0
            ):
                vals["expiration_date"] = now + relativedelta(
                    days=template.fnb_shelf_life_days
                )

        return super().create(vals_list)
