import json
import csv

arr = json.load(open("ONN-Vap-B-30dW-30dR_2020-12-01_2022-08-30.json"))

with open('Historical-ONN-Vap-B-30dW-30dR_2020-12-01_2022-08-30.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Close'])
    for pt in arr:
        vals = []
        vals.append(pt['isoInstant'])
        vals.append(pt['indexValue'])
        writer.writerow(vals)
