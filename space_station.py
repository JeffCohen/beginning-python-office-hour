import space_api
import geocoder

# # http://iss.astroviewer.net/

class SpaceStation:

    def location(self):
        data = space_api.retrieve_space_data()

        # Challenge: Where is the space station passing overhead right now?
        #            This function should return a string
        #            such as "Chicago, Illinois, United States of America"
        #            (hint: use the geocoder module)

    def names(self):
        '''
        Returns a list of the names of the people in space right now.
        '''
        data = space_api.retrieve_space_data()

        names = []
        for person in data['people']:
            names.append(person['name'])

        # Challenge: Can you think of other ways to
        #            capture the list of names?
        
        return names
