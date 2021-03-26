import csv
import time
import requests
from termcolor import colored
from datetime import datetime


def make_to_csv(routes):
    with open('temp.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(routes)


def send_batch():
    response = requests.post('http://localhost:8080/function/csv-to-json-http-q2', files={'file': open('temp.csv', 'r')})
    print(colored(response.text, 'green'))


with open('/home/billk97/Downloads/fares.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    csv_reader=csv_reader
    count = 0
    batch = []
    for row in csv_reader:
        count += 1
        batch.append(row)
        if count == 100:
            now = datetime.now()
            info = 'Info: Sending 100 batch time: ' + now.strftime("%H:%M:%S")
            print(info)
            make_to_csv(batch)
            send_batch()
            count = 0
            batch = []
            time.sleep(5)
