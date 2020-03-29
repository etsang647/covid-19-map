from urllib.request import urlopen
from contextlib import closing
from io import StringIO
from datetime import date
from dates import get_dates
import csv, json

# incomplete link to the JHU CSSE COVID-19 repo
DATA_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

OUTPUT_PATH = './data/'

LAST_DAY = date(2020, 3, 21)

LIST_OF_STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","Washington, D.C.","West Virginia","Wisconsin","Wyoming"]

# reads CSV data from the JHU CSSE and outputs that data as local JSON
def pull_data():
  dates_list = get_dates(LAST_DAY)

  for date in dates_list:
    csv_url = DATA_URL + date + '.csv'
    json_file = OUTPUT_PATH + date + '.json'

    with closing(urlopen(csv_url)) as infile:
      with open(json_file, 'w') as outfile:

        data = infile.read().decode('ascii', 'ignore')
        datafile = StringIO(data)
        dict_reader = csv.DictReader(datafile)

        outfile.write('[\n')

        for row in dict_reader:
          # only write US states to output
          if row['Province/State'] in LIST_OF_STATES:
            outfile.write(json.dumps(row, indent=4))
            outfile.write(',\n')

        outfile.write(']\n')

if __name__ == "__main__":
  pull_data()
