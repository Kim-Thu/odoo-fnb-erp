from odoo.tests.common import TransactionCase


class TestWarehouseInternalTransfer(TransactionCase):
    def test_internal_transfer_between_demo_locations(self):
        warehouse_rm = self.env.ref("fnb_core.stock_warehouse_rm_demo")
        warehouse_prod = self.env.ref("fnb_core.stock_warehouse_prod_demo")
        warehouse_fg = self.env.ref("fnb_core.stock_warehouse_fg_demo")

        self.assertEqual(warehouse_rm.company_id, self.env.company)
        self.assertEqual(warehouse_prod.company_id, self.env.company)
        self.assertEqual(warehouse_fg.company_id, self.env.company)

        source = warehouse_rm.lot_stock_id
        production = warehouse_prod.lot_stock_id
        finished = warehouse_fg.lot_stock_id

        self.assertEqual(source.usage, "internal")
        self.assertEqual(production.usage, "internal")
        self.assertEqual(finished.usage, "internal")

        product = self.env["product.product"].create(
            {
                "name": "T1203 Demo Transfer Product",
                "is_storable": True,
                "company_id": self.env.company.id,
            }
        )

        self.env["stock.quant"]._update_available_quantity(product, source, 5.0)

        picking = self.env["stock.picking"].create(
            {
                "picking_type_id": warehouse_rm.int_type_id.id,
                "location_id": source.id,
                "location_dest_id": production.id,
            }
        )
        move = self.env["stock.move"].create(
            {
                "name": "T1203 RM to Production",
                "picking_id": picking.id,
                "product_id": product.id,
                "product_uom_qty": 2.0,
                "product_uom": product.uom_id.id,
                "location_id": source.id,
                "location_dest_id": production.id,
            }
        )
        picking.action_confirm()
        picking.action_assign()
        move.move_line_ids.quantity = 2.0
        picking.button_validate()

        self.assertEqual(picking.state, "done")
        self.assertEqual(move.state, "done")
        self.assertEqual(
            self.env["stock.quant"]._get_available_quantity(product, source), 3.0
        )
        self.assertEqual(
            self.env["stock.quant"]._get_available_quantity(product, production), 2.0
        )
