import frappe

def update_context(context):

    context.company_name = "ABC Library"
    context.current_year = "2026"
    context.footer_message = "Powered by Frappe"

def extend_context(context):
    context.message = "Today's Special Collection"
    context.discount = "20%"
    
def context_404(context):
    context.custom_message = "This page was customized!"
    