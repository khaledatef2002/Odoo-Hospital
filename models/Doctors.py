from odoo import models, fields

class Doctors(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Is Doctor')