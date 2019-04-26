import random
import string
import json

class Location(object):

    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon
        self.location_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) 

    def __repr__(self):
        return json.dumps(self.__dict__)


class Vehicle(object):

    def __init__(self, v):
        self.type = v

    def __repr__(self):
        return json.dumps(self.__dict__)


