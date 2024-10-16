from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    job_grade = fields.Selection(
        [
            ('junior', 'Junior'),
            ('mid', 'Mid'),
            ('senior', 'Senior'),
            ('lead', 'Lead')
        ], 
        string="Job Grade", 
        default="junior"  
    )
    attendance_device_id = fields.Char(string="Attendance Device ID")
