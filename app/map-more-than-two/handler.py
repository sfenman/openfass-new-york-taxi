import json
import requests


def send_to_reducer(quarters):
    url = 'http://gateway.openfaas:8080/function/reduce-count-quarter'
    requests_data = json.dumps(quarters)
    response = requests.post(url, data=requests_data)
    return response


def handle(req):
    json_req = json.loads(req)
    result = []
    for route in json_req:
        if route['passenger_count'] > 2:
            result.append(route)
    reducer_response = send_to_reducer(result)
    response = reducer_response.json()

    return json.dumps(response)
