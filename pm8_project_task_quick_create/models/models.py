# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pm8_project_task_quick_create(models.Model):
#     _name = 'pm8_project_task_quick_create.pm8_project_task_quick_create'
#     _description = 'pm8_project_task_quick_create.pm8_project_task_quick_create'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
