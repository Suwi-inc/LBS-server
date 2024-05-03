from flask import Blueprint, jsonify, request

from ..model.models import GsmCell

cell = Blueprint("cell", __name__)


@cell.route("/", methods=["GET"])
def get_celltowers():
    data = request.get_json()
    if "device_id" not in data or "jwt_token" not in data:  # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401

    cell_data = GsmCell.query.all()
    cell_list = [
        {
            "id": cell.id,
            "country_code": cell.country_code,
            "operator_id": cell.operator_id,
            "cell_id": cell.cell_id,
            "lac": cell.lac,
            "signal_strength": cell.signal_strength,
            "age": cell.age,
        }
        for cell in cell_data
    ]

    return jsonify({"device": data["device_id"], "gsm": cell_list}), 200
