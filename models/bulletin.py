from odoo import models, fields, api

class Bulletin(models.Model):
    _name = 'bulletin'
    _description = 'Bulletin'

    teacher_id = fields.Many2one(comodel_name="teacher", string="Teacher")
    student_id = fields.Many2one(comodel_name="student", string="Student")
    bulletin_ligne_ids = fields.One2many(comodel_name="bulletin.ligne", inverse_name="bulletin_id", string="Lignes de bulletin")

    @api.depends('bulletin_ligne_ids.note', 'bulletin_ligne_ids.coefficient')
    def _compute_note_moyenne(self):
        for bulletin in self:
            total_weighted_grade = 0.0
            total_coefficients = 0.0
            for ligne in bulletin.bulletin_ligne_ids:
                total_weighted_grade += (ligne.note * ligne.coefficient)
                total_coefficients += ligne.coefficient
            bulletin.note_moyenne = total_weighted_grade / total_coefficients if total_coefficients else 0.0

    note_moyenne = fields.Float(compute='_compute_note_moyenne', string='Note Moyenne', store=True)

    stage = fields.Selection([
        ('draft', 'Draft'),
        ('failed', 'Failed'),
        ('succeed', 'Succeed'),
    ], string='Stage', default='draft')

    def action_fail(self):
        self.write({'stage': 'failed'})

    def action_success(self):
        self.write({'stage': 'succeed'})
