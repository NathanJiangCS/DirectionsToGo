from flask import Flask, request, redirect
from twilio import twiml

#from send_sms_twilio import send_sms
from send_sms import send_sms 
from forwardGeocache import string_location_parsing
from getDirections import get_directions_from_maps


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']

	status, origin, destination = string_location_parsing(message_body)
	print status
	print origin
	print destination

	

	resp = twiml.Response()
	return str(resp)

if __name__ == "__main__":
	app.run()
    #send_sms("2am", '6475298960')
