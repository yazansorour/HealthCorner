# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "health_corner"
app_title = "Health Corner"
app_publisher = "Yazan"
app_description = "Health Corner Services Mine"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "yazansorour1@gmail.com"
app_license = "MIT"

# Yazan edition
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/health_corner/css/health_corner.css"
# app_include_js = "/assets/health_corner/js/health_corner.js"

# include js, css files in header of web template
# web_include_css = "/assets/health_corner/css/health_corner.css"
# web_include_js = "/assets/health_corner/js/health_corner.js"

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
# get_website_user_home_page = "health_corner.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "health_corner.install.before_install"
# after_install = "health_corner.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "health_corner.notifications.get_notification_config"

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
# 		"health_corner.tasks.all"
# 	],
# 	"daily": [
# 		"health_corner.tasks.daily"
# 	],
# 	"hourly": [
# 		"health_corner.tasks.hourly"
# 	],
# 	"weekly": [
# 		"health_corner.tasks.weekly"
# 	]
# 	"monthly": [
# 		"health_corner.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "health_corner.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "health_corner.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "health_corner.task.get_dashboard_data"
# }

