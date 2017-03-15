import urllib.request
import urllib.parse
import json

# Chicago is located at 41.878114, -87.629798
# http://nominatim.openstreetmap.org/reverse/?format=json&lat=41.878114&lon=-87.629798&zoom=11

def get_location(lat, lng):
    '''
    Returns a string describing the location of a given lat/lng.

    Example: 41.878114, -87.629798 would return "Chicago, Illinois, United States of America"
    '''
    
    path = "http://nominatim.openstreetmap.org/reverse"
    params = urllib.parse.urlencode({'format': 'json', 'lat': lat, 'lon': lng, 'zoom': 11})
    url = "{0}/?{1}".format(path, params)

    with urllib.request.urlopen(url) as response:
        json_data = json.loads(response.read().decode('utf8'))

    if json_data.get("error"):
        return "Over the ocean somewhere"
    else:
        address = json_data["address"]
        city = address.get("city") or address.get("village")
        state = address.get("state")
        country = address.get("country")

        if city is not None:
            return "{0}, {1}, {2}".format(city, state, country)
        elif state is not None:
            return "{0}, {1}".format(state, country)
        else:
            return country
