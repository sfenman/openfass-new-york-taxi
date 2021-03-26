import json
import logging
import redis

logging.basicConfig(level=logging.DEBUG)


def call_redis(key):
    r = redis.StrictRedis(host="openfaas-redis-master", port=6379, charset="utf-8", decode_responses=True)
    #r = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True)
    result = r.get(key)
    if result is None:
        result = {'north_east': 0, 'north_west': 0, 'south_east': 0, 'south_west': 0}
        result = json.dumps(result)
    return json.loads(result)


def send_to_redis(quarters):
    try:
        r = redis.StrictRedis(host="openfaas-redis-master", port=6379, charset="utf-8", decode_responses=True)
        data = json.dumps(quarters)
        r.set('routes', data)
    except Exception as e:
        print(e)


def handle(req):
    data = json.loads(req)
    response = call_redis('routes')
    north_east_counter = response['north_east']
    north_west_counter = response['north_west']
    south_east_counter = response['south_east']
    south_west_counter = response['south_west']
    for route in data:
        if route["quarter"] == "north_east":
            north_east_counter += route["occurrence"]
        elif route["quarter"] == "north_west":
            north_west_counter += route["occurrence"]
        elif route["quarter"] == "south_east":
            south_east_counter += route["occurrence"]
        elif route["quarter"] == "south_west":
            south_west_counter += route["occurrence"]
    counts = {"north_east": north_east_counter, "north_west": north_west_counter,
              "south_east": south_east_counter, "south_west": south_west_counter}
    send_to_redis(counts)
    return json.dumps(counts)
