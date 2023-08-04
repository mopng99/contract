# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Contract(models.Model):
    _name = 'contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'partner_id'
    _description = "Contract"

    projects = fields.Char(string="Projects")
    pos = fields.Integer(string="POs")

    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('expired', 'Expired')]
        , default="new", string="status", tracking=True)

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, tracking=True)
    contract_no = fields.Char(string="Contract No", tracking=True)
    date = fields.Date('Date', tracking=True, default=fields.Date.today)
    start_date = fields.Date('Start date', tracking=True)
    end_date = fields.Date('End date', required=True, tracking=True)
    amount = fields.Integer(string="Amount", tracking=True)

    lg_initial = fields.Many2one('lg.configuration', string="LG Initial", tracking=True, domain=[('lg_type', '=', 'initial')])
    lg_initial_issuance_date = fields.Date(related='lg_initial.issuance_date', string="Initial Issuance Date")
    lg_initial_end_date = fields.Date(related='lg_initial.end_date', string="Initial End Date")

    lg_final = fields.Many2one('lg.configuration', string="LG Final", tracking=True, domain=[('lg_type', '=', 'final')])
    lg_final_issuance_date = fields.Date(related='lg_final.issuance_date', string="Final Issuance Date")
    lg_final_end_date = fields.Date(related='lg_final.end_date', string="Final End Date")

    # lg_amount = fields.Float(related='lg_no_id.amount', string="LG Amount", tracking=True)
    # lg_coverage_amount = fields.Float(related='lg_no_id.coverage_amount', string="Coverage Amount", tracking=True)

    contract_lines_ids = fields.One2many('contract.line', 'contract_id')

    pos_count = fields.Integer(string="Pos", compute="_compute_pos", store=True)
    pos_ids = fields.One2many('po', 'contract_id', string="po")

    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s (%s)' % (field.contract_no, field.partner_id.name)))
        return res

    def action_projects(self):
        return

    def action_pos(self):
        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'po',
            'name': _('PO'),
            'domain': "[('contract_id.partner_id', '=', %s)]" % self.partner_id.id,
            'view_type': 'tree',
            'target': 'current',
            'context': {
                'default_contract_id': self.id,
            },
        }
        return action

    def _compute_projects(self):
        return

    @api.depends('pos_ids')
    def _compute_pos(self):
        for rec in self:
            rec.pos_count = len(rec.pos_ids)

    @api.constrains('date', 'end_date')
    def _check_state(self):
        for rec in self:
            if rec.end_date <= rec.date:
                rec.state = "expired"
