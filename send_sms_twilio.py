from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

def send_sms(msg, number):
	try:

		client.messages.create(from_="(647) 691 3881",
						  to=number,
						  body=msg)

	except TwilioRestException as e:
		print e
