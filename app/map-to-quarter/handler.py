import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

# Museum of Arts and Design central point = longitude = 40.78388391263626, latitude = -73.9655459024013
ZERO_POINT = {"lat": 40.78388391263626, "lon": -73.9655459024013}


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
    reducer_response = send_to_mapper(result)
    response = reducer_response.json()

    return json.dumps(response)
