# -*- encoding: utf-8 -*-

from openerp import models, fields

class product_product(models.Model):
    _inherit = "product.product"

    def name_get(self, cr, uid, ids, context=None):
    	context = dict(context or {})
        context['display_default_code'] = False
        return super(product_product, self).name_get(cr, uid, ids, context=context)
