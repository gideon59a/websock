import eventlet
import socketio
# import time

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('my_message', {'srv_message': 'on connect'}, sid)


@sio.event
def my_message(sid, data):
    print('message ', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.event
def my_response(sid, data):
    print(f'response from client {sid}: {data}')



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
