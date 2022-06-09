# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo3modelos(http.Controller):
#     @http.route('/odoo_3modelos/odoo_3modelos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_3modelos/odoo_3modelos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_3modelos.listing', {
#             'root': '/odoo_3modelos/odoo_3modelos',
#             'objects': http.request.env['odoo_3modelos.odoo_3modelos'].search([]),
#         })

#     @http.route('/odoo_3modelos/odoo_3modelos/objects/<model("odoo_3modelos.odoo_3modelos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_3modelos.object', {
#             'object': obj
#         })
