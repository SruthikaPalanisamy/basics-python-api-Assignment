import frappe

def extend_bootinfo(bootinfo):
    bootinfo["company_name"] = "ABC Library"
    bootinfo["welcome_message"] = "Welcome to Library Management"