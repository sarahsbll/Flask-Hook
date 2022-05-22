from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		with open("test.txt", "w") as outfile:
			outfile.write("test")
			outfile.close()
		return "Webhook received!"
