Due to a python-socketio bug (client showing "socketio.exceptions.BadNamespaceError: / is not a connected namespace")
which is a bug mentioned in https://github.com/miguelgrinberg/python-socketio/issues/634,
I have to downgrade (instead of download the fix from github):
PS C:\python-env\websock> .\Scripts\pip.exe install -Iv  python-socketio==4.6.1
which required also (looking at https://github.com/miguelgrinberg/Flask-SocketIO/issues/1432):
PS C:\python-env\websock> .\Scripts\pip.exe install --upgrade flask-socketio==4.3.2


