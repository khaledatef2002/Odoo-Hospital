from odoo import fields, models

class AddAppointmentWizard(models.TransientModel):
    _name = 'add.appointment'

    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain="[('is_patient', '=', True)]")

    notes = fields.Text(string='notes')
    appointment_date = fields.Datetime(string="Date Time", required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', domain="[('is_doctor', '=', True), ('id', '=', uid)]")

    def confirm_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'notes': self.notes,
            'appointment_date': self.appointment_date,
            'doctor_id': self.doctor_id.id
        }
        self.env['hospital.appointments'].create(vals)
