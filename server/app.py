from flask import Flask, jsonify, request
from flask_cors import CORS
from get_data_nyt import get_data_nyt

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# MAIN ROUTE
# 
# sends the entirety of NYT state-level data in one go
# front-loaded response that allows for fast data retrieval on client side afterward
@app.route('/data', methods=['GET'])
def message():
  res_obj = {}
  if request.method == 'GET':
    res_obj = get_data_nyt()
  return jsonify(res_obj)

if __name__ == '__main__':
  app.run()
