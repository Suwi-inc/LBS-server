from DataObjects import GSMCell, WiFiNetwork, IPAddress
from flask import Flask, jsonify, Response,request
app = Flask(__name__)

dummy_location = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "altitude": 10,
    "precision": 5,
    "altitude_precision": 2,
    "type": "GSM"
}
dummy_wifi = {
    "mac": "2CD02D56HYU",
    "signal_strength": -20,
    "age": 1750
}
dummy_cell = {
    "country_code": 7,
    "operator_id": 100,
    "cell_id": 99,
    "lac": 9900,
    "signal_strength": -20,
    "age": 800
}

@app.route("/")
def hello_world():
    return "<p>Main!</p>"

@app.route('/location', methods=['GET'])
def get_location():
    data = request.json
    if 'wifi_networks' not in data and 'gsm_cells' not in data and 'ip' not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    #location simuation
    location = dummy_location
    return jsonify({"Location": location}), 200

@app.route('/wifi', methods=['GET'])
def get_wifi():
    data = request.get_json()
    if 'device_id' not in data or 'jwt_token' not in data: # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401
    #get wifi data 
    wifi = dummy_wifi
    return jsonify({"device": data['device_id'],"wifi": wifi}), 200

@app.route('/celltowers', methods=['GET'])
def get_celltowers():
    data = request.get_json()
    if 'device_id' not in data or 'jwt_token' not in data: # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401
    #get cell data   
    cells = dummy_cell
    return jsonify({"device": data['device_id'],"Cells": cells}), 200

