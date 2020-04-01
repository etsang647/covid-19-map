from urllib.request import urlopen
from contextlib import closing
from io import StringIO
from collections import defaultdict
import csv
import json

# NYT GitHub repo link
DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'

# reads CSV data from DATA_URL and returns it as a nicely formatted dict
def get_data_nyt():
  with closing(urlopen(DATA_URL)) as csv_file:

    # make csv_file more workable
    data = csv_file.read().decode('ascii', 'ignore')
    data_file = StringIO(data)
    dict_reader = csv.DictReader(data_file)

    # initialize empty nested dicts for later formatting
    dates_object = defaultdict(dict)

    # format data according to this structure:
    #
    # "2020-03-30": {
    #   "Washington": {
    #     "cases": 100,
    #     "deaths": 10
    #   },
    #   "New York": {
    #     "cases": 200,
    #     "deaths": 20
    #   },
    # },
    # "2020-03-31": { ... }
    #
    for row in dict_reader:
      date = row['date']
      name = row['state']
      cases = row['cases']
      deaths = row['deaths']

      state_object = {'cases': int(cases), 'deaths': int(deaths)}
      dates_object[date][name] = state_object

  return {'dates': dates_object}

if __name__ == "__main__":
  get_data_nyt()
