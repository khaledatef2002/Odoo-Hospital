from odoo import fields, models
from datetime import date
class Patients(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean(string="Is Patient")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(compute='calculate_age')

    app_count = fields.Integer(string='Count', compute='get_app_count')

    def get_app_count(self):
        count = self.env['hospital.appointments'].search_count([('patient_id', '=', self.id)])
        self.app_count = count

    def get_appointments(self):
        action = {
            'name': 'appointments',
            'res_model': 'hospital.appointments',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.id)]
        }

        return action

    def calculate_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = date.today().year - rec.birthdate.year
            else:
                rec.age = 0
