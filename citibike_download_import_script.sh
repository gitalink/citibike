
#!/usr/bin/env bash

TIMESTAMP=$(date "+%Y%m%d-%H%M")

echo "creating timestamp" 
echo "timestamp = $TIMESTAMP"

echo "downloading citibike statuses and saving to csv"
python ./download_citibike_station_statuses_to_csv.py > ./citibike_statuses_$TIMESTAMP.csv

echo "reading csv records into db"
cat ./citibike_statuses_$TIMESTAMP.csv | python ./import_citibike_station_statuses_csv_to_sqlite_db.py >> import_log.csv