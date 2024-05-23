def validate_request_data(data):
    if "device_id" not in data or "jwt_token" not in data:
        return False
    return True


def validate_cell_tower_data(data):
    required_fields = {
        "country_code": int,
        "operator_id": int,
        "cell_id": int,
        "lac": int,
        "signal_strength": int,
        "age": int,
        # "location_id": int, -- reserved for future use
    }

    if "cell_towers" not in data:
        raise ValueError("Missing 'cell_towers' in data.")

    for cell_tower in data["cell_towers"]:
        for field, field_type in required_fields.items():
            if field not in cell_tower:
                raise ValueError(f"Missing '{field}' in cell tower data.")
            if not isinstance(cell_tower[field], field_type):
                raise TypeError(
                    f"Field '{field}' should be of type {field_type.__name__}."
                )
