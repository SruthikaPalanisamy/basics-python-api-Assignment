import frappe
from frappe.model.document import Document

class Join(Document):

    @property
    def fullname(self):
        frappe.msgprint(f"{self.name1}, {self.initial}")
        return f"{self.name1}  {self.initial}"