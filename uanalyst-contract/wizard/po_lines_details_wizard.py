# -*- coding: utf-8 -*-

from odoo import models, fields, _


class PoLinesDetailsWizard(models.TransientModel):
    _name = 'po.lines.details.wizard'
    _description = "Po Lines Details Wizard"

    qty = fields.Float("QTY")
    accepted_amount = fields.Float("Accepted Amount")
    accepted = fields.Float("Accepted")

    def action_accept(self):
        # if self.state == 'approved':
        obj = self
        self.env['po.line']._compute_accepted_amount(obj)
        # self.statues = 'acceptance'
        return



