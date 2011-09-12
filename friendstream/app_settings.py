# -*- coding: utf-8 -*-

import os

postgresql_connection_info = {
    'user': 'emre',
    'pass': 'emre',
    'name': 'friendstream',
    'host': 'localhost',
}

template_path=os.path.join(os.path.dirname(__file__), "templates")
static_path=os.path.join(os.path.dirname(__file__), "static")
xsrf_cookies=True
autoescape="xhtml_escape"
debug = True
