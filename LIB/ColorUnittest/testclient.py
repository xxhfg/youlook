#!/usr/bin/env python
# coding:utf-8
#
# Copyright 2009 CoderZh.com.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'CoderZh'


import tornado.ioloop
import unittest
import mimetypes

import tornado.httpclient
import tornado.ioloop

TEST_PORT = 8989


def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


class Client:

    def handle_request(self, response):
        self.response = response
        tornado.ioloop.IOLoop.instance().stop()

    def get(self, url):
        url = 'http://127.0.0.1:%s%s' % (TEST_PORT, url)
        request = tornado.httpclient.HTTPRequest(url=url,
                                                 method='GET',
                                                 )

        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(request, self.handle_request)
        tornado.ioloop.IOLoop.instance().start()

        return Response(self.response.code, self.response.body)

    def post(self, url, data={}):
        url = 'http://127.0.0.1:%s%s' % (TEST_PORT, url)
        fields = []
        files = []
        for key, value in data.items():
            if isinstance(value, file):
                files.append([key, value.name, value.read()])
            else:
                fields.append([key, value])

        content_type, body = encode_multipart_formdata(fields, files)
        headers = {'Content-Type': content_type}

        request = tornado.httpclient.HTTPRequest(url=url,
                                                 method='POST',
                                                 headers=headers,
                                                 body=body)

        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(request, self.handle_request)
        tornado.ioloop.IOLoop.instance().start()

        return Response(self.response.code, self.response.body)


class TestCase(unittest.TestCase):
    def _pre_setup(self):
        pass

    def _post_teardown(self):
        pass

    def __call__(self, result=None):
        """
        Wrapper around default __call__ method to perform My test
        set up. This means that user-defined Test Cases aren't required to
        include a call to super().setUp().
        """
        self.client = Client()
        try:
            self._pre_setup()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            import sys
            result.addError(self, sys.exc_info())
            return
        super(TestCase, self).__call__(result)
        try:
            self._post_teardown()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            import sys
            result.addError(self, sys.exc_info())
            return


if __name__ == '__main__':
    filename = 'd:\\temp\\test.txt'
    file = open(filename)
    print encode_multipart_formdata([('a', '1'), ('b', '2')], [('File', 'd:\\temp\\test.txt', file.read())])
