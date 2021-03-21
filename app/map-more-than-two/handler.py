import json
import redis
import logging

logging.basicConfig(level=logging.DEBUG)

def send_to_redis(quarters):
    try:
        r = redis.StrictRedis(host="openfaas-redis-master", port=6379, charset="utf-8", decode_responses=True)
        data = json.dumps(quarters)
        r.set('two_pass', data)
    except Exception as e:
        print(e)

def handle(req):
    json_req = json.loads(req)
    result = []
    for route in json_req:
        if route['passenger_count'] > 2:
            result.append(route)
    reducer_response = send_to_redis(result)
    # response = reducer_response.json()
    # return json.dumps(response)
    return
