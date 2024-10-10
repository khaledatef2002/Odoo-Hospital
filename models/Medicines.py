from odoo import fields, models

class Medicines(models.Model):
    _name = 'hospital.medicines'

    name = fields.Char(string="Medicine Name")
    effective_material = fields.Char(string="Effective Material")
    prescription_ids = fields.One2many('hospital.prescription', 'medicine_id')