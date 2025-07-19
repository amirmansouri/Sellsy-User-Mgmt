app_name = "sellsy_user_mgmt"
app_title = "Sellsy User Mgmt"
app_publisher = "amirmansouri.dev@gmail.com"
app_description = "Sellsy User Mgmt"
app_email = "amirmansouri.dev@gmail.com"
app_license = "mit"

# Apps
# ------------------
fixtures = [
    {
        "dt": "DocType",
        "filters": [["name", "=", "Utilisateurs"]]
    }
]

doc_events = {
    "Utilisateurs": {
        "on_submit": "sellsy_user_mgmt.sellsy_user_mgmt.sellsy_user_mgmt.doctype.utilisateurs.utilisateurs.create_or_update_user"
    }
}

doctype_js = {
    "Utilisateurs": "public/js/utilisateurs.js"
}


# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sellsy_user_mgmt",
# 		"logo": "/assets/sellsy_user_mgmt/logo.png",
# 		"title": "Sellsy User Mgmt",
# 		"route": "/sellsy_user_mgmt",
# 		"has_permission": "sellsy_user_mgmt.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sellsy_user_mgmt/css/sellsy_user_mgmt.css"
# app_include_js = "/assets/sellsy_user_mgmt/js/sellsy_user_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/sellsy_user_mgmt/css/sellsy_user_mgmt.css"
# web_include_js = "/assets/sellsy_user_mgmt/js/sellsy_user_mgmt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sellsy_user_mgmt/public/scss/website"

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
# app_include_icons = "sellsy_user_mgmt/public/icons.svg"

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
# 	"methods": "sellsy_user_mgmt.utils.jinja_methods",
# 	"filters": "sellsy_user_mgmt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sellsy_user_mgmt.install.before_install"
# after_install = "sellsy_user_mgmt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sellsy_user_mgmt.uninstall.before_uninstall"
# after_uninstall = "sellsy_user_mgmt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sellsy_user_mgmt.utils.before_app_install"
# after_app_install = "sellsy_user_mgmt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sellsy_user_mgmt.utils.before_app_uninstall"
# after_app_uninstall = "sellsy_user_mgmt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sellsy_user_mgmt.notifications.get_notification_config"

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
# 		"sellsy_user_mgmt.tasks.all"
# 	],
# 	"daily": [
# 		"sellsy_user_mgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"sellsy_user_mgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sellsy_user_mgmt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sellsy_user_mgmt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sellsy_user_mgmt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sellsy_user_mgmt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sellsy_user_mgmt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sellsy_user_mgmt.utils.before_request"]
# after_request = ["sellsy_user_mgmt.utils.after_request"]

# Job Events
# ----------
# before_job = ["sellsy_user_mgmt.utils.before_job"]
# after_job = ["sellsy_user_mgmt.utils.after_job"]

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
# 	"sellsy_user_mgmt.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

