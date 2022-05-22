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
		print("Data received from Webhook is: ", request.json)
		li.append(request.get_json())
		print(li)

		#diction.update(request.get_json())
		#print(diction)
		#with open("test2.json", "a") as outfile:
			#json.dump(diction, outfile)
		#json_object = json.dumps(request.get_json(), indent = 4)
		#with open("test.txt", "w") as outfile:            
                        #outfile.write("test")
                        #outfile.close()
		return "Webhook received!"






dbx.files_upload(bytes(str(li)[1:-1], 'UTF-8'), '/Python/sample8.text')

#with open("test3.json", "w") as f:
	#f.write(str(li))
	#f.close()










app = Flask(__name__)
@app.route("/")
def index():
	return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.method == 'POST':
		str_1 = "Join our freelance network"

		str_1_encoded = bytes(str_1,'UTF-8')

		dbx.files_upload(str_1_encoded, '/Python/test6.txt')

		return "Webhook received!"
