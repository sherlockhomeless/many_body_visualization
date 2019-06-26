#!/usr/bin/python3
import csv
import json

# --- CONFIG ----
stars = 50


csvfile = open("simulation.csv")
fields = ["id","mass","x","y"]

reader = csv.DictReader(csvfile, fields)

list = []
for row in reader:
    list.append(row)

with open("simulation.json", "w", encoding="utf-8"
) as outfile:
    json.dump(list, outfile, ensure_ascii=False, indent=2)
