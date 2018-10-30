Programs in this repo:

## Answering one-time questions on Citibike status 

**calculate_share_of_citibike_docs_with_bikes.py**
- stand alone program that answers a question " What % of citibike docks have bikes in them?" at the time when the program is run.

## Importing Citibike data into the database 

**download_citibike_station_statuses_to_csv.py**
- downloads citibike data (https://feeds.citibikenyc.com/stations/stations.json) and creates csv on local computer

**import_citibike_station_statuses_csv_to_sqlite_db.py**
- imports csv file created by citibike_csv.py into sqlite database

### Run order:
1. download_citibike_station_statuses_to_csv.py
2. import_citibike_station_statuses_csv_to_sqlite_db.py

### Prerequisites 

* sqlite

* Python3+ packages:
	* requests
	* json
	* csv
	* sqlite3

