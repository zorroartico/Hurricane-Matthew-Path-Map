# Refactored file for longitude.

import csv

filename = 'hurrmatthew.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
		
	longitudes = []
	for column in reader:
		longitude = int(float(column[6]))
		longitudes.append(longitude)
		

		

