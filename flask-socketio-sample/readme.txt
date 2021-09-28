An example for the flask-socketio based server and the asyncio base client (& future web java script based client).
The client should be async as it has both inputs from the server as well as from user keyboard/mouse.

Next step is authentication, as the websocket connection has to be related to the flask login.
Ref: https://flask-socketio.readthedocs.io/en/latest/implementation_notes.html#authentication that mentions that
flask-login has to be used:
"Flask-SocketIO can access login information maintained by Flask-Login. After a regular Flask-Login authentication is
 performed and the login_user() function is called to record the user in the user session, any SocketIO connections
 will have access to the current_user context variable.
 Note that the login_required decorator cannot be used with SocketIO event handlers,... "