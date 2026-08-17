import frappe

def validate_custom_auth():
    print("AUTH HOOK CALLED")

    token = frappe.get_request_header("Authorization")

    print("Token:", token)

    if token == "Bearer sruthi123":
        frappe.set_user("sruthikap.23csd@kongu.edu")

        