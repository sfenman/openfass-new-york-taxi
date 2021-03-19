import logging
import json
import requests
from datetime import datetime

def parse_csv(data):
    lines = data.splitlines()
    routes = []
    for line in lines:
        values = line.split(',')
        route = {
            'id': values[0],
            'vendor_id': values[1],
            'pickup_datetime': values[2],
            'drop_off_datetime': values[3],
            'passenger_count': values[4],
            'pickup_longitude': values[5],
            'pickup_latitude': values[6],
            'drop_off_longitude': values[7],
            'drop_off_latitude': values[8],
            'store_and_fwd_flag': values[9]
        }
        routes.append(route)
    return routes


def get_csv_data(event):
    csv_file = event.request.files['file'].read()
    csv_data = csv_file.decode("utf-8")
    return csv_data


def send_to_mapper(function, routes):
    logging.info("sending to %s", routes)
    url = 'http://gateway.openfaas:8080/function/' + function
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


def convert_data_types(routes):
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
    routes = convert_data_types(routes)
    response1 = send_to_mapper('map-more-than-ten-min', routes)
    response2 = send_to_mapper('map-more-than-two', routes)
    response3 = send_to_mapper('map-more-than-one-km', routes)
    logging.warning(response1.text)
    logging.warning(response2.text)
    logging.warning(response3.text)

    return {
        "statusCode": 200,
        "body": response1.json(),
        "headers": {"content-type": "application/json"}
    }



