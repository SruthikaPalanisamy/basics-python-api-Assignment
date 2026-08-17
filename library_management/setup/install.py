import frappe

def before_install():
    print("Before save executed successfully")
    frappe.msgprint("Before Install Hook Executed")


def after_install():
    print("After  save executed successfully")
    frappe.msgprint("App Installed Successfully!")


def after_sync():
    print("after sync  executed successfully")
    frappe.msgprint("After Sync Hook Executed")

def before_uninstall():
        print("before uninstall  executed successfully")


def after_uninstall():
        print("After uninstall  executed successfully")

