#!/usr/bin/env python

import sqlite3
import csv
import sys


# with open(sys.stdin()) as csv_file: # Open the csv data file
csv_data = sys.stdin.read().splitlines()
#next(csv_data, None)  # Skip the header row

sql = sqlite3.connect('citibike_db2')
cur = sql.cursor()

# Create the table if it doesn't already exist
cur.execute(' ' ' CREATE TABLE IF NOT EXISTS citibikes_status (ExecutionTime text, id text, stationName text, availableDocks integer, totalDocks integer, latitude real, longitude real, statusValue text, statusKey text, availableBikes integer, stAddress1 text, stAddress2 text, city text, postalCode text, location text, altitude text, testStation text, lastCommunicationTime text, landmark text)''') 
cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS station_time on citibikes_status (ExecutionTime, id)")

reader = csv.reader(csv_data)
next(reader, None)
for row in reader:
#	print(row)
#	break
	cur.execute("INSERT OR IGNORE INTO citibikes_status VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
sql.commit()
sql.close()