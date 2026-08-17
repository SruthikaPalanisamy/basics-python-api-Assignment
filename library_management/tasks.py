import frappe

def every_minute_task():
    frappe.log_error(
        title="Minute Scheduler",
        message="Running every minute"
    )