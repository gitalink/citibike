#!/usr/bin/env python

import sqlite3
import csv

with open('citibikes_status.csv','r') as csv_file: # Open the csv data file
	next(csv_file, None)  # Skip the header row
	reader = csv.reader(csv_file)

	sql = sqlite3.connect('citibike_db2')
	cur = sql.cursor()

	# Create the table if it doesn't already exist
	cur.execute(' ' ' CREATE TABLE IF NOT EXISTS citibikes_status (ExecutionTime text, id text, stationName text, availableDocks integer, totalDocks integer, latitude real, longitude real, statusValue text, statusKey text, availableBikes integer, stAddress1 text, stAddress2 text, city text, postalCode text, location text, altitude text, testStation text, lastCommunicationTime text, landMark text)''') 
	cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS station_time on citibikes_status (ExecutionTime, id)")
	
	for row in reader:
		cur.execute("INSERT OR IGNORE INTO citibikes_status VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
sql.commit()
sql.close()