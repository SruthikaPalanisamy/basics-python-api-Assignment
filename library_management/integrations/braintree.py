def success_page(data):
    print("Braintree success hook called!")
    print("Reference DocType:", data.reference_doctype)
    print("Reference DocName:", data.reference_docname)

    return "/thank-you"