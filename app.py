from flask import Flask, request
import dropbox
import json

# using an access token
dbx = dropbox.Dropbox('sl.BKTIgucHvPwW2PFw5C0w69AgcPtsX-F1W18iEZaMTUK48CGfXDI3iZzpgN-uqDrgwUx56oQO1mqqQevzvkH6HtY827GlN86y2ZB_-mE8oXW9oUSc2DonjcHwzDC9gXu742vfoF5DIkfL')

app = Flask(__name__)
@app.route("/")
def index():
        return "Hello World!"


@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		#print("Data received from Webhook is: ", request.json)
		li.append(request.get_json())
		#print(li)
		dbx.files_upload(bytes(str(li), 'UTF-8'), '/Python/sample.json')

		return "Webhook received!"








