from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Again!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
       #print("Data received from Webhook is: ", request.json)
	with open('webhook.json', 'w') as jf:
    		json.dump(request.json, jf)
	
        return "Webhook received!"


