# Copyright (c) 2026, Me and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class Book(Document):
# 	pass

# import frappe
# from frappe.model.document import Document


# class Book(Document):

#     def on_update(self):

#         frappe.publish_realtime(
#             "book_updated",
#             {
#                 "book": self.name,
#                 "title": self.title,
#                 "message": "Book has been updated"
#             }
#         )

import frappe
from frappe.model.document import Document


class Book(Document):

    def on_update(self):

        frappe.publish_realtime(
            "book_updated",
            {
                "book": self.name1,
                "amt": self.amt
            }
        )