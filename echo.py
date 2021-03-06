from flask import Flask


app = Flask(__name__)


@app.route("/")
def status():
    return "echo server! :D"


@app.route("/echo/<word>")
def echo(word):
    if app.caps:
        return word.upper()
    else:
        return word
