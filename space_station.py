import space_api
import geocoder

# # http://iss.astroviewer.net/

class SpaceStation:

    def location(self):
        data = space_api.retrieve_space_data()

        # Challenge: Where is the space station passing overhead right now?
        #            Return a string such as "Chicago, Illinois, United States of America"

    def names(self):
        '''
        Return a list of the names of the people in space right now.
        '''
        data = space_api.retrieve_space_data()

        names = []
        for person in data['people']:
            names.append(person['name'])

        return names
