# Refactored file for latitude.

import csv

filename = 'hurrmatthew.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
		
	latitudes = []
	for column in reader:
		latitude = int(float(column[5]))
		latitudes.append(latitude)
		

	

	
