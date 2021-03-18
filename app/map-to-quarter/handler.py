import json
import requests
import logging
# LON = HIGTH
# lat = width
# Museum of Arts and Design central point = longitude = 40.78388391263626, latitude = -73.9655459024013

# west_north longitude = 40.78260062447487, latitude = -73.9861651724389
NORTH_WEST = {
    "minLat": -80.0000000000000,
    "maxLat": -73.98189295225801,
    "minLon": 40.76769138282124,
    "maxLon": 45.0000000000000
}

NORTH_EAST = {
    "minLat": -73.98189295225801,
    "maxLat": -64.0000000000000,
    "minLon": 40.76769138282124,
    "maxLon": 45.0000000000000
}

SOUTH_WEST = {
    "minLat": -80.0000000000000,
    "maxLat": -73.98189295225801,
    "maxLon": 40.76769138282123,
    "minLon": 35.0000000000000
}

SOUTH_EAST = {
    "minLat": -80.0000000000000,
    "maxLat": -64.0000000000000,
    "maxLon": 40.76769138282123,
    "minLon": 35.0000000000000
}

ZERO_POINT = {"lat": 40.78388391263626, "lon": -73.9655459024013}

def is_in_quarter(quarter, route):

    if (
        route["pickup_longitude"] > quarter["maxLon"]
        or route["pickup_longitude"] < quarter["minLon"]
    ):
        return False
    if (
        route["pickup_latitude"] > quarter["maxLat"]
        or route["pickup_latitude"] < quarter["minLat"]
    ):
        return False
    return True


def is_in_quarter_two(route):
    if route["pickup_longitude"] > ZERO_POINT["lon"] and route["pickup_latitude"] > ZERO_POINT["lat"]:
        return 'north_east'
    if route["pickup_longitude"] > ZERO_POINT["lon"] and route["pickup_latitude"] < ZERO_POINT["lat"]:
        return 'north_west'
    if route["pickup_longitude"] < ZERO_POINT["lon"] and route["pickup_latitude"] > ZERO_POINT["lat"]:
        return 'south_east'
    if route["pickup_longitude"] < ZERO_POINT["lon"] and route["pickup_latitude"] < ZERO_POINT["lat"]:
        return 'south_west'


def send_to_mapper(quarters):
    url = 'http://gateway.openfaas:8080/function/reduce-count-quarter'
    requests_data = json.dumps(quarters)
    response = requests.post(url, data=requests_data)
    return response


def handle(req):
    json_req = json.loads(req)
    result = []
    for route in json_req:
        result.append({"quarter": is_in_quarter_two(route), "occurrence": 1})
        # if is_in_quarter(NORTH_WEST, route):
        #     result.append({"quarter": 'q1', "ocurance": 1})
        # elif is_in_quarter(NORTH_EAST, route):
        #     result.append({"quarter": 'q2', "ocurance": 1})
        # elif is_in_quarter(SOUTH_WEST, route):
        #     result.append({"quarter": 'q3', "ocurance": 1})
        # elif is_in_quarter(SOUTH_EAST, route):
        #     result.append({"quarter": 'q4', "ocurance": 1})

    reducer_response = send_to_mapper(result)
    response = reducer_response.json()

    return json.dumps(response)
