# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Site(models.Model):
    _name = 'site'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'site_name'
    _description = "Site"

    site_name = fields.Char(string="Site Name")
    site_code = fields.Char(string="Site Code")
