import json
import math

import requests


def send_to_reducer(quarters):
    url = 'http://gateway.openfaas:8080/function/reduce-count-quarter'
    requests_data = json.dumps(quarters)
    response = requests.post(url, data=requests_data)
    return response


def is_more_than_one_km(route):
    lat1 = route['pickup_latitude']
    lon1 = route['pickup_longitude']
    lat2 = route['drop_off_latitude']
    lon2 = route['drop_off_longitude']
    EARTH_RADIUS_KM = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    a = math.sin(d_lat/2) * math.sin(d_lat/2) + math.sin(d_lon/2) * math.sin(d_lon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    print(EARTH_RADIUS_KM * c)
    return EARTH_RADIUS_KM * c > 1


def get_routes_longer_than_one_km(routes):
    long_routes = []
    for route in routes:
        if is_more_than_one_km(route):
            long_routes.append(route)
    return long_routes


def handle(req):
    json_req = json.loads(req)
    routes = get_routes_longer_than_one_km(json_req)
    reducer_response = send_to_reducer(routes)
    response = reducer_response.json()
    return json.dumps(response)
