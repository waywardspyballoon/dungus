from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I'm a stupid robot!!1!</p>"
