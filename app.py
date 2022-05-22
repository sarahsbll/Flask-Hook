from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		print("Data received from Webhook is: ", request.json)
		with open("webhooked.json", "a") as outfile:
			json.dump(request.get_json(), outfile)
		return "Webhook received!"
