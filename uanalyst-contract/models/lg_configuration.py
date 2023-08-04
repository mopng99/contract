# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LgConfiguration(models.Model):
    _name = 'lg.configuration'
    _description = "LG Configuration"
    _rec_name = 'lg_number'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    lg_number = fields.Char(string='LG No', required=True)
    covered_percentage = fields.Float(string='Covered Percentage', tracking=True)
    lg_type = fields.Selection([
        ('initial', 'Initial'),
        ('final', 'Final'),
    ], string='LG Type', required=True, tracking=True)
    issuance_date = fields.Date(string='Issuance Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    amount = fields.Float(string='Amount', tracking=True)
    coverage_amount = fields.Float(string='Coverage Amount', tracking=True, compute="_compute_coverage_amount")
    state = fields.Selection([
        ('active', 'Active'),
        ('return', 'Returned'),
        ('extend', 'Extended'),
    ], string='State', tracking=True, default="active")
    bank_id = fields.Many2one('res.bank', string='Bank', tracking=True)

    @api.depends('covered_percentage', 'amount')
    def _compute_coverage_amount(self):
        for rec in self:
            rec.coverage_amount = rec.amount * rec.covered_percentage

