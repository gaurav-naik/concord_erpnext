# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "concord_erpnext"
app_title = "Concord ERPNext"
app_publisher = "Gaurav Naik"
app_description = "ERPNext customization for Concord Transport"
app_icon = "fa fa-truck"
app_color = "#da261d"
app_email = "naik.gaurav.one@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/concord_erpnext/css/concord_erpnext.css"
# app_include_js = "/assets/concord_erpnext/js/concord_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/concord_erpnext/css/concord_erpnext.css"
# web_include_js = "/assets/concord_erpnext/js/concord_erpnext.js"

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
# get_website_user_home_page = "concord_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "concord_erpnext.install.before_install"
# after_install = "concord_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "concord_erpnext.notifications.get_notification_config"

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
# 		"concord_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"concord_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"concord_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"concord_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"concord_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "concord_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "concord_erpnext.event.get_events"
# }

