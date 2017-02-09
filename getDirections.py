import googlemaps
from pprint import pprint
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
		start_string = start_location["latt"] + "," + start_location["longt"]
		end_string = end_location["latt"] + "," + end_location["longt"]

		directions_result = gmaps.directions(origin=start_string,
		                                     destination=end_string,
		                                     mode=transport_mode,
		                                     avoid=avoidances,
		                                     alternatives=False)

		make_it_readable( directions_result[0]["legs"][0])
		return 0
	except Exception as e:
		print e
		return 0

def make_it_readable(directions_json):
	

a = {u'city': u'Mississauga', u'confidence': u'0.72', u'latt': u'43.601854713', u'prov': u'ON', u'staddress': u'Tucana Crt', u'longt': u'-79.648150424', u'stnumber': u'4470'}
b = {u'city': u'Waterloo', u'confidence': u'0.81', u'latt': u'43.449835', u'prov': u'ON', u'staddress': u'University Ave W', u'longt': u'-80.543892', u'stnumber': {}}

print(get_directions_from_maps(a, b))
