from odoo import models, fields, api
from datetime import datetime, timedelta
import random

class AttendanceLog(models.Model):
    _name = 'employee.attendance.log'
    _description = 'Employee Attendance Log'
    
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    check_in = fields.Datetime(string="Check In", required=True)
    check_out = fields.Datetime(string="Check Out", required=True)
    device_id = fields.Char(string="Device ID")
    
    total_hours_month = fields.Float(string="Total Hours (Current Month)", compute="_compute_total_hours_month", store=True)
    days_worked_month = fields.Integer(string="Days Worked (Current Month)", compute="_compute_days_worked_month", store=True)
    department_id = fields.Many2one('hr.department', string='Department') 
    is_first_occurrence = fields.Boolean(
        string="First Occurrence", compute="_compute_is_first_occurrence", store=True
    )

    @api.depends('employee_id')
    def _compute_is_first_occurrence(self):
        for record in self:

            first_record = self.search([('employee_id', '=', record.employee_id.id)], order='id asc', limit=1)
            record.is_first_occurrence = record.id == first_record.id
    @api.depends('check_in', 'check_out')
    def _compute_total_hours_month(self):
        for log in self:
            current_month_start = datetime.now().replace(day=1)
            logs_in_month = self.search([
                ('employee_id', '=', log.employee_id.id),
                ('check_in', '>=', current_month_start)
            ])
            total_hours = 0
            for entry in logs_in_month:
                if entry.check_in and entry.check_out:
                    total_hours += (entry.check_out - entry.check_in).total_seconds() / 3600
            log.total_hours_month = total_hours

    @api.depends('check_in')
    def _compute_days_worked_month(self):
        for log in self:
            current_month_start = datetime.now().replace(day=1)
            logs_in_month = self.search([
                ('employee_id', '=', log.employee_id.id),
                ('check_in', '>=', current_month_start)
            ])
            days_worked = len(set(entry.check_in.date() for entry in logs_in_month))
            log.days_worked_month = days_worked

class Employee(models.Model):
    _inherit = 'hr.employee'

    attendance_log_ids = fields.One2many('employee.attendance.log', 'employee_id', string="Attendance Logs")

    def action_sync_attendance(self):
        for employee in self:
            # Simulate fetching and creating random attendance logs
            logs = self.generate_random_logs(employee)
            # Create attendance logs
            self.env['employee.attendance.log'].create(logs)

    def generate_random_logs(self, employee):
        logs = []
        device_id = employee.attendance_device_id  # Device ID from employee
        
        for day in range(7):  # Simulating logs for the last 7 days
            check_in_time = datetime.now() - timedelta(days=day, hours=random.randint(7, 9))
            check_out_time = check_in_time + timedelta(hours=random.randint(7, 9))  # Random working hours

            log = {
                'employee_id': employee.id,
                'check_in': check_in_time,
                'check_out': check_out_time,
                'device_id': device_id,
            }
            logs.append(log)
        
        return logs
