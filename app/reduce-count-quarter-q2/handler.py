import json
from .route import Route
import redis
import logging

logging.basicConfig(level=logging.DEBUG)


def convert_to_routes(response):
    routes = set()
    for line in response:
        temp = Route(line['id'], line['vendor_id'], line['pickup_datetime'], line['drop_off_datetime'],
                     line['passenger_count'], line['pickup_longitude'], line['pickup_latitude'],
                     line['drop_off_longitude'], line['drop_off_latitude'], line['store_and_fwd_flag']
                     )
        routes.add(temp)
    return routes


def call_redis(key):
    result = []
    r = redis.StrictRedis(host="openfaas-redis-master", port=6379, charset="utf-8", decode_responses=True)
    result = r.get(key)
    return json.loads(result)


def get_more_than_one_km_routes():
    response = call_redis('one_km')
    response = convert_to_routes(response)
    return response


def get_more_than_ten_min_routes():
    response = call_redis('ten_minutes')
    response = convert_to_routes(response)
    return response


def get_more_than_two_pass_routes():
    response = call_redis('two_pass')
    response = convert_to_routes(response)
    return response


def handle(req):
    # get previous results
    logging.debug("skata")
    one_km = get_more_than_one_km_routes()
    ten_min = get_more_than_ten_min_routes()
    two_pass = get_more_than_two_pass_routes()
    results = one_km & ten_min & two_pass
    results = list(results)
    # safe results
    return json.dumps(results, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)

