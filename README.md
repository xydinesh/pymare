# pymare
Python SDK for MARE.

```
from mare.components import Location, Vehicle
from mare.matrix import Request

# set apikey using MARE_KEY environment variable
# export MARE_KEY='abcxxxxxx'
request = Request()
# define locations
locations = []
a = Location(lat=33.937244, lon=-84.36947)
locations.append(a)
b = Location(lat=33.8875767, lon=-84.2613857)
locations.append(b)
c = Location(lat=33.8968108, lon=-84.3276536)
locations.append(c)
d = Location(lat=33.8730743, lon=-84.3951042)
locations.append(d)

# add locations to the request
request.add_locations(locations=locations)

# define vehicle type and add to request
car = Vehicle(v='car')
request.add_vehicle(vehicle=car)

# send request
response = request.send()
print (response)
```


