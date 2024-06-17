def validate_device_data(data):
    required_fields = {
        "device_model": str,
        "serial_number": str,
    }
    if not isinstance(data, dict):
        raise TypeError("Data should be a dictionary.")

    for field, field_type in required_fields.items():
        if field not in data:

            raise ValueError(f"Missing '{field}' in device data.")
        if not isinstance(data[field], field_type):

            raise TypeError(f"Field '{field}' should be of type {field_type.__name__}.")


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
