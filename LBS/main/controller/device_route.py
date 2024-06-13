from flask import Blueprint, jsonify, request

from ..auth.auth_guard import auth_guard
from ..service.device_service import add_device_service, auth_device_service
from ..utils.data_validator import validate_device_data

device = Blueprint("device", __name__)


@device.route("/register", methods=["POST"])
def add_device():
    # change device registration later checking that
    # only authentic devices are eligible for registration
    data = request.get_json()

    return add_device_service(data)


@device.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    if not validate_device_data(data):
        return jsonify({"Fail": "Missing credentails"}), 433
    return auth_device_service(data)
