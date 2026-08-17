import frappe

def validate_token():
    token = frappe.get_request_header("Authorization")

    if token == "Bearer my-secret-token":
        frappe.set_user("Administrator")


@frappe.whitelist(allow_guest=True)
def who_am_i():
    return frappe.session.user