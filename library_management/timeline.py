import frappe

def all_timeline(doctype, docname):
    return [
        {
            "creation": frappe.utils.now(),
            "template": "Custom Timeline Entry",
            "template_data": {
                "message": f"Custom timeline for {doctype} - {docname}"
            }
        }
    ]