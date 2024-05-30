from flask import Blueprint, jsonify, request

from ..service.wifi_service import get_wifinetworks_service
from ..utils.data_validator import validate_device_data

wifi = Blueprint("wifi", __name__)


@wifi.route("/", methods=["GET"])
def get_wifinetworks():
    data = request.get_json()

    if not validate_device_data(data):
        return jsonify({"Fail": "Missing device data"}), 422

    return get_wifinetworks_service()
