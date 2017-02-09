import requests

"""

string_location_parsing takes the body of the SMS and parses it to extract the start
and end location of the user. Using this, it will call the forward_geocaching function
which will convert these two strings to valid addresses.

parameters:
	string:<string> - body of SMS

return: (All in a tuple)
	status:<int> - 0 if successful, 1 improper format, 2 couldn't find location
	start_pos:<dict> or None - dictionary containing start location 
							 - returns None if starting position cannot be found

	end_pos:<dict> or None - dictionary containing end location 
						   - returns None if ending position cannot be found

Currently, it can only handle "A to B" format strings.

"""

def string_location_parsing(string):

	start_substr = ""
	end_substr = ""

	#Handling "How can I get from A to B"
	if "to" in string:
		start_substr = string[:string.find("to")]
		end_substr = string[string.find("to")+2:]


	if len(start_substr) and len(end_substr):
		return forward_geocaching(start_substr, end_substr)

	else:
		return 1, None, None



def forward_geocaching(loc1, loc2):
	try:
		#json:1 configures the response to be in json format
		#country:canada gives a bias towards Canadian addresses
		loc1_data = {"scantext": loc1, "json":1, "country":"canada"}
		loc2_data = {"scantext": loc2, "json":1, "country":"canada"}

		resp1 = requests.post("http://geocoder.ca", loc1_data)
		resp2 = requests.post("http://geocoder.ca", loc2_data)
		resp1 = resp1.json()
		resp2 = resp2.json()

		if "match" in resp1:
			start_pos = resp1['match']
			#If there are multiple matches, the results will be in a list
			#Take the most confident result (at index 0)
			if type(start_pos) == list:
				start_pos = start_pos[0]

			#Check if the confidence in the geocoded location is greater than 0.5
			#if the location is less than 0.5, we assume that a location is not found
			if float(start_pos["confidence"]) > 0.5:
				status = 0
			else:
				status = 2
				start_pos = None
		else:
			status = 2
			start_pos = None


		if "match" in resp2:
			end_pos = resp2['match']
			#If there are multiple matches, the results will be in a list
			#Take the most confident result (at index 0)
			if type(end_pos) == list:
				end_pos = end_pos[0]
				
			#Check if the confidence in the geocoded location is greater than 0.5
			#if the location is less than 0.5, we assume that a location is not found
			if float(end_pos["confidence"]) > 0.5:
				status = 0
			else:
				status = 2
				end_pos = None
		else:
			status = 2
			end_pos = None

		return status, start_pos, end_pos

	except RequestException as e:
		print e
		return 1, None, None

