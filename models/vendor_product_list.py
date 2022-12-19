from odoo import fields, models, api


class VendorProductList(models.Model):
    _inherit = 'purchase.order'

    is_vendor_product = fields.Boolean("Is Vendor Product")


class VendorProduct(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def sort_product(self):
        if self.order_id.is_vendor_product:
            return {'domain': {'product_id': [('seller_ids.name', '=', self.partner_id.id)]}}
