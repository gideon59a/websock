# A flask_socketio based synchronous server

# Ref: https://flask-socketio.readthedocs.io/en/latest/ using the already working client
# Ref (works ok): https://pythonprogramminglanguage.com/python-flask-websocket/
# NOTE:
# The server fails until I downgraded flask-socketio to 4.3.2 per https://github.com/miguelgrinberg/Flask-SocketIO/issues/1432
#       C:\Python\Python39\Scripts\pip.exe install -Iv flask-socketio==4.3.2

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, namespace

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')  # for web based client to load its entry page, whic currently doesn't exist
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return {"status": "looks connected"}

# Socketio events
#=================

@socketio.on('connect')
def test_connect():
    emit('my_message', {'srv_message': 'on connect to a flask_socketio server'})
    print(f' request.sid: {request.sid}')   # https://stackoverflow.com/questions/39423646/flask-socketio-emit-to-specific-user
    msg = 'on connect, to the sid ' + request.sid
    emit('my_message', {'srv_message': msg}, room=request.sid)

    # The next one is for the web client. The message key must be "data".
    emit('after web connect', {'data': 'Lets dance'})

@socketio.on('message')  # built-in event
def handle_message(data):
    print('received message: ' + data)

@socketio.on('json')  # built-in event
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my_response')
def handle_my_custom_event(json):
    print('received from client: ' + str(json))

@socketio.on('client_response')
def client_response(data):
    print(f'response from client {request.sid}: {data}')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5003)
