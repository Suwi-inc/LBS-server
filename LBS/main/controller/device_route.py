from flask import Blueprint, jsonify, request
import json
from ..service.device_service import add_device_service, auth_device_service
from ..utils.data_validator import validate_device_data
from ..utils.logger import log_action

from ..utils.data_objects import RouteInfo


device = Blueprint("device", __name__)


@device.route("/register", methods=["POST"])
def add_device():
    # change device registration later checking that
    # only authentic devices are eligible for registration
    data = request.get_json()
    route = RouteInfo(request.path, request.method)

    return add_device_service(data, route)


@device.route("/auth", methods=["POST"])
def auth():
    data = json.loads(request.data.decode("utf-8").replace("json=", ""))
    route = RouteInfo(request.endpoint, request.method)
    try:
        validate_device_data(data)
    except (ValueError, TypeError) as e:
        log_action(
            __name__,
            str(e),
            route.endpoint,
            route.methods,
            data.get("serial_number"),
        )
        return jsonify({"error": str(e)}), 400

    return auth_device_service(data, route)
