from flask import Blueprint, jsonify, request

from ..service.wifi_service import get_wifinetworks_service
from ..utils.data_validator import validate_device_data
from ..auth.auth_guard import auth_guard

wifi = Blueprint("wifi", __name__)


@wifi.route("/", methods=["GET"])
@auth_guard()
def get_wifinetworks():
    return get_wifinetworks_service()
