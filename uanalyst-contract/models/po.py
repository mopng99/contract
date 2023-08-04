# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Po(models.Model):
    _name = 'po'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Po"
    _rec_name = 'po_num'

    partner_id = fields.Many2one('res.partner', string='Partner')
    po_lines_ids = fields.One2many('po.line', 'po_id')
    contract_id = fields.Many2one('contract', string='Contract', tracking=True)
    po_num = fields.Char('PO No')
    start_date = fields.Date('Start date', tracking=True)
    end_date = fields.Date('End date', tracking=True)
    # project_name = fields.Many2one('', string='Project Name')
    payment_terms = fields.Many2one('payment.terms', string='Payment Terms', tracking=True)
    category = fields.Char("Category", tracking=True)
    bidding_area = fields.Float("Bidding Area", tracking=True)
    shipment_num = fields.Char('Shipment No', tracking=True)
    project_code = fields.Char('Project Code', tracking=True)
    state = fields.Selection([
        ('new', 'New'),
        ('approved', 'Approved'),
        ('cancel', 'Cancelled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')]
        , default="new", string="status", tracking=True)

    def action_approved(self):
        self.state = "approved"

    def action_cancelled(self):
        self.state = "cancel"
        for rec in self:
            rec.po_lines_ids.statues = "cancel"

    def check_all_pos_done(self, record):
        all_record = record.po_lines_ids.search_count([('po_id', '=', record.id)])
        count = 0
        for rec in record.po_lines_ids:
            if rec.statues == 'done':
                count += 1
        if all_record == count:
            record.state = "done"
