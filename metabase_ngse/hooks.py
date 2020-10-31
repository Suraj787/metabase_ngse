# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "metabase_ngse"
app_title = "Metabase Ngse"
app_publisher = "firsterp"
app_description = "Metabase for Nandan GSE"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@firsterp.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/metabase_ngse/css/metabase_ngse.css"
# app_include_js = "/assets/metabase_ngse/js/metabase_ngse.js"

# include js, css files in header of web template
# web_include_css = "/assets/metabase_ngse/css/metabase_ngse.css"
# web_include_js = "/assets/metabase_ngse/js/metabase_ngse.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "metabase_ngse.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "metabase_ngse.install.before_install"
# after_install = "metabase_ngse.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "metabase_ngse.notifications.get_notification_config"

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
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"metabase_ngse.tasks.all"
# 	],
# 	"daily": [
# 		"metabase_ngse.tasks.daily"
# 	],
# 	"hourly": [
# 		"metabase_ngse.tasks.hourly"
# 	],
# 	"weekly": [
# 		"metabase_ngse.tasks.weekly"
# 	]
# 	"monthly": [
# 		"metabase_ngse.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "metabase_ngse.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "metabase_ngse.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "metabase_ngse.task.get_dashboard_data"
# }

