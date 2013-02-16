#!/usr/bin/python
# -*- coding: UTF-8 -*-


from config import *
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options


class Application(tornado.web.Application):
    def __init__(self):
        # from poweredsites.urls import handlers, sub_handlers, ui_modules

        handlers.append((r"/", MainHandler))
        super(Application, self).__init__(handlers, **settings)

        # add handlers for sub domains
        # for sub_handler in sub_handlers:
            # host pattern and handlers
            # self.add_handlers(sub_handler[0], sub_handler[1])


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def main():
    tornado.options.parse_command_line()
    # application = tornado.web.Application([
        # (r"/", MainHandler),
    # ])
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
