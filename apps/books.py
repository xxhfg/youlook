#!/usr/bin/env python
# coding: utf8

import tornado


class BooksIndexHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "world")
        self.set_header("Content-Type", "text/plain")
        self.finish("Hello %s!" % name)

handlers = [
    (r"/", BooksIndexHandler),
]
