import sys
import flask
from flask import Flask, request, jsonify

from services import viacep, location

app = Flask(__name__)

@app.route('/api/cep/<string:cep>', methods=['GET'])
def getCep(cep):
  detailed = request.args.get('detailed') or True
  address = viacep.fetch_address(cep)

  if not hasattr(address, 'error'):
    if detailed:
      coordinates = location.fetch_coordinates(address)

      if not hasattr(coordinates, 'error'):
        address['coordinates'] = coordinates
      
  return jsonify(address), address['status'] if hasattr(address, 'status') else 200

app.run()