#!/usr/bin/env python
import requests 
import json 
import sys
import csv
import logging
from requests.exceptions import HTTPError

# configure logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

# Get the data from citibikenyc and change it into json 
try: 
	r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
	r.raise_for_status()
except HTTPError as http_err:
	logging.info(f'Not able to download data. HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
	logging.info(f'Other error occurred: {err}')  # Python 3.6


try:
	bikes = r.json()
	logging.info("Converted json into dictionary")

except json.decoder.JSONDecodeError:
	logging.info("Not able to convert json into dictionary. JSONDecodeError occurred")


def write_csv(fieldnames, data):
	
	# Write a csv from citibike stations app json and feed it to standard out

	writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
	writer.writeheader()
	for station in data:
		station.update({"ExecutionTime": bikes["executionTime"]})
		writer.writerow(station)
try:
	data = bikes["stationBeanList"]
except NameError:
	logging.info("Input dictionary is not defined")

fieldnames = ["ExecutionTime","id", "stationName", "availableDocks", "totalDocks", "latitude", "longitude", "statusValue", "statusKey", "availableBikes", "stAddress1","stAddress2","city", "postalCode", "location", "altitude", "testStation", "lastCommunicationTime", "landMark"]

try:
	write_csv(fieldnames, data)
	logging.info("CSV writer completed successfully")
except NameError:
	logging.info("Input data for write_csv function is not defined")
