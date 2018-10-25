#!/usr/bin/env python

import sqlite3
import csv

csv_file=open('citibikes_status.csv','r') # open the csv data file
next(csv_file, None) # skip the header row
reader = csv.reader(csv_file)

sql = sqlite3.connect('citibike_db2')
cur = sql.cursor()

# create the table if it doesn't already exist
cur.execute(' ' ' CREATE TABLE IF NOT EXISTS citibikes_status (ExecutionTime text, id text, stationName text, availableDocks integer, totalDocks integer, latitude real, longitude real, statusValue text, statusKey text, availableBikes integer, stAddress1 text, stAddress2 text, city text, postalCode text, location text, altitude text, testStation text, lastCommunicationTime text, landMark text)''') 

for row in reader:
	cur.execute("INSERT INTO citibikes_status VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
	
csv_file.close()
sql.commit()
sql.close()