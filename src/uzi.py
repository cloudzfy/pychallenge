from calendar import isleap
from datetime import date

for year in range(1586, 1997, 10):
	if isleap(year) and date(year, 1, 26).weekday() == 0:
		print year
