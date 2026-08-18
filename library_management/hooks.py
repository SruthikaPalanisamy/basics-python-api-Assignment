app_name = "library_management"
app_title = "Library Management"
app_publisher = "Me"
app_description = "This is a Library Management App"
app_email = "sruthikap.23csd@kongu.edu"
app_license = "mit"

scheduler_events = {
    "daily": [
        "library_management.tasks.daily_maintenance"
        ]
}
# website with dynamic routes
# get_web_pages_with_dynamic_routes = "library_management.script.get_web_pages_with_dynamic_routes"

# homepage = "homepage"



# Portal Side Bar
# portal_menu_items = [
#     {
#         "title": "Test Menu",
#         "route": "/admin-dashboard"
#     }
# ]
# portal_menu_items = [
#     {
#         "title": "Dashboard",
#         "route": "/dashboard",
#         "role": "Student"
#     },
#     {
#         "title": "My Books",
#         "route": "/my-books",
#         "role": "Student"
#     },
# ]
# Base Tempalte
# base_template = "library_management/templates/my_custom_base.html"
# base_template_map = {
#     r"docs.*": "templates/doc_template.html"
# }


# braintree_success_page = "library_management.integrations.braintree.success_page"


# default_mail_footer = """
# <div>
#     <b>Sent via Library Management System</b>
# </div>
# """

# auth_hooks = [
#     "library_management.over.validate_custom_auth"
# ]



#Document Query
# permission_query_conditions = {
#     "Jammy": "library_management.permissions.todo_query"
# }


# has_permission = {
#     "Event": "library_management.permissions.event_has_permission"
# }

# has_permission = {
#     "Student": "library_management.permissions.student_permission"
# }

# override_doctype_class = {
#     "ToDo": "library_management.overrides.todo.CustomToDo"
# }

# calendars = ["C_view" ]



# doc_events = {
#     "Travel Manager": {
#         "before_insert": "library_management.crud_events.before_insert_book",
#         "after_insert": "library_management.crud_events.after_insert_book"
#     }
# }

# doctype_js = {

#     "ToDo": "public/js/todo.js"

# }

# jinja = {
#     "methods": [
#         "library_management.utils.get_library_name",
#         "library_management.utils.greet"
#     ],
#     "filters": [
#         "library_management.utils.to_upper",
#         "library_management.utils.reverse_string"
#     ]
# }


# override_whitelisted_methods = {
#     "frappe.client.get_count" : [library_management.whitelisted.custom_get_count]
# }
# override_whitelisted_methods = {
#     "frappe.client.get_count": "library_management.whitelisted.custom_get_count"
# }

# notification_config = "library_management.notifications.get_config"
# # auto_cancel_exempted_doctypes = ["Library_Category"]
# ignore_links_on_delete = ["Receipt"]


# additional_timeline_content = {
#     "*": [
#         "library_management.timeline.all_timeline"
#     ]
# }
# scheduler_events = {
#     "all": [
#         "library_management.tasks.every_minute_task"
#     ]
# }
# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "library_management.tasks.every_minute_task"
#         ] 
#     }
# }
# runs 4 mins
# before_migrate = "library_management.migrate.before_migrate"
# after_migrate = "library_management.migrate.after_migrate"

# auth_hooks = [
#     "library_management.auth.validate_token"
# ]

# extend_doctype_class = {
#     "Tag" : ["library_management.extensions.tag.Add" , "library_management.extensions.name.Join"] 
    
# }

# fixtures = [
#     "Library_Category" , 

#     {
#         "dt": "Profile1", 
#         "filters": [
#             ["name", "=", "A-0001"] 
#         ]
#     }
# ]

#signup_form_template = "library_management/templates/signup-form.html"

# user_data_fields = [
#     {
#         "doctype": "Travel Manager",
#         "filter_by": "email"
#     } , {
#         "doctype": "Customer" , 
#         "filter_by": "password"
#     }
# ]
# your_custom_app/hooks.py

# user_data_fields = [
#     # Case 1: Scrub specific fields in a custom profile DocType where email matches
#     {
#         "doctype": "Travel Manager",
#         "filter_by": "email",
#         "redact_fields": ["email", "phone_number"],
#         "rename": True, # Renames document if primary key is the user's email
#     }

    # # Case 2: Strict scrub for sensitive feedback or comments across the whole app
    # {
    #     "doctype": "Project Review",
    #     "filter_by": "reviewer_email",
    #     "strict": True,
    #     "redact_fields": ["review_text"],
    # },

    # # Case 3: Partial redaction for user mention references in logs
    # {
    #     "doctype": "Activity Log",
    #     "filter_by": "user",
    #     "partial": True
    # }
# ]
# extend_bootinfo = "library_management.boot.extend_bootinfo"

# before_install = "library_management.setup.install.before_install"
# after_install = "library_management.setup.install.after_install"
# after_sync = "library_management.setup.install.after_sync"

# before_uninstall = "library_management.setup.install.before_uninstall"
# after_uninstall = "library_management.setup.install.after_uninstall"


# brand_html = """
# <div style="display:flex;align-items:center;gap:8px;">
#     <img src="/assets/library_management/images/image.png"
#          height="30">
#     <span>TennisMart</span>
# </div>
# # """

# on_login = "library_management.auth_hooks.login_handler"
# on_session_creation = "library_management.auth_hooks.session_created"
# on_logout = "library_management.auth_hooks.logout_handler"

    
# doctype_js = {
#     "ToDo": "library_management/public/js/todo.js" }


# update_website_context = (
#     "library_management.website_context.update_context"
# )

# extend_website_page_controller_context = {
#     "frappe.www.404": "library_management.website_context.context_404"
# }

# website_route_rules = [
#     {
#         "from_route": "/project/<name>",
#         "to_route": "project"
#     }
# ] 

# website_path_resolver = (
#     "library_management.path_resolver.resolve_path"
# )

# website_clear_cache = (
#     "library_management.website.clear_cache"
# )

#app_include_css = "/assets/library_management/css/custom.css"
#app_include_js = "/assets/library_management/js/custom.js"

# web_include_css = "/assets/library_management/css/custom.css"
# web_include_js = "/assets/library_management/js/custom.js"

# webform_include_js = {
#     "student-form": "/library_management/assets/js/custom.js"
# }

# webform_include_css = {
#     "student-form": "/library_management/assets/css/custom.css"
# }


# sounds = [
#     {"name": "success", "src": "/assets/app/sounds/success.mp3", "volume": 0.8}
# # ]


# webform_include_js = "/assets/library_management/js/custom.js"
# webform_include_css = "/assets/library_management/css/custom.css"


#page_js = {
 #   "permission-manager": "/assets/library_management/js/permission-manager.js"
#}



# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_management",
# 		"logo": "/assets/library_management/logo.png",
# 		"title": "Library Management",
# 		"route": "/library_management",
# 		"has_permission": "library_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "library_management.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
#Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "library_management.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["library_management.utils.before_request"]
# after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

