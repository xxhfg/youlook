#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import time
import libs
import apps


# from mytestclient import TestCase
from myunittest import MyTestRunner
import unittest

from tornado.escape import utf8
from tornado.httpclient import HTTPRequest, HTTPResponse, _RequestProxy
from tornado.iostream import IOStream
from tornado import netutil
from tornado.stack_context import ExceptionStackContext, NullContext
from tornado.testing import AsyncHTTPTestCase, bind_unused_port
from tornado.test.util import unittest
from tornado.util import u, bytes_type
from tornado.web import Application, RequestHandler, url

try:
    from io import BytesIO  # python 3
except ImportError:
    from cStringIO import StringIO as BytesIO

import books


class HelloWorldHandler(RequestHandler):
    def get(self):
        name = self.get_argument("name", "world")
        self.set_header("Content-Type", "text/plain")
        self.finish("Hello %s!" % name)


class HTTPClientCommonTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return Application([
            url("/hello", books.BooksIndexHandler),
            # url("/post", PostHandler),
            # url("/chunk", ChunkHandler),
            # url("/auth", AuthHandler),
            # url("/countdown/([0-9]+)", CountdownHandler, name="countdown"),
            # url("/echopost", EchoPostHandler),
            # url("/user_agent", UserAgentHandler),
            # url("/304_with_content_length", ContentLength304Handler),
        ], gzip=True)

    def test_hello_world(self):
        response = self.fetch("/hello")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/plain")
        self.assertEqual(response.body, b"Hello world!")
        self.assertEqual(int(response.request_time), 0)

        response = self.fetch("/hello?name=Ben")
        self.assertEqual(response.body, b"Hello Ben!")


if __name__ == "__main__":
    unittest.main(testRunner=MyTestRunner())
    # unittest.main()
