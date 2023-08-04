# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PoLine(models.Model):
    _name = 'accepted'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Accepted"

    po_id = fields.Many2one('po')

    po_no = fields.Char("Po Line No", tracking=True)
    line_id = fields.Char('Line Id', tracking=True)
    site_name = fields.Char("Site Name", tracking=True)
    site_code = fields.Char("Site Code", tracking=True)
    item_code = fields.Char("Item Code", tracking=True)
    item_description_id = fields.Many2one('product.template', string="Item Description", tracking=True)
    requested_quantity = fields.Integer("Requested Quantity", tracking=True)
    unite_price = fields.Float("Unit Price", tracking=True)
    line_amount = fields.Float("Line Amount", tracking=True)
    tax_rate = fields.Many2one('account.tax', string="Tax Rate", tracking=True)
    start_date = fields.Date('Start date', tracking=True)
    end_date = fields.Date('End date', tracking=True)
    published_date = fields.Date("Published Date", tracking=True)
    project_manager = fields.Char("Project Manager", tracking=True)

    # qty = fields.Float("QTY")
    accepted_amount = fields.Float("Accepted Amount", tracking=True)
    accepted = fields.Float("Accepted", tracking=True)

    statues = fields.Selection([
        ('new', 'New'),
        ('acceptance', 'Acceptance'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')]
        , default="new", string="statues", tracking=True, store=True)

    @api.model
    def _valid_field_parameter(self, field, parameter):
        if parameter == 'tracking':
            return True
        return super()._valid_field_parameter(field, parameter)

