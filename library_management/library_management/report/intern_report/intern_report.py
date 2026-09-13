import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Intern Name",
            "fieldname": "name1",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": "Role",
            "fieldname": "role",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": "College",
            "fieldname": "college",
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "label": "Stipend",
            "fieldname": "stipend",
            "fieldtype": "Currency",
            "width": 120,
        },
    ]

    data = [
        {
            "name1": "Arun Kumar",
            "role": "Developer",
            "college": "ABC Engineering College",
            "stipend": 10000,
        },
        {
            "name1": "Priya Sharma",
            "role": "Tester",
            "college": "XYZ Institute of Technology",
            "stipend": 12000,
        },
        {
            "name1": "Rahul Raj",
            "role": "Designer",
            "college": "National Engineering College",
            "stipend": 11000,
        },
        {
            "name1": "Sneha Devi",
            "role": "Developer",
            "college": "Government Engineering College",
            "stipend": 15000,
        },
    ]

    return columns, data