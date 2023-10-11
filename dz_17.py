import json
import csv
import random

with open('dz_16.json') as file_1:
    data = json.load(file_1)
    with open('dz_17.csv', 'w') as file_2:
        writer = csv.writer(file_2)
        writer.writerow(['Number', 'Name', 'Age', 'Tel'])
        for key, item in data.items():
            row = [str(key), item[0], str(item[1]), random.randint(000000, 999999)]
            writer.writerow(row)
