# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    contract_count = fields.Integer(string="Contracts", compute="_compute_contract_count", store=True)
    contract_ids = fields.One2many('contract', 'partner_id')

    def open_action_contract(self):
        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'contract',
            'name': _('Contract'),
            'view_type': 'tree,form',
            'target': 'self',
            'domain': "[('partner_id', '=', %s)]" % self.id,
            'context': {
                'default_partner_id': self.id,
            },
        }
        return action

    @api.depends('contract_ids')
    def _compute_contract_count(self):
        for rec in self:
            rec.contract_count = len(rec.contract_ids)
