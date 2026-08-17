import frappe

def before_insert_book(doc, method=None):
    doc.native = doc.native.upper()

def after_insert_book(doc, method=None):
    frappe.msgprint(f"Email user '{doc.email}' inserted successfully!")