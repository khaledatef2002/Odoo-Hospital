from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError


class Appointments(models.Model):
    _name = 'hospital.appointments'
    _description = 'Appointments Module'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment ID',
                       required=True,
                       readonly=True,
                       copy=False,
                       index=True,
                       default=lambda self: _('New'))

    patient_id = fields.Many2one('res.partner', 'Patient', required=True, domain=[('is_patient', '=', True)])

    patient_age = fields.Integer(string='Patient Age', related='patient_id.age')
    notes = fields.Text(string='Notes')
    appointment_date = fields.Date(string='Date Time', required=True, Tracking=True)

    prescription_ids = fields.One2many('hospital.prescription', 'appointment_id', reaconly="status in ['done', 'cancel']")
    doctor_id = fields.Many2one('res.users', string='Doctor', domain=[('is_doctor', '=', True)], readonly="status != 'new'")

    status = fields.Selection([
        ('new', 'New'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Canceled')
    ], default='new', string='Status', Tracking=True)

    def set_confirmed(self):
        for rec in self:
            rec.status = 'confirm'

    def set_done(self):
        for rec in self:
            rec.status = 'done'

    def set_cancel(self):
        for rec in self:
            rec.status = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointments.sequence') or _('New')

        # Call super to create records
        return super(Appointments, self).create(vals)

    def write(self, vals):
        if self.status == 'cancel' or self.status == 'done':
            # Raise an error if the status is 'Cancelled'
            raise UserError("You cannot modify a cancelled or done appointment.")

        # If no condition is violated, allow the changes
        return super(Appointments, self).write(vals)