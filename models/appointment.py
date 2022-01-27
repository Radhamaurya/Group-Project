from tokenize import group
from attr import field
from odoo import fields, models, api

class Appointment_System(models.Model):
    _name = 'appointment.system'

    custmer = fields.Many2one("res.partner")
    group = fields.Char()
    timesheet = fields.Date()
    price = fields.Float()
