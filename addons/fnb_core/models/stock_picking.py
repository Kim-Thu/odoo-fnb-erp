from odoo import _, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        result = super().button_validate()
        for picking in self.filtered(lambda record: record.picking_type_code == "incoming"):
            for line in picking.move_line_ids.filtered(
                lambda move_line: move_line.quantity > 0
                and move_line.product_id.product_tmpl_id.fnb_requires_traceability
            ):
                if not line.lot_id:
                    raise ValidationError(
                        _("Product %s requires a lot before receipt validation.")
                        % line.product_id.display_name
                    )
                if not line.lot_id.expiration_date:
                    raise ValidationError(
                        _("Lot %s requires an expiration date before receipt validation.")
                        % line.lot_id.display_name
                    )
        return result
