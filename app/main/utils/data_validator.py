def validate_request_data(data):
    if "device_id" not in data or "jwt_token" not in data:
        return False
    return True
