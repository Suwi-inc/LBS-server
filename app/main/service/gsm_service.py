from flask import jsonify
from ..model.models import GsmCell

def get_celltowers_service():
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
    response_object = {
            "cell_towers": cell_list,
        }
    return response_object, 200

    
    