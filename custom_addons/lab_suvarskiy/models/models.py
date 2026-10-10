# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    description = fields.Text(string="Описание")
    product_id = fields.Many2one(
        'product.product',
        string='Услуга'
    )
    stage_id_extra = fields.Many2one(
    'crm.stage',
    string='Дополнительный этап'
    )