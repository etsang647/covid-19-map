from urllib.request import urlopen
from io import StringIO
import csv

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'

data = urlopen(url).read().decode('ascii', 'ignore')
datafile = StringIO(data)
cr = csv.reader(datafile)

for row in cr:
  if (row[1] == "US"):
    print(row)