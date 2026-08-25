from frappe.utils import (
    comma_and,
    money_in_words,
    validate_json_string,
    random_string,
    unique,
    get_abbr,
    validate_url
)

import frappe
from frappe.utils.pdf import get_pdf


@frappe.whitelist()
def generate_test_pdf():
    html = """
        <h1>Library Management</h1>
        <h2>Book Details</h2>

        <p><b>Book Name:</b> Python Programming</p>
        <p><b>Author:</b> James</p>
        <p><b>Price:</b> ₹500</p>
    """

    pdf = get_pdf(html)

    frappe.local.response.filename = "book_details.pdf"
    frappe.local.response.filecontent = pdf
    frappe.local.response.type = "pdf" 