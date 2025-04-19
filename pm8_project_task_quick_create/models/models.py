# -*- coding: utf-8 -*-

from odoo import models

class ProjectTask(models.Model):
    _inherit = 'project.task' 

    def action_open_task(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Task',
            'res_model': 'project.task',
            'view_mode': 'form',
            'res_id': self.id, 
            'target': 'current', 
        }
