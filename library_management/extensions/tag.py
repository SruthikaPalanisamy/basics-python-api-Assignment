import frappe
from frappe.model.document import Document

class Add(Document):

    def validate(self):    
            if not self.description:
                frappe.throw("Description is mandatory")   