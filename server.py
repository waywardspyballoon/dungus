import config
import os
from flask import Flask, request
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I'm a stupid robot!!1!</p>"

@app.post("/api/bot")
def bot():
    data = request.get_json()
    if data["sender_type"] != "user":
        return 

    r = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={"bot_id": os.environ["GROUPME_BOT_ID"], "text": "hi"},
    )
    return { "data" : "ok"}


