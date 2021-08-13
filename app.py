from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Big Whips! Try again? Please work?</p>"
