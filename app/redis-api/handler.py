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


def handle(event, context):
    req = json.loads(event.body)
    call_redis(req['key'])
    response = call_redis(req['key'])
    response = json.dumps(response)
    return {
        "statusCode": 200,
        "body": response,
        "headers": {"content-type": "application/json"}
    }


