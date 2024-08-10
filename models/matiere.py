from odoo import models, fields, api

class Matiere(models.Model):
    _name = 'matiere'
    _description = 'Matiere'

    name = fields.Char(string="Libellé",required=True)
    code = fields.Char(string="Code")



