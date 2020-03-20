import json
import sys
import operator

CONFIRMED_JSON = './data/confirmed.json'
DEATHS_JSON = './data/deaths.json'
RECOVERED_JSON = './data/recovered.json'


def get_confirmed(name, date):
  with open(CONFIRMED_JSON) as file:
    data = json.load(file)
    for obj in data:
      if obj['Province/State'] == name:
        return obj[date]

# for binary search
# will migrate it to output_data.py
#
# def sort_confirmed():
#   with open(CONFIRMED_JSON) as input:
#     with open('./data/confirmed_sorted.json', 'w') as output:
#       data = json.load(input)
#       data.sort(key=operator.itemgetter('Province/State'))
#       json.dump(data, output)


# if __name__ == "__main__":
  # get_confirmed(sys.argv[1], sys.argv[2])
  # sort_confirmed()
