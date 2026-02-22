app_name = "irshad_demo"
app_title = "irshad_demo"
app_publisher = "Irshad"
app_description = "irshad_demo"
app_email = "irshadsha164@gmail.com"
app_license = "mit"

doc_events={
    "Item":{
        "after_insert":"irshad_demo.api.item_after_insert"
    },
    "Supplier":{
        "after_insert":"irshad_demo.api.new_supplier_added"
    },
    "Issue":{
         "validate":"irshad_demo.api.ticket_issued"
    },
    "Sales Order":{
        "on_submit":"irshad_demo.api.sales_order_recieved"
    },
    "Customer":{
        "after_insert":"irshad_demo.api.new_customer_created",
        "after_delete":"irshad_demo.api.after_customer_delete"
        # "on_trash":"irshad_demo.api.block_delete"
    },
    "Web Page":{
        "validate": "irshad_demo.api.validate_web_form"
    },
    "Task_demo":{
        "validate": [
            "irshad_demo.task_system.api.validate_task",
            "irshad_demo.task_system.api.calculate_hours"
        ],
        "on_submit":"irshad_demo.task_system.api.update_project_demo_status",
    },
    "Delivery Note":{
        "on_submit":"irshad_demo.task_system.api.validate_stock_before_sale"
    },
    "Task Log":{
        "on_submit":"irshad_demo.api.update_project_demo_status"
    },
    "POS Invoice":{
        "on_submit":"irshad_demo.pos_submit.api.handle_pos_submit"
    }
    
}

shedular_events = {
    "daily":["irshad_demo.api.send_issue_reminders",
             "irshad_demo.task_system.api.auto_mark_overdue"],
    "weekly":["irshad_demo.api.auto_close_issue"],  
}

fixtures = [
   "Web Page"
]

# doc_events = {
#     "Customer":{
#         "validate":"irshad_demo.api.on_validate"
#     }
# }

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "irshad_demo",
# 		"logo": "/assets/irshad_demo/logo.png",
# 		"title": "irshad_demo",
# 		"route": "/irshad_demo",
# 		"has_permission": "irshad_demo.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/irshad_demo/css/irshad_demo.css"
# app_include_js = "/assets/irshad_demo/js/irshad_demo.js"

# include js, css files in header of web template
# web_include_css = "/assets/irshad_demo/css/irshad_demo.css"
# web_include_js = "/assets/irshad_demo/js/irshad_demo.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "irshad_demo/public/scss/website"

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
# app_include_icons = "irshad_demo/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "irshad_demo.utils.jinja_methods",
# 	"filters": "irshad_demo.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "irshad_demo.install.before_install"
# after_install = "irshad_demo.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "irshad_demo.uninstall.before_uninstall"
# after_uninstall = "irshad_demo.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "irshad_demo.utils.before_app_install"
# after_app_install = "irshad_demo.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "irshad_demo.utils.before_app_uninstall"
# after_app_uninstall = "irshad_demo.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "irshad_demo.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

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
# 		"irshad_demo.tasks.all"
# 	],
# 	"daily": [
# 		"irshad_demo.tasks.daily"
# 	],
# 	"hourly": [
# 		"irshad_demo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"irshad_demo.tasks.weekly"
# 	],
# 	"monthly": [
# 		"irshad_demo.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "irshad_demo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "irshad_demo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "irshad_demo.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["irshad_demo.utils.before_request"]
# after_request = ["irshad_demo.utils.after_request"]

# Job Events
# ----------
# before_job = ["irshad_demo.utils.before_job"]
# after_job = ["irshad_demo.utils.after_job"]

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
# 	"irshad_demo.auth.validate"
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

