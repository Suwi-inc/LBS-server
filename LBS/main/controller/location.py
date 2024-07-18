import json
import logging
import math
from datetime import datetime, timezone
from typing import List, Tuple

from flask import Blueprint, abort, jsonify, request

from .. import db
from ..model.models import GsmCell, Location
from ..utils.data_objects import LocationInfo
from ..utils.logger import log_action

location = Blueprint("location", __name__)


# https://ieeexplore.ieee.org/abstract/document/7456592
# Has multiple flaws:
# 1. Does not account for the fact that all the math is happening on spheroid
# 2. Does not account for the fact that signal strength may not correlate with real position
#    (1 tower may be blocked by an iron sheet, while others are not)
# 3. Does not account for altitude at all
# 4. Impossible to know real precision
# 5. Ignores abundance of data in the database
def triangulate(gsmtowers: List[Tuple[Location, float]]) -> Tuple[Tuple[float, float], int]:
    locations: List[Tuple[float, float]] = [(t[0].latitude, t[0].longitude) for t in gsmtowers]
    strength: List[float] = [t[1] for t in gsmtowers]
    min_strength: float = min(strength)
    strength_shifted: List[float] = [(r - min_strength) for r in strength]

    locations_weighted: List[Tuple[float, float]] = [(i * s, j * s) for (i, j), s in zip(locations, strength_shifted)]
    final_location: Tuple[float, float] = (
        math.fsum([i for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
        math.fsum([j for (i, j) in locations_weighted]) / math.fsum(strength_shifted),
    )

    precision: float = max_distance(locations, final_location)
    return final_location, round(precision)


def calculate_spherical_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    RADIUS: float = 6371000.0  # Earth radius in m

    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return RADIUS * c


def max_distance(points: List[Tuple[float, float]], p: Tuple[float, float]) -> float:
    max_dist = 0
    for point in points:
        dist = calculate_spherical_distance(p, point)
        max_dist = max(max_dist, dist)
    return max_dist


def add_new_gsm_cell(cell):
    pass


@location.route("/", methods=["POST"])
# @auth_guard()
def get_location():
    logging.basicConfig(level=logging.DEBUG)
    try:
        print(json.loads(request.data.decode("utf-8").replace("json=", "")))
    except Exception:
        err = "Could not parse request as JSON"
        abort(400, err)
    data = json.loads(request.data.decode("utf-8").replace("json=", ""))
    log_action(
        __name__,
        "Location Request",
        request.endpoint,
        request.method,
        data.get("serial_number"),
        "info",
    )
    if "gsm_cells" not in data:
        return (jsonify({"error": "Not enough data provided"}),)

    gsm_cell_locations: List[(Location, float)] = []

    for cell in data["gsm_cells"]:
        gsm_cell: List[GsmCell] = db.session.execute(
            db.select(GsmCell).where(
                (GsmCell.country_code == cell["country_code"])
                & (GsmCell.operator_id == cell["operator_id"])
                & (GsmCell.cell_id == cell["cell_id"])
                & (GsmCell.lac == cell["lac"])
            )
        ).all()

        if len(gsm_cell) == 0:
            add_new_gsm_cell(cell)
            abort(500, "Adding new tower is not yet implemented")

        gsm_cell: GsmCell = gsm_cell[0]._mapping["GsmCell"]
        location: List[Location] = db.session.execute(db.select(Location).where(Location.id == gsm_cell.location_id)).all()

        assert len(location) == 1, f"We do not have location for cell tower {gsm_cell.cell_id}, strange"
        location: Location = location[0]._mapping["Location"]

        gsm_cell_locations.append((location, cell["signal_strength"]))

    # if len(data["gsm_cells"]) == 2:
    #     abort(400, f'Need at least 2 cell towers to determine location, got 2')

    if len(data["gsm_cells"]) in [1, 2]:
        location_res = {
            "latitude": gsm_cell_locations[0][0].latitude,
            "longitude": gsm_cell_locations[0][0].longitude,
            "altitude": -1,
            "precision": gsm_cell_locations[0][0].location_precision,
            "altitude_precision": -1,
            "type": "GSM",
        }

        log_action(
            __name__,
            str(data),
            request.endpoint,
            request.method,
            data.get("serial_number"),
            "info",
            LocationInfo(
                location_res["latitude"],
                location_res["longitude"],
                location_res["precision"],
                datetime.now(timezone.utc),
            ),
        )

        return jsonify({"position": location_res}), 200

    loc_tuple = triangulate(gsm_cell_locations)
    location_res = {
        "latitude": loc_tuple[0][0],
        "longitude": loc_tuple[0][1],
        "altitude": -1,
        "precision": loc_tuple[1],
        "altitude_precision": -1,
        "type": "GSM",
    }
    # Successful Location request log
    log_action(
        __name__,
        str(data),
        request.endpoint,
        request.method,
        data.get("serial_number"),
        "info",
        LocationInfo(
            location_res["latitude"],
            location_res["longitude"],
            location_res["precision"],
            datetime.now(timezone.utc),
        ),
    )
    return jsonify({"position": location_res}), 200
