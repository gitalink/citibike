#!/usr/bin/env python
import requests 
import json 
import csv


# Get the data from citibikenyc and change it into json 

r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
bikes = r.json()


def write_csv(path, fieldnames, data):
	
	# Write a csv file from citibike stations app json.
	
	with open(path, "w", newline = "") as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		for station in data:
			station.update({"ExecutionTime":bikes["executionTime"]})
			writer.writerow(station)

path = "citibikes_status.csv"
data = bikes["stationBeanList"]
fieldnames = ["ExecutionTime","id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1","stAddress2","city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark"]

write_csv(path, fieldnames, data)