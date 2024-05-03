from flask import Flask,Blueprint, jsonify, Response,request
from ..model.models import WifiNetwork

wifi = Blueprint("wifi",__name__) 

dummy_location = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "altitude": 10,
    "precision": 5,
    "altitude_precision": 2,
    "type": "GSM"
}

@wifi.route('/location', methods=['GET'])
def get_location():
    data = request.json
    if 'wifi_networks' not in data and 'gsm_cells' not in data and 'ip' not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    #location simuation
    location = dummy_location
    return jsonify({"Location": location}), 200

@wifi.route('/', methods=['GET'])
def get_wifi():
    data = request.get_json()
    if 'device_id' not in data or 'jwt_token' not in data: # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401
    
    wifi_data = WifiNetwork.query.all()
    wifi_list = [{'id': wifi.id, 'mac': wifi.mac, 'signal_strength': wifi.signal_strength, 'age': wifi.age, 'location': wifi.location_id} for wifi in wifi_data]

    return jsonify({"device": data['device_id'], "wifi": wifi_list}), 200