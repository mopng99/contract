# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ContractLine(models.Model):
    _name = 'contract.line'
    _description = "Contract Line"

    contract_id = fields.Many2one('contract')

    item_description_id = fields.Many2one('product.template', string="Item Description", tracking=True)
    item_code = fields.Char("Item Code", related="item_description_id.default_code", tracking=True)
    unit_price = fields.Float("Unit Price", related="item_description_id.list_price", tracking=True)

    @api.model
    def _valid_field_parameter(self, field, parameter):
        if parameter == 'tracking':
            return True
        return super()._valid_field_parameter(field, parameter)

