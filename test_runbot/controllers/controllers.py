# -*- coding: utf-8 -*-
# from odoo import http


# class TestRunbot(http.Controller):
#     @http.route('/test_runbot/test_runbot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_runbot/test_runbot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_runbot.listing', {
#             'root': '/test_runbot/test_runbot',
#             'objects': http.request.env['test_runbot.test_runbot'].search([]),
#         })

#     @http.route('/test_runbot/test_runbot/objects/<model("test_runbot.test_runbot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_runbot.object', {
#             'object': obj
#         })
