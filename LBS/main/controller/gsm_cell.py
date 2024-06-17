from flask import Blueprint, jsonify, request
import json

from ..service.gsm_service import add_cell_towers_service, get_celltowers_service
from ..utils.data_validator import validate_cell_tower_data, validate_device_data
from ..auth.auth_guard import auth_guard
from ..utils.logger import log_action
from ..utils.data_objects import RouteInfo


cell = Blueprint("cell", __name__)


@cell.route("/", methods=["GET"])
@auth_guard()
def get_celltowers():

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

    log_action(
        __name__,
        "User requested to view cell towers",
        request.path,
        request.method,
        data.get("serial_number"),
        "info",
    )
    return get_celltowers_service()


@cell.route("/", methods=["POST"])
@auth_guard()
def add_celltowers():
    data = json.loads(request.data.decode("utf-8").replace("json=", ""))
    route = RouteInfo(request.path, request.method)

    try:
        validate_cell_tower_data(data)
    except (ValueError, TypeError) as e:
        log_action(
            __name__, str(e), route.endpoint, route.methods, data.get("serial_number")
        )
        return jsonify({"error": str(e)}), 400

    return add_cell_towers_service(data)
