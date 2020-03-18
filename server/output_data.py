from urllib.request import urlopen
from contextlib import closing
from io import StringIO
import csv, json

CONFIRMED_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
DEATHS_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
RECOVERED_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

CONFIRMED_JSON_OUTPUT = './data/confirmed.json'
DEATHS_JSON_OUTPUT = './data/deaths.json'
RECOVERED_JSON_OUTPUT = './data/recovered.json'

NUM_ROWS = None
LAST_US_ROW = None

# evaluate NUM_ROWS and LAST_US_ROW
with closing(urlopen(CONFIRMED_CSV_INPUT)) as csvfile:
  data = csvfile.read().decode('ascii', 'ignore')
  datafile = StringIO(data)
  dict_reader = csv.DictReader(datafile)
  total_rows = 0
  last_us_row = 0

  for row in dict_reader:
    if row['Country/Region'] == 'US':
      last_us_row = total_rows
    total_rows += 1

  NUM_ROWS = total_rows
  LAST_US_ROW = last_us_row

# generates confirmed.json
#
# reads data from CSV file located at the URL CONFIRMED_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects, stored in the file at CONFIRMED_JSON_OUTPUT
with closing(urlopen(CONFIRMED_CSV_INPUT)) as csvfile:
  with open(CONFIRMED_JSON_OUTPUT, 'w') as jsonfile:
    data = csvfile.read().decode('ascii', 'ignore')
    datafile = StringIO(data)
    dict_reader = csv.DictReader(datafile)
    line_count = 0

    for row in dict_reader:
      if line_count == 0:
        jsonfile.write('[\n')

      if row['Country/Region'] == 'US':
        json.dump(row, jsonfile)

        # append commas where necessary
        if line_count < LAST_US_ROW - 1:
          jsonfile.write(',')

        jsonfile.write('\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1

# generates deaths.json
#
# reads data from CSV file located at the URL CONFIRMED_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects, stored in the file at CONFIRMED_JSON_OUTPUT
with closing(urlopen(DEATHS_CSV_INPUT)) as csvfile:
  with open(DEATHS_JSON_OUTPUT, 'w') as jsonfile:
    data = csvfile.read().decode('ascii', 'ignore')
    datafile = StringIO(data)
    dict_reader = csv.DictReader(datafile)
    line_count = 0

    for row in dict_reader:
      if line_count == 0:
        jsonfile.write('[\n')

      if row['Country/Region'] == 'US':
        json.dump(row, jsonfile)

        # append commas where necessary
        if line_count < LAST_US_ROW - 1:
          jsonfile.write(',')
          
        jsonfile.write('\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1

# generates recovered.json
#
# reads data from CSV file located at the URL CONFIRMED_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects, stored in the file at CONFIRMED_JSON_OUTPUT
with closing(urlopen(RECOVERED_CSV_INPUT)) as csvfile:
  with open(RECOVERED_JSON_OUTPUT, 'w') as jsonfile:
    data = csvfile.read().decode('ascii', 'ignore')
    datafile = StringIO(data)
    dict_reader = csv.DictReader(datafile)
    line_count = 0

    for row in dict_reader:
      if line_count == 0:
        jsonfile.write('[\n')

      if row['Country/Region'] == 'US':
        json.dump(row, jsonfile)

        # append commas where necessary
        if line_count < LAST_US_ROW - 1:
          jsonfile.write(',')
          
        jsonfile.write('\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1
