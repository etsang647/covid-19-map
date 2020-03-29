from urllib.request import urlopen
from contextlib import closing
from io import StringIO
from collections import defaultdict
import csv
import json

DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'

def get_data():
  with closing(urlopen(DATA_URL)) as csv_file:
    data = csv_file.read().decode('ascii', 'ignore')
    data_file = StringIO(data)
    dict_reader = csv.DictReader(data_file)

    dates_object = defaultdict(dict)

    for row in dict_reader:
      date = row['date']
      name = row['state']
      cases = row['cases']
      deaths = row['deaths']

      state_object = {'cases': cases, 'deaths': deaths}
      
      dates_object[date][name] = state_object

  return {'dates': dates_object}

if __name__ == "__main__":
  get_data()
