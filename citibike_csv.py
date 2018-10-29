#!/usr/bin/env python
import requests 
import json 
import csv


# Get the data from citibikenyc and changes it into json 

r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
bikes = r.json()


# Add timestamp to every station record 

for station in bikes["stationBeanList"]:
	station.update({"ExecutionTime":bikes["executionTime"]})


def csv_writer(path, fieldnames, data):
	
	# Write a csv file from citibike stations app json.
	
	with open(path, "w", newline = "") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		for row in data:
			writer.writerow(row)

path = "citibikes_status.csv"
data = bikes["stationBeanList"]
fieldnames = ["ExecutionTime","id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1","stAddress2","city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark"]

csv_writer(path, fieldnames, data)