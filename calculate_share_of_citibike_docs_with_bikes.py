#!/usr/bin/env python
import requests 
import json 

r = requests.get("https://feeds.citibikenyc.com/stations/stations.json")
bikes = r.json()

stations_list = bikes["stationBeanList"]

total_docks = 0
total_bikes = 0

for station in stations_list:
	total_docks += station["totalDocks"]
	total_bikes += station["availableBikes"]

share_docks_w_bikes = total_bikes / total_docks * 100

print("There are total of {} docks. There are {} available bikes.".format(total_docks, total_bikes))
print('%6.2f' % (share_docks_w_bikes) + "% of docks have bikes.")