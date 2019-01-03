#!/usr/bin/env python
import requests 
import json 
import sys
import csv


# Get the data from citibikenyc and change it into json 

r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
bikes = r.json()


def write_csv(fieldnames, data):
	
	# Write a csv from citibike stations app json and feed it to standard out

	writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
	writer.writeheader()
	for station in data:
		station.update({"ExecutionTime":bikes["executionTime"]})
		writer.writerow(station)

data = bikes["stationBeanList"]
fieldnames = ["ExecutionTime","id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1","stAddress2","city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark"]

write_csv(fieldnames, data)