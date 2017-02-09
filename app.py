from flask import Flask, request, redirect
from twilio import twiml

from send_sms import send_sms


app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']

	resp = twiml.Response()

	resp.message("Hi this is a test")

    incoming_number = request.values.get('From', None)
    print incoming_number

    return str(resp)

if __name__ == "__main__":
	app.run()
    #send_sms("2am", '6475298960')
