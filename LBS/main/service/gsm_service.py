from ..model.models import GsmCell
from ..model.models import Location
from ..utils.logger import log_request
from ..utils.route_information import RouteInfo
from .. import db


def get_celltowers_service(request: RouteInfo):
    cell_data = GsmCell.query.join(Location).all()
    cell_list = [
        {
            "id": cell.id,
            "country_code": cell.country_code,
            "operator_id": cell.operator_id,
            "cell_id": cell.cell_id,
            "lac": cell.lac,
            "signal_strength": cell.signal_strength,
            "age": cell.age,
            "Location": {
                "latitude": cell.location.latitude,
                "longitude": cell.location.longitude,
                "location_precision": cell.location.location_precision,
            },
        }
        for cell in cell_data
    ]
    response_object = {
        "cell_towers": cell_list,
    }
    log_request(request, "user requested to view cell towers", __name__)
    return response_object, 200


def add_cell_towers_service(data):

    for cell_tower in data["cell_towers"]:
        # Check if the cell tower already exists in the database
        existing_cell_tower = GsmCell.query.filter_by(
            country_code=cell_tower["country_code"],
            operator_id=cell_tower["operator_id"],
            cell_id=cell_tower["cell_id"],
            lac=cell_tower["lac"],
        ).first()

        if not existing_cell_tower:
            # If the cell tower does not exist, add it to the database
            new_cell_tower = GsmCell(
                country_code=cell_tower["country_code"],
                operator_id=cell_tower["operator_id"],
                cell_id=cell_tower["cell_id"],
                lac=cell_tower["lac"],
                signal_strength=cell_tower["signal_strength"],
                age=cell_tower["age"],
                location_id=cell_tower["location_id"],
            )
            db.session.add(new_cell_tower)
    db.session.commit()
    response_object = {"status": "success", "message": "Cell Towers added"}
    return response_object, 201
