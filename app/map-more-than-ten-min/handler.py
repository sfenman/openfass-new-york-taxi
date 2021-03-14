import json
import requests
from datetime import datetime
from datetime import timedelta


def send_to_reducer(quarters):
    url = 'https://openfaas-ingress-billk97.cloud.okteto.net/function/reduce-count-quarter'
    requests_data = json.dumps(quarters)
    response = requests.post(url, data=requests_data)
    return response


def is_date(string):
    try:
        datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


def get_more_than_ten_minutes_routes(routes):
    ten_minutes = timedelta(minutes=10)
    result = []
    for route in routes:
        if not is_date(route['pickup_datetime']) or not is_date(route['drop_off_datetime']):
            continue
        else:
            drop = datetime.strptime(route['drop_off_datetime'], '%Y-%m-%d %H:%M:%S')
            pickup = datetime.strptime(route['pickup_datetime'], '%Y-%m-%d %H:%M:%S')
            if drop-pickup > ten_minutes:
                result.append(route)
    return result


def handle(req):
    json_req = json.loads(req)
    routes = get_more_than_ten_minutes_routes(json_req)
    reducer_response = send_to_reducer(routes)
    response = reducer_response.json()
    return json.dumps(response)
