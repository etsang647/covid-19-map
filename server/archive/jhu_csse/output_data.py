from urllib.request import urlopen
from contextlib import closing
from io import StringIO
import csv
import json

# input files
# GitHub raw CSV links from JHU CSSE
CONFIRMED_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
DEATHS_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
RECOVERED_CSV_INPUT = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

# output files as JSON
CONFIRMED_JSON_OUTPUT = './data/confirmed.json'
DEATHS_JSON_OUTPUT = './data/deaths.json'
RECOVERED_JSON_OUTPUT = './data/recovered.json'

NUM_ROWS = None  # number of rows in each CSV (identical)

# calculate NUM_ROWS
with closing(urlopen(CONFIRMED_CSV_INPUT)) as csvfile:
  data = csvfile.read().decode('ascii', 'ignore')
  datafile = StringIO(data)
  csv_reader = csv.reader(datafile)

  NUM_ROWS = sum(1 for row in csv_reader)
  NUM_ROWS -= 1  # subtract header row from total

# generates confirmed.json
#
# reads data from CSV file located at URL CONFIRMED_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects stored in the file CONFIRMED_JSON_OUTPUT
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
        jsonfile.write(',\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1

# generates deaths.json
#
# reads data from CSV file located at URL DEATHS_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects stored in the file DEATHS_JSON_OUTPUT
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
        jsonfile.write(',\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1

# generates recovered.json
#
# reads data from CSV file located at URL RECOVERED_CSV_INPUT
# and outputs the number of confirmed cases by date for all US states
# as a list of JSON objects stored in the file RECOVERED_JSON_OUTPUT
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
        jsonfile.write(',\n')

      if line_count == NUM_ROWS - 1:
        jsonfile.write(']\n')

      line_count += 1
