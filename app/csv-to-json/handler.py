import requests
import csv

def handle(req):
    result = {"found": False}
    csv_file = csv.reader(req, delimiter = ",")
    lines = 0
    responce = []
    for row in csv_file:
        lines +=1
        responce.append(row)
    return (csv_file)
