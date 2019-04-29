#!/usr/bin/env python

import sqlite3
import csv
import sys
import logging


# configure logging 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')


with sqlite3.connect('citibike_db2') as sql:
  cur = sql.cursor()
  logging.info("Opened DB Connection")

  # Create the table if it doesn't already exist
 
  try:
    cur.execute(' ' ' CREATE TABLE citibikes_status (ExecutionTime text, id text, stationName text, availableDocks integer, totalDocks integer, latitude real, longitude real, statusValue text, statusKey text, availableBikes integer, stAddress1 text, stAddress2 text, city text, postalCode text, location text, altitude text, testStation text, lastCommunicationTime text, landmark text)''') 
    logging.info("Created table citibikes_status")

  except sqlite3.OperationalError:  
    logging.info("Table citibikes_status exists")

  # Create unique index if it doesn't already exist

  try:
    cur.execute("CREATE UNIQUE INDEX station_time on citibikes_status (ExecutionTime, id)")
    logging.info("Created unique index on ExecutionTime and id fields")
  
  except sqlite3.OperationalError: 
    logging.info("Unique index on ExecutionTime and id exist")


  # Read iterable csv and insert into database 

  reader = csv.reader(sys.stdin)
  logging.info("Starting inserting rows")
  
  next(reader, None) # Skip header
  logging.info("Skipped header row") 
  
  for row in reader:
    try:
      cur.execute("INSERT INTO citibikes_status VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
      logging.info("Trying to insert row")

    except sqlite3.IntegrityError:
      logging.info("Ignored row. ExecutionTime and id unique index already exists")
  logging.info("Finished inserting rows")