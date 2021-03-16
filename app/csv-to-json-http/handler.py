import logging
import json
import requests
from datetime import datetime

def parse_csv(data):
    lines = data.splitlines()
    lines.pop(0)
    routes = []
    for line in lines:
        values = line.split(',')
        route = {
            'id': values[0],
            'vendor_id': values[1],
            'pickup_datetime': values[2],
            'passenger_count': values[3],
            'pickup_longitude': values[4],
            'pickup_latitude': values[5],
            'drop_off_longitude': values[6],
            'drop_off_latitude': values[7],
            'store_and_fwd_flag': values[8]
        }
        routes.append(route)
    return routes


def get_csv_data(event):
    csv_file = event.request.files['file'].read()
    csv_data = csv_file.decode("utf-8")
    return csv_data


def send_to_mapper(routes):
    url = 'http://gateway.openfaas:8080/function/map-to-quarter'
    routes = json.dumps(routes)
    response = requests.post(url, data=routes)
    logging.warning(response)
    return response


def is_date(string):
    try:
        datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False


def convert_datatipes(routes):
    for route in routes:
        if route['vendor_id'].isnumeric():
            route['vendor_id'] = int(route['vendor_id'])
        if route['passenger_count'].isnumeric():
            route['passenger_count'] = int(route['passenger_count'])
        route['pickup_longitude'] = float(route['pickup_longitude'])
        route['pickup_latitude'] = float(route['pickup_latitude'])
        route['drop_off_longitude'] = float(route['drop_off_longitude'])
        route['drop_off_latitude'] = float(route['drop_off_latitude'])
    return routes


def handle(event, context):
    csv_data = get_csv_data(event)
    routes = parse_csv(csv_data)
    routes = convert_datatipes(routes)
    response = send_to_mapper(routes)
    logging.warning(response.text)

    return {
        "statusCode": 200,
        "body": response.json(),
        "headers": {"content-type": "application/json"}
    }


