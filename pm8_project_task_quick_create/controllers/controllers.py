# -*- coding: utf-8 -*-
# from odoo import http


# class Pm8ProjectTaskQuickCreate(http.Controller):
#     @http.route('/pm8_project_task_quick_create/pm8_project_task_quick_create', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pm8_project_task_quick_create/pm8_project_task_quick_create/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pm8_project_task_quick_create.listing', {
#             'root': '/pm8_project_task_quick_create/pm8_project_task_quick_create',
#             'objects': http.request.env['pm8_project_task_quick_create.pm8_project_task_quick_create'].search([]),
#         })

#     @http.route('/pm8_project_task_quick_create/pm8_project_task_quick_create/objects/<model("pm8_project_task_quick_create.pm8_project_task_quick_create"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pm8_project_task_quick_create.object', {
#             'object': obj
#         })
