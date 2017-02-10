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

	number = number[2:]
	message_body= message_body.strip()

	if message_body == "?":
		help_message = """Text this number with a request saying something like: "How can I get from LOCATION A to LOCATION B" and we will help you find your way."""

		send_sms(help_message, number)
	else:
		status, origin, destination = string_location_parsing(message_body)

		if status == 2:
			if origin == None and destination == None:
				error_message = "Sorry, I couldn't find either of your specified locations. Please also include which cities they are in! "
			elif origin == None:
				error_message = "Sorry, I couldn't find your current location. Please also include which city it is in! "
			else:
				error_message = "Sorry, I couldn't find your destination location. Please also include which city it is in! "
			
			send_sms(error_message.strip(), number)

		elif status == 1:
			error_message = """Sorry, I couldn't understand your request. Please make sure to format it as follows: "How can I get from YOUR CURRENT LOCATION to YOUR DESTINATION." """

			send_sms(error_message.strip(), number)

		else:
			directions = get_directions_from_maps(origin, destination)
			directions_message = ""
			for each_step in directions:
				if len(directions_message+each_step) > 160:
					send_sms(directions_message.strip(), number)
					directions_message = each_step
				else:
					directions_message += each_step

	resp = twiml.Response()
	return str(resp)

if __name__ == "__main__":
	app.run()

