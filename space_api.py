# https://gist.github.com/JeffCohen/c8693203198cc94b64a3db36e736d622
# https://docs.python.org/3/howto/urllib2.html
# http://api.open-notify.org/astros.json

# This code works.  Run it to verify.

import urllib.request
import json

astros_url = "http://api.open-notify.org/astros.json"
location_url = "http://api.open-notify.org/iss-now.json"

def retrieve_space_data():
    '''
    Return a dictionary of space station data.
    '''

    with urllib.request.urlopen(astros_url) as response:
        data = json.loads(response.read().decode('utf8'))

    with urllib.request.urlopen(location_url) as response:
        location_data = json.loads(response.read().decode('utf8'))

    data['position'] = location_data['iss_position']

    return data
