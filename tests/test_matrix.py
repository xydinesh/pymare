import string
import pytest
from mare.components import Location, Vehicle
from mare.matrix import Request
from mare.error import InvalidValueError, MareKeyNotDefinedError

def test_locations():
    a = Location(lat=33.937244, lon=-84.36947)
    assert a.latitude == 33.937244
    assert a.longitude == -84.36947
    for l in a.location_id:
        assert l in (string.ascii_lowercase + string.digits)

def test_vehicle():
    v = Vehicle(v='car')
    assert v.type == 'car'

def test_matrix_request_locations():
    r = None
    with pytest.raises(MareKeyNotDefinedError):
        r = Request()

    r = Request(key='abc')
    with pytest.raises(InvalidValueError):
        r.add_locations(locations=None)
    locations = []
    a = Location(lat=33.937244, lon=-84.36947)
    locations.append(a)
    b = Location(lat=33.8875767, lon=-84.2613857)
    locations.append(b)
    c = Location(lat=33.8968108, lon=-84.3276536)
    locations.append(c)
    d = Location(lat=33.8730743, lon=-84.3951042)
    locations.append(d)
    r.add_locations(locations=locations)

def test_matrix_request_vehicle():
    r = Request(key='abc')
    with pytest.raises(InvalidValueError):
        r.add_vehicle(vehicle=None)
    car = Vehicle(v='car')
    r.add_vehicle(vehicle=car)

def test_matrix_request_send():
    r = Request()
    locations = []
    a = Location(lat=33.937244, lon=-84.36947)
    locations.append(a)
    b = Location(lat=33.8875767, lon=-84.2613857)
    locations.append(b)
    c = Location(lat=33.8968108, lon=-84.3276536)
    locations.append(c)
    d = Location(lat=33.8730743, lon=-84.3951042)
    locations.append(d)
    r.add_locations(locations=locations)
    car = Vehicle(v='car')
    r.add_vehicle(vehicle=car)
    response = r.send()
    assert response is not None


