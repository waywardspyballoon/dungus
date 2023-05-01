import config
import openai
import os
from pprint import pprint
from flask import Flask, request
import requests

openai.api_key = os.environ["OPENAI_API_KEY"]
app = Flask(__name__)

PROMPT = "you are a bot"
def get_completion(user_text):
    #[
    #   { "role": "system", "content": "You are a stupid bot." },
    #   { "role": "user", "content": "Hi what's up?" }
    # ]   
    global PROMPT
    messages = [
        { "role": "system", "content": PROMPT},
        { "role": "user", "content": user_text}
    ]
    completions = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.6,
                    frequency_penalty=0.6,
                    max_tokens=300,
                )
    
    response = completions["choices"][0]["message"]["content"]   
    return response


@app.route("/")
def hello_world():
    return "<p>I'm a stupid robot!!1!</p>"

@app.post("/api/bot")
def bot():
    data = request.get_json()
    pprint(data)
    if data["sender_type"] != "user":
        return 

    user_text = data["text"]
    bot_text = get_completion(user_text)
    r = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={"bot_id": os.environ["GROUPME_BOT_ID"], "text": bot_text},
    )
    return "ok"


