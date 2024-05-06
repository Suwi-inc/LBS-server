import math
from typing import List, Tuple

from flask import Blueprint, abort, jsonify, request

from .. import db
from ..model.models import GsmCell, Location

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
def triangulate(gsmtowers: List[Tuple[Location, float]]) -> Tuple[float, float]:
    locations: List[Tuple[float, float]] = [(t[0].latitude, t[0].longitude) for t in gsmtowers]
    strength: List[float] = [t[1] for t in gsmtowers]
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
    try:
        print(request.get_json())
    except Exception:
        abort(400, "Could not parse request as JSON")
    data = request.json
    if "gsm_cells" not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    gsm_cell_locations: List[(GsmCell, Location)] = []
    if len(data["gsm_cells"]) < 2:
        abort(400, f'Need at least 2 cell towers to determine location, got {len(data["gsm_cells"])}')
    for cell in data["gsm_cells"]:
        gsm_cell: List[GsmCell] = db.session.execute(
            db.select(GsmCell).where(
                (GsmCell.country_code == cell["country_code"]) & (GsmCell.operator_id == cell["operator_id"]) & (GsmCell.cell_id == cell["cell_id"])
            )
        ).all()

        assert len(gsm_cell) <= 1, "Combination of country_code operator_id and cell_id is supposed to be unique"

        if len(gsm_cell) == 0:
            add_new_gsm_cell(cell)
            abort(500, "Adding new tower is not yet implemented")

        gsm_cell: GsmCell = gsm_cell[0]._mapping["GsmCell"]
        location: List[Location] = db.session.execute(db.select(Location).where(Location.id == gsm_cell.location_id)).all()

        assert len(location) == 1, f"We do not have location for cell tower {gsm_cell.cell_id}, strange"
        location: Location = location[0]._mapping["Location"]

        gsm_cell_locations.append((location, cell["signal_strength"]))
    loc_tuple = triangulate(gsm_cell_locations)
    location_res = {"latitude": loc_tuple[0], "longitude": loc_tuple[1], "altitude": 0, "precision": 100, "altitude_precision": 0, "type": "GSM"}
    return jsonify({"Location": location_res}), 200
