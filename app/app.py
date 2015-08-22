from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit
import logging

logging.basicConfig(
    filename="my_log.log",
    level=logging.DEBUG
)

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("event", namespace="/test")
def test_connect(msg):
    logging.debug("Received - " + msg)
    emit("event", "Hi client!")

@socketio.on_error_default
def default_err_handler(e):
    pass

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
