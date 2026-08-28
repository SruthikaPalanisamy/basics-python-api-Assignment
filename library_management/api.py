import frappe

@frappe.whitelist()
def get_message():
    return "Hello"

@frappe.whitelist()
def greet(name):
    return f"Hello {name}"


@frappe.whitelist() 

def create_task(task_subject):
    task = frappe.new_doc("Task") 
    task.task_subject = task_subject 
    task.save() 
    return task.name
# from my_app.search import MyAppSearch


# def custom_logic(doc, method):
#     frappe.msgprint("Hook executed!")

# @frappe.whitelist()
# def download_file(name):
#     file = frappe.get_doc("File", name)

#     frappe.response.filename = file.file_name
#     frappe.response.filecontent = file.get_content()
#     frappe.response.type = "download"
#     frappe.response.display_content_as = "attachment"



# @frappe.whitelist()
# def search(query, filters=None):

#     search = MyAppSearch()

#     return search.search(
#         query,
#         filters=filters
#     )


# @frappe.whitelist()
# def get_recent_todos():

#     todos = frappe.get_list(
#         "ToDo",
#         fields=["name", "description", "owner"],
#         order_by="creation desc",
#         limit_page_length=5
#     )

#     records = []

#     for todo in todos:
#         owner_email = frappe.db.get_value(
#             "User",
#             todo.owner,
#             "email"
#         )

#         records.append({
#             "name": todo.name,
#             "description": todo.description,
#             "owner_email": owner_email
#         })

#     timestamp = frappe.utils.now()

#     return {
#         "timestamp": timestamp,
#         "records": records
#     }