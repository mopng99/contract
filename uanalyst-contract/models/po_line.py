# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PoLine(models.Model):
    _name = 'po.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Po Lines"

    po_id = fields.Many2one('po')

    po_no = fields.Char("Po Line No", compute="_compute_po_number", tracking=True)
    line_id = fields.Char('Line Id', tracking=True, required=True)
    site_id = fields.Many2one('site', string="Site Name", tracking=True)
    site_code = fields.Char(related='site_id.site_code', string="Site Code", tracking=True)
    item_code = fields.Char("Item Code", related="item_description_id.default_code", tracking=True)
    item_description_id = fields.Many2one('product.template', string="Item Description", tracking=True)
    requested_quantity = fields.Integer("Requested Quantity", tracking=True)
    remaining_quantity = fields.Integer("Remaining Quantity", tracking=True)
    unit_price = fields.Float("Unit Price", related="item_description_id.list_price", tracking=True)
    line_amount = fields.Float("Line Amount", compute="_compute_line_amount", tracking=True)
    tax_rate = fields.Many2one('account.tax', string="Tax Rate", tracking=True)
    start_date = fields.Date('Start date', tracking=True)
    end_date = fields.Date('End date', tracking=True)
    published_date = fields.Date("Published Date", tracking=True)
    project_manager = fields.Many2one(comodel_name='hr.employee', string="Project Manager", tracking=True)

    # qty = fields.Float("QTY")
    accepted_amount = fields.Float("Accepted Amount", tracking=True)
    selected_accepted_amount = fields.Float("Accepted Amount ", store=True)
    accepted = fields.Float("Accepted", tracking=True)
    accepted_id = fields.Many2one('accepted', string="Accepted Id")

    statues = fields.Selection([
        ('new', 'New'),
        ('acceptance', 'Acceptance'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')]
        , default="new", string="statues", tracking=True, store=True)

    def open_wizard(self):
        for rec in self:
            if rec.po_id.state in ('approved', 'in_progress'):
                action = {
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'po.line',
                    'name': _('PO Lines Details'),
                    'view_type': 'form',
                    'res_id': rec.id,
                    'target': 'new',
                }
            else:
                raise ValidationError(_('Must be PO State is Approved'))
        return action

    def action_accept(self):
        selected_ids = self.env.context.get('active_ids')
        records = self.env['po.line'].browse(selected_ids)
        for record in records:
            if record.remaining_quantity >= self.selected_accepted_amount:
                record.statues = 'acceptance'
                record.po_id.state = 'in_progress'
                record.accepted_amount = record.accepted_amount + self.selected_accepted_amount
                record.remaining_quantity = record.requested_quantity - record.accepted_amount
                if record.remaining_quantity == 0:
                    record.statues = "done"
                    self.env['po'].check_all_pos_done(record.po_id)
            else:
                raise ValidationError(_('PO >> %s Remaining Quantity is %s And must be Accepted Amount less than or equal Remaining Quantity') % (record.po_no, record.remaining_quantity))
        for rec in records:
            print(rec.tax_rate)
            accepted = self.env['accepted'].sudo().create({
                'po_no': rec.po_no,
                'accepted_amount': self.selected_accepted_amount,
                'line_amount': rec.line_amount,
                'tax_rate': rec.tax_rate.id,
                'start_date': rec.start_date,
                'end_date': rec.end_date,
                'published_date': rec.published_date,
            })
            rec.accepted_id = accepted.id
        return

    @api.depends('line_id', 'po_id.po_num', 'po_id.shipment_num')
    def _compute_po_number(self):
        for rec in self:
            if rec.line_id and rec.po_id.po_num and rec.po_id.shipment_num:
                rec.po_no = str(rec.line_id) + "-" + str(rec.po_id.po_num) + "-" + str(rec.po_id.shipment_num)
            else:
                rec.po_no = ""

    @api.depends('requested_quantity', 'unit_price')
    def _compute_line_amount(self):
        for rec in self:
            rec.line_amount = rec.requested_quantity * rec.unit_price

    @api.constrains('requested_quantity')
    def _compute_remaining_quantity(self):
        for rec in self:
            rec.remaining_quantity = rec.requested_quantity


