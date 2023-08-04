# -*- coding: utf-8 -*-
# from odoo import http


# class 14-uanalyst-construction(http.Controller):
#     @http.route('/14-uanalyst-construction/14-uanalyst-construction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/14-uanalyst-construction/14-uanalyst-construction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('14-uanalyst-construction.listing', {
#             'root': '/14-uanalyst-construction/14-uanalyst-construction',
#             'objects': http.request.env['14-uanalyst-construction.14-uanalyst-construction'].search([]),
#         })

#     @http.route('/14-uanalyst-construction/14-uanalyst-construction/objects/<model("14-uanalyst-construction.14-uanalyst-construction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('14-uanalyst-construction.object', {
#             'object': obj
#         })
