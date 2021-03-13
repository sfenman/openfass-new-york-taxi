import json
import requests

QUARTER_ONE = {
    "minLat": 40.0000000000000,
    "maxLat": 42.0000000000000,
    "minLon": -72.0000000000000,
    "maxLon": -70.0000000000000,
}

QUARTER_TWO = {
    "minLat": 40.0000000000000,
    "maxLat": 42.0000000000000,
    "minLon": -74.0000000000000,
    "maxLon": -72.0000000000000,
}

QUARTER_THREE = {
    "minLat": 42.0000000000000,
    "maxLat": 44.0000000000000,
    "minLon": -74.0000000000000,
    "maxLon": -72.0000000000000,
}

QUARTER_FOUR = {
    "minLat": 42.0000000000000,
    "maxLat": 44.0000000000000,
    "minLon": -72.0000000000000,
    "maxLon": -70.0000000000000,
}


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


def send_to_mapper(quarters):
    url = 'https://openfaas-ingress-billk97.cloud.okteto.net/function/reduce-count-quarter'
    requests_data = json.dumps(quarters)
    response = requests.post(url, data=requests_data)
    return response


def handle(req):
    json_req = json.loads(req)
    result = []
    for route in json_req:
        if is_in_quarter(QUARTER_ONE, route):
            result.append({"quarter": 'q1', "ocurance": 1})
        elif is_in_quarter(QUARTER_TWO, route):
            result.append({"quarter": 'q2', "ocurance": 1})
        elif is_in_quarter(QUARTER_THREE, route):
            result.append({"quarter": 'q3', "ocurance": 1})
        elif is_in_quarter(QUARTER_FOUR, route):
            result.append({"quarter": 'q4', "ocurance": 1})

    reducer_response = send_to_mapper(result)
    response = reducer_response.json()

    return json.dumps(response)
