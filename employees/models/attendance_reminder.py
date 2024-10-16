from odoo import models, fields, api
from datetime import datetime, timedelta

class Employee(models.Model):
    _inherit = 'hr.employee'

    last_reminder_sent = fields.Datetime(string="Last Reminder Sent")
    reminder_count = fields.Integer(string="Reminder Count", default=0)

    def send_attendance_reminder(self):

        three_days_ago = datetime.now() - timedelta(days=3)


        employees_no_attendance = self.env['hr.employee'].search([
            ('attendance_log_ids', '=', False),  
            '|',  
            ('attendance_log_ids.check_in', '<', three_days_ago), 
            ('attendance_log_ids', '=', False),  
        ])

        for employee in employees_no_attendance:

            if employee.last_reminder_sent and employee.last_reminder_sent > three_days_ago:
                continue

            manager = employee.parent_id  

            if manager:

                template = self.env.ref('employees.email_template_attendance_reminder')
                template.send_mail(employee.id, force_send=True)

                # Update reminder data
                employee.last_reminder_sent = datetime.now()
                employee.reminder_count += 1

    def send_daily_reminder(self):

        employees = self.search([])
        employees.send_attendance_reminder()
