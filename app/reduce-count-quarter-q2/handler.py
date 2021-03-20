import json
from .route import Route
import redis


def convert_to_routes(response):
    routes = set()
    for line in response:
        # route_id = line['id']
        # del line['id']
        # line['route_id'] = route_id
        # temp = RouteSchema().load(line)
        temp = Route(line['id'], line['vendor_id'], line['pickup_datetime'], line['drop_off_datetime'],
                     line['passenger_count'], line['pickup_longitude'], line['pickup_latitude'],
                     line['drop_off_longitude'], line['drop_off_latitude'], line['store_and_fwd_flag']
                     )
        routes.add(temp)
    return routes


def call_redis(key):
    result = []
    r = redis.Redis(host='localhost', port=6379, db=0)
    result = r.get(key)
    # type(result)
    return result

    # with open('test.json') as json_file:
    #     routes = json_file.read()
    #     result = json.loads(routes)
    # return result


def get_more_than_one_km_routes():
    response = call_redis('key')
    response = convert_to_routes(response)
    return response


def get_more_than_ten_min_routes():
    response = call_redis('key')
    response = convert_to_routes(response)
    return response


def get_more_than_two_pass_routes():
    response = call_redis('key')
    response = convert_to_routes(response)
    return response


def handle(req):
    one_km = get_more_than_one_km_routes()
    ten_min = get_more_than_ten_min_routes()
    twp_pass = get_more_than_two_pass_routes()
    results = one_km & ten_min & twp_pass
    results = list(results)
    return json.dumps(results, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
