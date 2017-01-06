# -*- coding: utf-8 -*-
"""
    flask_websocket.py
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by Damon Chen.
    :license: BSD, see LICENSE for more details.
"""

import json
from collections import defaultdict
from flask import request, current_app as app


class WebSocket(object):
    def __init__(self, app=None):
        self.app = app
        self.event_handlers = defaultdict(list)
        self.raw_message_handler = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        url = app.config.get('WEBSOCKET_URL', '/ws')

        @app.route(url)
        def ws():
            socket = request.environ.get('wsgi.websocket')
            if socket is not None:
                while True:
                    message = socket.receive()
                    if not message:
                        break

                    self.dispatch_message(message)

    def on(self, event):
        def decorator(handler):
            # add to current event handler
            self.event_handlers[event].append(handler)
            return handler

        return decorator

    def on_raw_message(self):
        def decorator(handler):
            self.raw_message_handler = handler
            return handler

        return decorator

    def dispatch(self, event, *args, **kwargs):
        for handler in self.event_handlers[event]:
            handler(*args, **kwargs)

    def dispatch_message(self, message):
        if self.raw_message_handler is not None:
            self.raw_message_handler(message)
        else:
            try:
                msg = json.loads(message)
            except Exception as e:
                app.logger.error(e)
            else:
                event = msg.get('event')
                self.dispatch(event, msg.get('data'))
            finally:
                pass

