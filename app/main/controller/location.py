from flask import Blueprint, jsonify, request

location = Blueprint("location", __name__)

dummy_location = {"latitude": 40.7128, "longitude": -74.0060, "altitude": 10, "precision": 5, "altitude_precision": 2, "type": "GSM"}

@location.route("/", methods=["GET"])
def get_location():
    data = request.json
    if "wifi_networks" not in data and "gsm_cells" not in data and "ip" not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    # location simuation
    location = dummy_location
    return jsonify({"Location": location}), 200