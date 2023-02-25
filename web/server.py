import logging
from flask import Flask, render_template
from uvicorn import Config, Server

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("status.html")

if __name__ == '__main__':
    config = Config(app, host='0.0.0.0', port=8000)
    server = Server(config)
    server.run()