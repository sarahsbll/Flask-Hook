from flask import Flask, request
import dropbox
import json

# using an access token
dbx = dropbox.Dropbox('sl.BIHXQMOID8C4j__clI2sqjyTAMYuAQZcHQKHdpZ3t41eHqsbQn4bjE2tPq68X3f7K0fgL-vaLx6iCqJNqvudHl9S3W6C3BMRujZAPhuBs6keEmtujAGFuSRPPPCIrH3_O2E8OEwLXRzK')



#diction = {}

li = []


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
		dbx.files_upload(bytes(str(li), 'UTF-8'), '/Python/sample11.json')

		return "Webhook received!"



#with open("test3.json", "w") as f:
	#f.write(str(li))
	#f.close()







