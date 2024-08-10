from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'

    name = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)

    @api.model
    def action_teacher_menu(self):
        return {
            'name': 'Teachers',
            'type': 'ir.actions.act_window',
            'res_model': 'teacher',
            'view_mode': 'tree',
            'view_id': self.env.ref('school_system.view_teacher_tree').id,
        }
