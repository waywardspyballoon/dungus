import config
import openai
import os
from pprint import pprint
from flask import Flask, request
import requests

openai.api_key = os.environ["OPENAI_API_KEY"]
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I'm a stupid robot!!1!</p>"

@app.post("/api/bot")
def bot():
    data = request.get_json()
    pprint(data)
    if data["sender_type"] != "user":
        return 

    r = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={"bot_id": os.environ["GROUPME_BOT_ID"], "text": "hi"},
    )
    return { "data" : "ok"}


