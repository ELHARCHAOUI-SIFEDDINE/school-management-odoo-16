from odoo import models, fields, api

class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    teacher_id = fields.Many2one(comodel_name="teacher", string="Teacher")
    classe_id = fields.Many2one(comodel_name="classe", string="Classe")

    age = fields.Char(string='Age', required=True)
    bdate = fields.Date(string='Date Of Birth')
    student_age = fields.Float(string='Total Age', compute='_get_age_from_student')

    stage = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
    ], string='Stage', default='draft')

    def _get_age_from_student(self):
        today_date = fields.Date.context_today(self)
        for stud in self:
            if stud.bdate:
                bdate = stud.bdate
                total_age = str(int((today_date - bdate).days / 365))
                stud.student_age = total_age
            else:
                stud.student_age = 0

    def action_enroll(self):
        self.write({'stage': 'enrolled', 'nom' : 'oussama' })

    def action_complete(self):
        self.write({'stage': 'completed'})
        #for rec in self:
            #search
            #students = self.env['student'].search([])
            #print('students...', students)
            #students_age = self.env['student'].search([('age', '>=', 17), ('prenom', '=', 'talbi')])
            #print('students age...', students_age)
            #students_teacher = self.env['student'].search([('teacher_id', '=', "mehdi")])
            #print('students teacher...', students_teacher)

            #search_count
            #students_count = self.env['student'].search_count([])
            #print('students count...', students_count)

            #browse
            #browse_result = self.env['student'].browse(20)
            #"print("browse_result...", browse_result)
            #search_result = self.env['student'].search([('id', '=', 2)])
            #print("search_result...", search_result)

            #exists
            #if browse_result.exists():
                #print("Existing")
            #else :
                #print("Noooooo")

    @api.model
    def action_student_menu(self):
        return {
            'name': 'Students',
            'type': 'ir.actions.act_window',
            'res_model': 'student',
            'view_mode': 'tree',
            'view_id': self.env.ref('school_system.view_student_tree').id,
        }
