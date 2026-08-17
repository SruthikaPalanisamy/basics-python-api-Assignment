import frappe

def login_handler(login_manager):
    frappe.msgprint(f"Welcome {login_manager.user}")


def session_created(login_manager):
    frappe.msgprint("Session Created Successfully!")



def logout_handler(login_manager):
    frappe.msgprint("Logged Out Successfully!")
    frappe.msgprint(f"Goodbye {login_manager.user}")