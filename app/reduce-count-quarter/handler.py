import json

def handle(req):
    q1_counter = 0
    q2_counter = 0
    q3_counter = 0
    q3_counter = 0
    q4_counter = 0
    data = json.loads(req)
    for route in data['list']: 
        if route['quarter'] == "q1":
            q1_counter += route['ocurance']
        elif route['quarter'] == "q2":
            q2_counter += route['ocurance']
        elif route['quarter'] == "q3":
            q3_counter += route['ocurance']
        elif route['quarter'] == "q4":
            q4_counter += route['ocurance']
    return(q1_counter, q2_counter, q3_counter, q4_counter)
