# odoo_employee_task
Employee Attendance Module
This module extends the functionality of Odoo’s Employee and Attendance modules by adding custom fields, automating attendance tracking, and providing an attendance summary report for employees.

Features
Adds new fields to the employee model for tracking Job Grade and Attendance Device ID.
Automates attendance logging from external devices.
Generates reports for total working hours and number of days worked in the current month.
Sends automated email reminders to managers for employees without attendance logs for the last 3 days.

Installation Instructions

1.Download or Clone the Module:

Clone the repository or download the module into your Odoo addons directory:

2.Update Apps List:

Start your Odoo server.
Go to Apps from the Odoo dashboard.
Click on Update App List to refresh the available modules.

3.Install the Module:

Search for Employee Attendance in the Apps menu.
Click Install to add the module to your Odoo instance.


Usage Instructions

1. Employee Model Customization
After installing the module, the following new fields are available in the Employee form:

Job Grade: Represents the employee’s rank (e.g., Junior, Mid, Senior, Lead).
Attendance Device ID: A unique ID used to synchronize employee attendance with a third-party attendance device.
You can find these fields under a new section on the Employee form.

2. Sync Attendance Logs
A Sync Attendance button is added to the Employee form view. This button allows manual synchronization of attendance records from third-party devices based on the Attendance Device ID.

When clicked, it will generate random attendance logs (for simulation purposes) for the past week. The logs will be automatically saved in the Attendance Log model.

Steps to sync attendance:

1.Go to Employees.
2.Open the employee form of the employee whose attendance you want to sync.
3.Click on Sync Attendance to fetch logs from the external device.


3.View Attendance Logs

Attendance logs are stored in the model employee.attendance.log. You can see these logs in a one-to-many field in the Employee form.

Logs include:

    Check-in and check-out times.
    Device ID used for check-ins/check-outs.

    .................................................................................
                  Generating Attendance Summary Report
The Attendance Summary Report shows the following details for each employee for the current month:

Total working hours based on check-in and check-out times.
Number of days worked.

Steps to generate the report:

1.Navigate to Employees → Reports → Attendance Summary Report.
2.The report will list the employees, their total working hours, and the number of days they have worked in the current month.
3.You can filter the report by employee or department.

...................................................................................
            Automated Attendance Reminder

The module includes a scheduled action that runs daily at 9 AM to check for employees who have not logged any attendance for the last 3 days. An email reminder is sent to the manager of those employees.

1.Scheduling the Action:
2.The scheduled action is automatically installed with the module.
To modify or check the schedule:
 Go to Settings → Technical → Automation → Scheduled Actions.
 Find the action named Send Attendance Reminder and ensure it is active and set to run daily at 9 AM.
