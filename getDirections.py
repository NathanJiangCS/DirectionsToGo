import googlemaps

"""
get_directions_from_maps requests Google Maps API to get directions from one place
to another.

paramaters:
	start_location:<string> - starting location
	end_location:<string> - ending destination
	transport_mode:<string> - "driving", "walking", "bicycling", "transit" (default)
	avoidances:<string> - "tolls" (default), "highways", "ferries"

return:
	json object containing directions to get to the destination
"""

API_KEY = 'AIzaSyAE6o3bNueg57_Ij5oK3oTqd40R0nac5No'

def get_directions_from_maps(start_location, end_location, transport_mode, avoidances):
	gmaps = googlemaps.Client(key=API_KEY)
	directions_result = gmaps.directions(origin=start_location,
	                                     destination=end_location,
	                                     mode=transport_mode,
	                                     avoid="tolls",
	                                     alternatives=False)

	return directions_result

