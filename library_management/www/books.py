# books.py

from library_management.website_context import extend_context

def get_context(context):

    context.title = "Books"

    context.books = [
        {"name": "Python"},
        {"name": "Java"}
    ]

    # Call the function
    extend_context(context)