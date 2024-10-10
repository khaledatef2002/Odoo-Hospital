from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Prescription(models.Model):
    _name = 'hospital.prescription'

    notes = fields.Char(string='Notes')

    appointment_id = fields.Many2one('hospital.appointments', string='Appointment')
    medicine_id = fields.Many2one('hospital.medicines', string='Medicine')

    @api.constrains('medicine_id', 'appointment_id')
    def _check_unqiune_medicine(self):
        for rec in self:
            search_result = rec.search([
                ('appointment_id', '=', rec.appointment_id.id),
                ('medicine_id', '=', rec.medicine_id.id),
                ('id', '=', rec.id)
            ])
            if search_result:
                raise ValidationError(f"The medicine {rec.medicine_id.name} already exists")