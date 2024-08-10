# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolSystem(http.Controller):
#     @http.route('/school_system/school_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_system/school_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_system.listing', {
#             'root': '/school_system/school_system',
#             'objects': http.request.env['school_system.school_system'].search([]),
#         })

#     @http.route('/school_system/school_system/objects/<model("school_system.school_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_system.object', {
#             'object': obj
#         })
