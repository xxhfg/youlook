#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
将LIB目录下引用包加入系统路径
"""

import  os
import sys

LIB_DIR = (os.path.join(os.curdir, 'LIB'))
sys.path.append(os.curdir)
sys.path.append(os.pardir)
sys.path.append(LIB_DIR)

dirs = [n for n in os.listdir(LIB_DIR) if
        os.path.isdir(os.path.join(LIB_DIR, n))]
for d in dirs:
    sys.path.append(os.path.join(LIB_DIR, d))

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

ui_modules = {}
settings = dict(
    debug=options.debug,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    # xsrf_cookies=options.xsrf_cookies,
    # cookie_secret=options.cookie_secret,
    # login_url=options.login_url,
    # static_url_prefix=options.static_url_prefix,

    ui_modules=ui_modules,

    # auth secret
    # twitter_consumer_key=options.twitter_consumer_key,
    # twitter_consumer_secret=options.twitter_consumer_secret,
    # friendfeed_consumer_key=options.friendfeed_consumer_key,
    # friendfeed_consumer_secret=options.friendfeed_consumer_secret,
    # facebook_api_key=options.facebook_api_key,
    # facebook_secret=options.facebook_secret,
)

handlers = [
    (r"/(favicon\.ico)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
    (r"/static/(.+)", tornado.web.StaticFileHandler,
     dict(path=MEDIA_ROOT, name='static_path')),
    (r"/media/(.+)", tornado.web.StaticFileHandler,
     dict(path=MEDIA_ROOT, name='media_path')),
]
# handlers.append(('.*', tornado.web.FallbackHandler,
                 # dict(fallback=WSGIContainer(WSGIHandler()))))
# handlers = []
sub_handlers = []
