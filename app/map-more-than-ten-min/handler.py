import json
import requests
import redis
from datetime import datetime
from datetime import timedelta

def send_to_redis(quarters):
    try:
        r = redis.StrictRedis(host="openfaas-redis-master", port=6379, charset="utf-8", decode_responses=True)
        data = json.dumps(quarters)
        r.set('ten_minutes', data)
    except Exception as e:
        print(e)

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
    reducer_response = send_to_redis(routes)
    # response = reducer_response.json()
    # return json.dumps(response)
    return
