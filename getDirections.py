import googlemaps
import re
"""
get_directions_from_maps requests Google Maps API to get directions from one place
to another.

paramaters:
	start_location:<dictionary> - starting location
	end_location:<dictionary> - ending destination
	transport_mode:<string> - "driving", "walking", "bicycling", "transit" (default)
	avoidances:<string> - "tolls" (default), "highways", "ferries"

return:
	string containing directions to get to the destination
"""

API_KEY = 'AIzaSyAE6o3bNueg57_Ij5oK3oTqd40R0nac5No'

def get_directions_from_maps(start_location, end_location, transport_mode="transit", avoidances="tolls"):
	try:
		gmaps = googlemaps.Client(key=API_KEY)
		start_coordinates = start_location["latt"] + "," + start_location["longt"]
		end_coordinates = end_location["latt"] + "," + end_location["longt"]

		directions_result = gmaps.directions(origin=start_coordinates,
		                                     destination=end_coordinates,
		                                     mode=transport_mode,
		                                     avoid=avoidances,
		                                     alternatives=False)
		
		return make_it_readable(directions_result[0]["legs"][0])
			
	except Exception as e:
		print str(e)
		return 0

def make_it_readable(directions_json):
	#Time is calculated assuming same time zone
	departure_time = directions_json["departure_time"]["text"] 
	arrival_time = directions_json["arrival_time"]["text"]
	duration = directions_json["duration"]["text"]
	#Nice, readable string version of start and end address
	start_address = directions_json["start_address"]
	end_address = directions_json["end_address"]

	steps = []

	for unspecific_step in directions_json["steps"]:
		step_travel_mode = unspecific_step["travel_mode"]

		if step_travel_mode == "WALKING":

			if len(unspecific_step["steps"]) == 0 or len(unspecific_step["steps"]) == 1:
				html_instructions = re.sub(r'<.*?>', '', unspecific_step["html_instructions"])
				step_distance = unspecific_step["distance"]["text"]
				step_duration = unspecific_step["duration"]["text"]
				formatted_step = "{}. Walk for approximately {} ({})".format(html_instructions, 
																		   step_duration, 
																		   step_distance)
				print formatted_step
				steps.append(formatted_step)

			else:
				for each_step in unspecific_step["steps"]:
					html_instructions = re.sub(r'<.*?>', '', each_step["html_instructions"])
					step_distance = each_step["distance"]["text"]
					step_duration = each_step["duration"]["text"]
					formatted_step = "{}. Walk for approximately {} ({})".format(html_instructions, 
																			   step_duration, 
																			   step_distance)
					print formatted_step
					steps.append(formatted_step)

		elif step_travel_mode == "TRANSIT":
			transit_details = unspecific_step["transit_details"]
			#Details
			arrival_stop = transit_details["arrival_stop"]["name"]
			departure_stop = transit_details["departure_stop"]["name"]
			bus_arrival_time = transit_details["arrival_time"]["text"]
			bus_departure_time = transit_details["departure_time"]["text"]
			head_sign = transit_details["headsign"]
			line_name = transit_details["line"]["name"]
			short_name = transit_details["line"]["short_name"]

			formatted_step = """Head to {} to take the {} ({}) which arrives at {}. You will arrive at {} at approximately {}.""".format(departure_stop, head_sign, short_name, bus_departure_time, arrival_stop, bus_arrival_time)
			print formatted_step
			steps.append(formatted_step)

		elif step_travel_mode == "DRIVING":
			pass
		else: #Biking
			pass

	steps.append("You have arrived at your destination!")
			
	return steps

#a = {u'city': u'Mississauga', u'confidence': u'0.72', u'latt': u'43.601854713', u'prov': u'ON', u'staddress': u'Tucana Crt', u'longt': u'-79.648150424', u'stnumber': u'4470'}
#b = {u'city': u'Waterloo', u'confidence': u'0.81', u'latt': u'43.449835', u'prov': u'ON', u'staddress': u'University Ave W', u'longt': u'-80.543892', u'stnumber': {}}


