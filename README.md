
Programs in this repo:

## Answering one-time questions on Citibike status 

**citibike.py**
- stand alone program that answers a question " What % of citibike docks have bikes in them?" at the time when the program is run.

## Importing Citibike data into the database 

**citibike_csv.py**
- downloads citibike data (https://feeds.citibikenyc.com/stations/stations.json) and creates csv on local computer

**csv_to_sql.py**
- imports csv file created by citibike_csv.py into sqlite database

### Run order:
1. citibike_csv.py
2. csv_to_sql.py