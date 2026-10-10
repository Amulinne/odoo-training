# -*- coding: utf-8 -*-
# from odoo import http


# class SntRassvet(http.Controller):
#     @http.route('/snt_rassvet/snt_rassvet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/snt_rassvet/snt_rassvet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('snt_rassvet.listing', {
#             'root': '/snt_rassvet/snt_rassvet',
#             'objects': http.request.env['snt_rassvet.snt_rassvet'].search([]),
#         })

#     @http.route('/snt_rassvet/snt_rassvet/objects/<model("snt_rassvet.snt_rassvet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('snt_rassvet.object', {
#             'object': obj
#         })

