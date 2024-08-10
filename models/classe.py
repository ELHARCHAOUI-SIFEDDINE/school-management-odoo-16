from odoo import models, fields, api

class Classe(models.Model):
    _name = 'classe'
    _description = 'Classe'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    code = fields.Char(string='Code', required=True)
    # Add additional fields specific to classes here

    @api.model
    def action_class_menu(self):
        return {
            'name': 'Classes',
            'type': 'ir.actions.act_window',
            'res_model': 'classe',
            'view_mode': 'tree',
            'view_id': self.env.ref('school_system.view_classe_tree').id,
        }

