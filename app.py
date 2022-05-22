from flask import Flask, request
import dropbox

#testdropbox
# using an access token
dbx = dropbox.Dropbox('sl.BIFVS2Po_OUNDI8q_DVraj12gqyKm4DrwwCenpc1Xy3Aq1hvzYwu5nBp8cevJ1Gt3nmctUc2J7J_kbQ0vrUU91G04dDVDptP81zr4OxSqUZgeTP2ZANOD68GAvOFQ8N0mCLlfGX2Wcb_')

str_1 = "Join our freelance network"

str_1_encoded = bytes(str_1,'UTF-8')

dbx.files_upload(str_1_encoded, '/Python/test.txt')





app = Flask(__name__)
@app.route("/")
def index():
	return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		return "Webhook received!"
