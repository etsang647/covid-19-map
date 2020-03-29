from flask import Flask, jsonify, request
from flask_cors import CORS
from get_data_nyt import get_data

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['POST'])
def message():
  if request.method == 'POST':
    req_data = request.get_json()
  res_obj = get_data()
  return jsonify(res_obj)

if __name__ == '__main__':
  app.run()
