import requests
from Route import *
from RouteSchema import *

def handle(req):
    lines = req.read().splitlines()
    lines.pop(0)
    routes = []
    schema = RouteSchema()
    for line in lines:
        values = line.split(',')
        route = Route(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
        result = schema.load(route.__dict__)
        routes.append(result)
    return schema.dumps(routes, many=True)
