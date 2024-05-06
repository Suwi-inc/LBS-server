from flask import Blueprint, jsonify, request

from ..service.wifi_service import get_wifinetworks_service
from ..utils.data_validator import validate_request_data

wifi = Blueprint("wifi", __name__)


@wifi.route("/", methods=["GET"])
def get_wifinetworks():
    data = request.get_json()

    if not validate_request_data(data):
        return jsonify({"No Access": "Unauthorized device"}), 401

    return get_wifinetworks_service()
