from odoo import models, fields, api

class BulletinLigne(models.Model):
    _name = 'bulletin.ligne'
    _description = 'Bulletin ligne'

    matiere_id = fields.Many2one(comodel_name="matiere", string="Matière")
    note = fields.Float(string="Note", required=True)
    coefficient = fields.Float(string="Coefficient", required=True)  # New field
    bulletin_id = fields.Many2one(comodel_name="bulletin", string="Bulletin")
