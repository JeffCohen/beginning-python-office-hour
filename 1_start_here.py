# bit.ly/beginningpy
# https://docs.python.org/3/howto/urllib2.html

import urllib.request
import json

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as response:
    data = response.read().decode('utf8')

# Challenge: Can you display the names of the people onboard the space station?
