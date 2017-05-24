from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

def send_sms(msg, number):
	try:
		client = TwilioRestClient(account="AC42268174c5815f26cd5084406a48b7e5",
							  token="f1a3d61fe159f9e6876070a33bf2d648")

		client.messages.create(from_="(647) 691 3881",
						  to=number,
						  body=msg)

	except TwilioRestException as e:
		print e
