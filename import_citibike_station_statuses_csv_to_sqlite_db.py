#!/usr/bin/env python

import sqlite3
import csv
import sys

with sqlite3.connect('citibike_db2') as sql:
  cur = sql.cursor()

  # Create the table if it doesn't already exist and create unique index
  cur.execute(' ' ' CREATE TABLE IF NOT EXISTS citibikes_status (ExecutionTime text, id text, stationName text, availableDocks integer, totalDocks integer, latitude real, longitude real, statusValue text, statusKey text, availableBikes integer, stAddress1 text, stAddress2 text, city text, postalCode text, location text, altitude text, testStation text, lastCommunicationTime text, landmark text)''') 
  cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS station_time on citibikes_status (ExecutionTime, id)")

  reader = csv.reader(sys.stdin)
  next(reader, None) # Skip header
  for row in reader:
  	# print(row)
	  cur.execute("INSERT OR IGNORE INTO citibikes_status VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)