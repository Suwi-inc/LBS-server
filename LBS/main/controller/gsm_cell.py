from flask import Blueprint, jsonify, request

from ..service.gsm_service import add_cell_towers_service, get_celltowers_service
from ..utils.data_validator import validate_cell_tower_data, validate_device_data
from ..auth.auth_guard import auth_guard
from ..utils.route_information import RouteInfo

cell = Blueprint("cell", __name__)


@cell.route("/", methods=["GET"])
@auth_guard()
def get_celltowers():

    return get_celltowers_service(RouteInfo(request.path, request.method))


@cell.route("/", methods=["POST"])
@auth_guard()
def add_celltowers():
    data = request.get_json()

    try:
        validate_cell_tower_data(data)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    return add_cell_towers_service(data)
