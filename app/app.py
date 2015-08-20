from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/chat")
def index():
    return render_template("index.html")


@socketio.on("event")
def test_connect():
    pass

@socketio.on_error("event")
def error_event(e):
    pass

@socketio.on_error_default
def default_err_handler(e):
    pass

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
    print "asas"
