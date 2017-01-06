# Flask-WebSocket


copyright: (c) 2017 by Damon Chen.
license: BSD, see LICENSE for more details.

simple websocket for Flask

## Install

pip install flask-websocket


## Usage

you must define message with the follow message if you use on decorator:

```
{
    "event": event for listen
    "data": the event happend with dtaa
}
```



```python

from flask import Flask
from flask_websocket import WebSocket

app = Flask(__name__)
ws = WebSocket(app)

@ws.on('click')
def click(data):
    print(data)


```


or you could process raw message by yourself.


```python
from flask import Flask
from flask_websocket import WebSocket

app = Flask(__name__)
ws = WebSocket(app)


@ws.on_raw_message
def raw_message_handler(message):
    print(message)


```
