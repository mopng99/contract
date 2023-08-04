# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentTerms(models.Model):
    _name = 'payment.terms'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Payment Terms"
    _rec_name = "field1"

    field1 = fields.Text(string='field1', tracking=True)




