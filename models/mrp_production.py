# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id and self.product_id and self.product_id.partner_id != self.partner_id:
            self.product_id = False
        if self.partner_id:
            return {'domain': {'product_id': [('type', 'in', ['product', 'consu']),('partner_id', '=', self.partner_id.id),
                                              '|',('company_id', '=', False),('company_id', '=', self.company_id.id)]},
                    'context': {'default_detailed_type': 'product', 'default_partner_id': self.partner_id.id}}
        else:
            return {'domain': {'product_id': [('type', 'in', ['product', 'consu']),'|',('company_id', '=', False),('company_id', '=', self.company_id.id)]},
                    'context': {'default_detailed_type': 'product'}}