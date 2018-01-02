# Refactored file for wind speed.

import csv

filename = 'hurrmatthew.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	wind_speeds = []
	for column in reader:
		wind_speed = int(float(column[7]))
		wind_speeds.append(wind_speed)
	

