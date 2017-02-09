import requests

"""

string_location_parsing takes a string parameter and returns 2 strings.

It takes the body of the SMS and parses it to extract the start
and end location of the user. If one or both of the locations could
not be determined, it will return an empty string for that location.

Currently, it can only handle "A to B" format strings.

"""

def string_location_parsing(string):

	start_location = None
	end_location = None

	#Handling "How can I get from A to B"
	if "to" in string:
		to_index = string.index("to")

		start_location = string[:to_index]
		end_location = string[to_index + 2:]


	if start_location and end_location:
		forward_geocaching(start_location, end_location)	
"""
		start_location, end_location = 
		return start_location, end_location

	else:
		if start_location == None and end_location == None:
			return "", ""
		elif start_location == None:
			return "", end_location
		else:
			return start_location, ""
"""


def forward_geocaching(loc1, loc2):
	try:
		loc1_data = {"scantext": loc1, "json":1}
		loc2_data = {"scantext": loc2, "json":1}

		resp1 = requests.post("http://geocoder.ca", loc1_data)
		resp2 = requests.post("http://geocoder.ca", loc2_data)

		print resp1.json()
		print resp2.json()

		start_data = resp1.json()
		end_data = resp2.json()
#
#		start_pos = start_data['match']
#		end_pos = end_data['match']
#
#		print start_data
#		print type(start_pos)
#
#		print end_data
#		print type(end_pos)

	except Exception as e:
		print e

string_location_parsing("How do I get from 330 metcalfe ottawa to hsdff")