import json
import logging

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
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    for route in json_req["list"]:
        if is_in_quarter(QUARTER_ONE, route):
            result.append({"quarter": 'q1', "ocurance": 1})
        elif is_in_quarter(QUARTER_TWO, route):
            result.append({"quarter": 'q2', "ocurance": 1})
        elif is_in_quarter(QUARTER_THREE, route):
            result.append({"quarter": 'q3', "ocurance": 1})
        elif is_in_quarter(QUARTER_FOUR, route):
            result.append({"quarter": 'q4', "ocurance": 1})
    # send to reducer
    result = {"list": result}
    result = json.dumps(result)
    # return result
