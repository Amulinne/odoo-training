# -*- coding: utf-8 -*-
# from odoo import http


# class DrivingSchool(http.Controller):
#     @http.route('/driving_school/driving_school', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/driving_school/driving_school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('driving_school.listing', {
#             'root': '/driving_school/driving_school',
#             'objects': http.request.env['driving_school.driving_school'].search([]),
#         })

#     @http.route('/driving_school/driving_school/objects/<model("driving_school.driving_school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('driving_school.object', {
#             'object': obj
#         })

