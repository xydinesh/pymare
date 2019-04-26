import os
import json
import requests
from .error import InvalidValueError, MareKeyNotDefinedError

class Request(object):
    def __init__(self, key=None):
        self.locations = []
        self.vehicle = None
        self.key = key
        self.endpoint = 'https://public-api.mapanything.io/mare/matrix'
        if self.key is None:
            self.key = os.environ.get('MARE_KEY', None)

        if self.key is None:
            raise MareKeyNotDefinedError('provide key with request object or MARE_KEY environment variable')
        self.headers = {'Content-Type': 'application/json', 'x-api-key': self.key}

    def __repr__(self):
        return json.dumps(self.__dict__)

    def add_vehicle(self, vehicle):
        if vehicle is None:
            raise InvalidValueError('vehicle can not be empty')
        self.vehicle = vehicle 

    def add_locations(self, locations):
        if locations is None:
            raise InvalidValueError('locations can not be empty')
        self.locations = locations

    def send(self):
        data = {}
        data['vehicle'] = self.vehicle.__dict__
        data['locations'] = [i.__dict__ for i in self.locations]
        response = requests.post(self.endpoint, headers=self.headers, data=json.dumps(data))
        if response.status_code != 200:
            raise InvalidRequestError('Did not receive a successful response for the request')
        return response.text
