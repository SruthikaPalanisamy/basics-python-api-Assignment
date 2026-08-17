import frappe
from frappe.query_builder import DocType


@frappe.whitelist()
def customer_payment():

    ticket = DocType("Tour Ticket")
    tourist1 = DocType("Tourist")

    # Query Builder
    query = (
        frappe.qb.from_(tourist1)
        .left_join(ticket)
        .on(tourist1.name1 == ticket.tourist)
        .select(
            tourist1.name,
            tourist1.name1,
            tourist1.gender,
            tourist1.email,
            ticket.amout,
        )
        .limit(15)
    )

    results = query.run(as_dict=True)

    # Document API
    if results:
        tourist = frappe.get_doc(
            "Tourist",
            results[0]["name"]
        )

        tourist.gender = "Girl"
        tourist.save()

    # Database API
    for row in results:
        frappe.db.set_value(
            "Tourist",
            row["name"],
            "email",
            "hi@tridotstech.com"
        )
    frappe.db.commit()
    return results