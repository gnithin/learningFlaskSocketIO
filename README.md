# Socket-io trial

Trying out a basic socket-io based app using flask.

### References -
* https://flask-socketio.readthedocs.org/en/latest/
* http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent

### Troubleshooting 
* During `pip install flask-socketio`, there is an error that pops up - `import error. Error importing 'Python.h'`. This can be solved by installing the python-dev package - `apt-get install python-dev`(It's about 50MB)
