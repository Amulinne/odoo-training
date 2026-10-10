# -*- coding: utf-8 -*-
# from odoo import http


# class LabSuvarskiy(http.Controller):
#     @http.route('/lab_suvarskiy/lab_suvarskiy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab_suvarskiy/lab_suvarskiy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab_suvarskiy.listing', {
#             'root': '/lab_suvarskiy/lab_suvarskiy',
#             'objects': http.request.env['lab_suvarskiy.lab_suvarskiy'].search([]),
#         })

#     @http.route('/lab_suvarskiy/lab_suvarskiy/objects/<model("lab_suvarskiy.lab_suvarskiy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab_suvarskiy.object', {
#             'object': obj
#         })

