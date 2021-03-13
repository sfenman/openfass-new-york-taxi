import csv
import logging
import json

def handle(event, context):
    data = event.request.files['file'].read()
    logging.critical(data)
    logging.critical(type(data))
    data = data.decode("utf-8")
    logging.critical(type(data))
    logging.critical(data.splitlines()[0].split(',')[1])
    lines = data.splitlines()
    lines.pop(0)
    routes = []
    for line in lines:
        values = line.split(',')
        logging.warning(values)
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
    return {
        "statusCode": 200,
        "body": json.dumps(routes)

    }
