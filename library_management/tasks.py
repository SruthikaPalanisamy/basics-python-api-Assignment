import frappe


# # For Schedular Events
# def every_minute_task():
#     frappe.log_error(
#         title="Minute Scheduler",
#         message="Running every minute"
#     )

# #Background job workers
# def test_background_job():
#     frappe.log_error(
#         "Background job executed successfully",
#         "Test Background Job"
#     )

# # For Multi Queue Jobs
# def short_job():
#     print("SHORT JOB EXECUTED")

# def default_job():
#     print("DEFAULT JOB EXECUTED")

# def long_job():
#     print("LONG JOB EXECUTED")


# # For email
# def send_test_email():
#     frappe.sendmail(
#         recipients=["sruthikap.23csd@kongu.edu"],
#         subject="Test Background Email",
#         message="Hello! This email was sent using a Frappe background job."
#     )

#     print("EMAIL SENT SUCCESSFULLY")

def daily_maintenance():
    frappe.log_error(
            "Daily Maintence",
            "Daily maintenance task executed successfully."

        )