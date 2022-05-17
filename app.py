from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Again!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
       #print("Data received from Webhook is: ", request.json)
	with open('webhook.json', 'w') as f:
    		f.write(request.json)
		f.close()
        return "Webhook received!"


