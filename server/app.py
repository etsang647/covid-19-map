from flask import Flask, jsonify, request
from flask_cors import CORS
from get_data import *


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def message():
  res_obj = {}
#   req_data = request.get_json()
#   name = req_data.get('name')
#   date = req_data.get('date')
  res_obj['amount'] = get_confirmed('Massachusetts', '3/19/20')
  return jsonify(res_obj)


if __name__ == '__main__':
  app.run()
