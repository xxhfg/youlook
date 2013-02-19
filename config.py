#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import libs

import tornado
import tornado.web
from tornado.options import define, options


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "static"),

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, type=bool)
define("xsrf_cookies", default=True, type=bool)
define("cookie_secret", '')
define("login_url", '/login')
define("static_url_prefix", '/static/')
define("template_path", os.path.join(os.path.dirname(__file__),
                                     "templates"))
define("static_path", os.path.join(os.path.dirname(__file__),
                                   "static"))
