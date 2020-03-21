import json
import sys
from pull_data import LIST_OF_STATES

DATA_PATH = './data/'


def get_cases(date):
  json_file = DATA_PATH + date + '.json'
  with open(json_file) as file:
    data = json.load(file)
    state_cases = initialize_cases()
    state_classes = {}

    for obj in data:
      confirmed = obj['Confirmed']
      deaths = obj['Deaths']
      recovered = obj['Recovered']
      confirmed_cases = int(confirmed) if confirmed != '' else 0
      deaths_cases = int(deaths) if deaths != '' else 0
      recovered_cases = int(recovered) if recovered != '' else 0
      confirmed_class = determine_class(confirmed_cases)
      deaths_class = determine_class(deaths_cases)
      recovered_class = determine_class(recovered_cases)
      cases = {'confirmed': confirmed_cases,
               'deaths': deaths_cases, 'recovered': recovered_cases}
      classes = {'confirmed': confirmed_class, 'deaths': deaths_class, 'recovered': recovered_class}
      state_cases[obj['Province/State']] = cases
      state_classes[obj['Province/State']] = classes

    return {'cases': state_cases, 'classes': state_classes}


def initialize_cases():
  states = {}
  for state in LIST_OF_STATES:
    cases = {'confirmed': 0, 'deaths': 0, 'recovered': 0}
    states[state] = cases
  return states


def determine_class(number):
  class_str = None
  if number == 0:
    class_str = 'class-0'
  elif number >= 1 and number <= 5:
    class_str = 'class-1'
  elif number >= 6 and number <= 50:
    class_str = 'class-2'
  elif number >= 51 and number <= 100:
    class_str = 'class-3'
  elif number >= 101 and number <= 500:
    class_str = 'class-4'
  elif number >= 501 and number <= 1000:
    class_str = 'class-5'
  elif number >= 1001 and number <= 5000:
    class_str = 'class-6'
  else:
    class_str = 'class-7'
  return class_str


if __name__ == "__main__":
  # get_confirmed(sys.argv[1], sys.argv[2])
  # sort_confirmed()
  get_cases(sys.argv[1])
