from flask import Flask, request
import dropbox

#testdropbox
# using an access token
dbx = dropbox.Dropbox('sl.BIHXQMOID8C4j__clI2sqjyTAMYuAQZcHQKHdpZ3t41eHqsbQn4bjE2tPq68X3f7K0fgL-vaLx6iCqJNqvudHl9S3W6C3BMRujZAPhuBs6keEmtujAGFuSRPPPCIrH3_O2E8OEwLXRzK')


str_1 = "Join our freelance network"

str_1_encoded = bytes(str_1,'UTF-8')

dbx.files_upload(str_1_encoded, '/Python/test4.txt')





app = Flask(__name__)
@app.route("/")
def index():
	return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		return "Webhook received!"
