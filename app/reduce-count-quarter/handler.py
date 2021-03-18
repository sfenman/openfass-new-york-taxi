import json


def handle(req):
    north_east_counter = 0
    north_west_counter = 0
    south_east_counter = 0
    south_west_counter = 0
    data = json.loads(req)
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
    return json.dumps(counts)
