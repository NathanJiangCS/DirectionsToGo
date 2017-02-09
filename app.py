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

	if message_body == "help":
		help_message = """
						Hi, welcome to Directions to Go! Text this number with a request saying something like: 
						"How can I get from LOCATION A to LOCATION B" and we will help you find your way. When specifying
						either locations, please include which city they are in for best results. Additionally, you can 
						specify which method of transportation you wish to take including "transit", "driving", or "walking".
					   """

		send_sms(help_message, number)
	else:
		status, origin, destination = string_location_parsing(message_body)
		print status
		print origin
		print destination

		if status == 2:
			if origin == None and destination == None:
				error_message = "Sorry, I couldn't find either of your specified locations. Please also include which cities they are in! "
			elif origin == None:
				error_message = "Sorry, I couldn't find your current location. Please also include which city it is in! "
			else:
				error_message = "Sorry, I couldn't find your destination location. Please also include which city it is in! "
			
			send_sms(error_message, number)

		elif status == 1:
			error_message = """
							Sorry, I couldn't understand your request. Please make sure to format it as follows:
							"How can I get from YOUR CURRENT LOCATION to YOUR DESTINATION."
							"""

			send_sms(error_message, number)

		else:
			directions = get_directions_from_maps(origin, destination)

			send_sms(directions, number)


	resp = twiml.Response()
	return str(resp)

if __name__ == "__main__":
	app.run()
    #send_sms("2am", '6475298960')
