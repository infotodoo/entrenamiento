# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule1(http.Controller):
#     @http.route('/my_module1/my_module1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_module1/my_module1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_module1.listing', {
#             'root': '/my_module1/my_module1',
#             'objects': http.request.env['my_module1.my_module1'].search([]),
#         })

#     @http.route('/my_module1/my_module1/objects/<model("my_module1.my_module1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_module1.object', {
#             'object': obj
#         })
