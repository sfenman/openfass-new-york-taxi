import json

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


def handle(req):
    result = []
    json_req = json.loads(req)
    for route in json_req["list"]:
        if is_in_quarter(QUARTER_ONE, route):
            result.append({'q1', 1})
        elif is_in_quarter(QUARTER_TWO, route):
            result.append({'q2', 1})
        elif is_in_quarter(QUARTER_THREE, route):
            result.append({'q3', 1})
        elif is_in_quarter(QUARTER_FOUR, route):
            result.append({'q4', 1})
    # send to reducer
    return result