from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "label": _("Dasboards"),
            "icon": "octicon octicon-briefcase",
            "items": [
				{
                    "type": "page",
                    "name": "metabase-dashboard",
                    "label": _("Metabase Dashboard"),
                    "description": _("Metabase Dashboard"),
                }
            ]
        }
	]