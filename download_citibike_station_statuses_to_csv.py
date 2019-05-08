#!/usr/bin/env python
import requests 
import json 
import sys
import csv
import logging

# configure logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

# Get the data from citibikenyc and change it into json 
try:
	r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
	logging.info("Got stations data feed from https://feeds.citibikenyc.com/stations/stations.json")

except HTTPError as http_err:
	logging.info (f'HTTP error occurred: {http_err}')  

except Exception as err:
	logging.info(f'Other error occurred: {err}')  

bikes = r.json()
logging.info("Converted json into dictionary")


def write_csv(fieldnames, data):
	
	# Write a csv from citibike stations app json and feed it to standard out

	writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
	writer.writeheader()
	for station in data:
		station.update({"ExecutionTime": bikes["executionTime"]})
		writer.writerow(station)

data = bikes["stationBeanList"]
fieldnames = ["ExecutionTime","id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1","stAddress2","city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark"]

write_csv(fieldnames, data)
logging.info("Finished writing csv")