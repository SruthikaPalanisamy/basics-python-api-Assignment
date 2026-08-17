

import frappe

@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    frappe.msgprint("My custom method is called!")

    return 1200