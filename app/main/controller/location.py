import math
from typing import List, Tuple

from flask import Blueprint, jsonify, request

from .. import db
from ..model.models import GsmCell

location = Blueprint("location", __name__)

dummy_location = {"latitude": 40.7128, "longitude": -74.0060, "altitude": 10, "precision": 5, "altitude_precision": 2, "type": "GSM"}


# https://ieeexplore.ieee.org/abstract/document/7456592
# Has multiple flaws:
# 1. Does not account for the fact that all the math is happening on spheroid
# 2. Does not account for the fact that signal strength may not correlate with real position
#    (1 tower may be blocked by an iron sheet, while others are not)
# 3. Does not account for altitude at all
# 4. Impossible to know real precision
# 5. Ignores abundance of data in the database
def triangulate(gsmtowers: List[GsmCell]) -> Tuple[float, float]:
    locations: List[Tuple[float, float]] = [(t.location.latitude, t.location.longitude) for t in gsmtowers]
    strength: List[float] = [t.signal_strength for t in gsmtowers]
    min_strength: float = min(strength)
    strength_shifted: List[float] = [(r - min_strength) for r in strength]

    locations_weighted: List[Tuple[float, float]] = [(i * s, j * s) for (i, j), s in zip(locations, strength_shifted)]
    final_location: Tuple[float, float] = (
        math.fsum([i for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
        math.fsum([j for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
    )
    return final_location


def add_new_gsm_cell(cell):
    pass


@location.route("/", methods=["GET"])
def get_location():
    data = request.json
    if "wifi_networks" not in data and "gsm_cells" not in data and "ip" not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    gsm_cell_obj: List[GsmCell] = []
    for cell in data["gsm_cells"]:
        gsm_cell: List[GsmCell] = db.session.execute(
            db.select(GsmCell).where(
                GsmCell.country_code == cell["country_code"] and GsmCell.operator_id == cell["operator_id"] and GsmCell.cell_id == cell["cell_id"]
            )
        )
        assert len(gsm_cell) <= 1, "Combination of country_code operator_id and cell_id is supposed to be unique"
        if len(gsm_cell) == 0:
            add_new_gsm_cell(cell)
        gsm_cell_obj.append(gsm_cell[0])
    loc_tuple = triangulate(gsm_cell_obj)
    location = {"latitude": loc_tuple[0], "longitude": loc_tuple[1], "altitude": 0, "precision": 100, "altitude_precision": 0, "type": "GSM"}
    return jsonify({"Location": location}), 200
