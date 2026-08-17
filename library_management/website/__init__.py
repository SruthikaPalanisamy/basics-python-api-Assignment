import frappe

def clear_cache(path=None):
    print(f"Website cache cleared for: {path}")
    frappe.cache.delete_key("my_custom_cache")