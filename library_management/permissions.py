import frappe


# def todo_query(user):
#     if not user:
#         user = frappe.session.user

#     return "(`tabToDo`.owner = {user} or `tabToDo`.assigned_by = {user})".format(
#         user=frappe.db.escape(user)
#     )

def event_has_permission(doc, user=None, permission_type=None):

    # when reading a document allow if event is Public
    if permission_type == "read" and doc.event_type == "Public":
        return True

    # when writing a document allow if event owned by user
    if permission_type == "write" and doc.owner == user:
        return True

    return False


def todo_query(user):
    if not user:
        user = frappe.session.user

    if user == "Sruthi":
        return "(`tabJammy`.name1 = 'David')"

    return "1=0"

# def todo_query(user):
#     return "`tabJammy`.`name1` = 'David'"


# def student_permission(doc, user=None, permission_type=None):

#     if frappe.session.user == "Administrator":
#         return True

#     return False
