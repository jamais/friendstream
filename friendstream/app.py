#!/usr/bin/env python

import tornado.options
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from handlers.index import IndexHandler

define('port', default=8888, help='run on the given port', type=int)

import app_settings

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
        ]
        settings = dict(
            postgresql_info = app_settings.postgresql_connection_info,
            cookie_secret   = "43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnpasd",
            template_path   = app_settings.template_path,
            static_path     = app_settings.static_path,
            autoescape      = app_settings.autoescape,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.debug = True
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()


