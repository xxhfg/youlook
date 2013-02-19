#!/usr/bin/env python
# coding: utf8

import apps
import libs

import tornado
import tornado.web
from tornado.options import define, options
from config import *


handlers = [
    (r"/(favicon\.ico)", tornado.web.StaticFileHandler,
     dict(path=MEDIA_ROOT)),
    (r"/static/(.+)", tornado.web.StaticFileHandler,
     dict(path=MEDIA_ROOT, name='static_path')),
    (r"/media/(.+)", tornado.web.StaticFileHandler,
     dict(path=MEDIA_ROOT, name='media_path')),
]
# handlers.append(('.*', tornado.web.FallbackHandler,
                 # dict(fallback=WSGIContainer(WSGIHandler()))))
sub_handlers = []
ui_modules = {}
settings = dict(
    debug=options.debug,
    template_path=options.template_path,
    static_path=options.static_path,
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

from apps import books

handlers.extend(books.handlers)
