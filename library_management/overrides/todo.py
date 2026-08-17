import frappe
from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):

    def on_update(self):
        frappe.msgprint("CustomToDo on_update executed!")

        # Call the original ToDo on_update()
        super().on_update()