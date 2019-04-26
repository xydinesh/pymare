import random
import string
import json

class Location(object):

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) 

    def __str__(self):
        return json.dumps({
            "location_id": self.id,
            "latitude": self.lat,
            "longitude": self.lon
        })
