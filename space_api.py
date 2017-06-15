# Intro to unit testing in Python 3
# http://bit.ly/begpy

import urllib.request
import json

# import unittest
# from unittest.mock import Mock


class SpaceAPI:

    def get_astronaut_data(self):
        astros_url = "http://api.open-notify.org/astros.json"
        with urllib.request.urlopen(astros_url) as response:
            return json.loads(response.read().decode('utf8'))

    def get_names_of_astronauts(self):
        data = self.get_astronaut_data()
        return [person['name'] for person in data['people']]

    def get_location_data(self):
        location_url = "http://api.open-notify.org/iss-now.json"
        with urllib.request.urlopen(location_url) as response:
            location_data = json.loads(response.read().decode('utf8'))

        return location_data['iss_position']


if __name__ == '__main__':
    api = SpaceAPI()
    print(api.get_names_of_astronauts())
