import frappe

from frappe.search.sqlite_search import SQLiteSearch


class MyAppSearch(SQLiteSearch):

    INDEX_NAME = "library_management_search.db"

    INDEX_SCHEMA = {
        "text_fields": [
            "title",
            "content"
        ],

        "metadata_fields": [
            "status",
            "priority"
        ],

        "tokenizer":
            "unicode61 remove_diacritics 2 tokenchars '-_@.'"
    }

    INDEXABLE_DOCTYPES = {

        "Mobile": {

            "fields": [
                "name",
                {"title": "title"},
                {"content": "content"},
               
                "status",
                "priority"
            ],

            "filters": {
                "status": ("=", "Available")
            }
        }
    }

    def get_search_filters(self):

        user = frappe.session.user

        if user == "Administrator":
            return {}

        return {
            "owner": user
        }