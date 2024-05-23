from flask import Blueprint, jsonify, request

from ..service.gsm_service import add_cell_towers_service, get_celltowers_service
from ..utils.data_validator import validate_cell_tower_data, validate_request_data

cell = Blueprint("cell", __name__)


@cell.route("/", methods=["GET"])
def get_celltowers():
    data = request.get_json()

    if not validate_request_data(data):
        return jsonify({"No Access": "Unauthorized device"}), 401

    return get_celltowers_service()


@cell.route("/", methods=["POST"])
def add_celltowers():
    data = request.get_json()

    try:
        validate_cell_tower_data(data)
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    return add_cell_towers_service(data)
