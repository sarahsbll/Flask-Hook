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
		json_object = json.dumps(request.get_json(), indent = 4)
		with open("webhooked.json", "w") as outfile:
			outfile.write(json_object)
			outfile.close()
		return "Webhook received!"
