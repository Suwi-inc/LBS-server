from flask import jsonify

from .. import db
from ..model.models import Device
from ..auth.auth_provider import authenticate_device
from ..auth.jwt_handler import generate_jwt


def add_device_service(data):
    device = Device.query.filter_by(
        device_model=data["device_model"], serial_number=data["serial_number"]
    ).first()
    if not device:
        new_device = Device(
            device_model=data["device_model"], serial_number=data["serial_number"]
        )
        db.session.add(new_device)
        db.session.commit()
        response_object = {"status": "success", "message": "Device added"}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Device already exists",
        }
        return response_object, 409


def auth_device_service(data):
    model = data["device_model"]
    serial = data["serial_number"]

    device_data = authenticate_device(model, serial)
    if not device_data:
        return jsonify({"message": "Invalid credentials", "status": 400}), 400

    token = generate_jwt(
        payload=device_data, lifetime=60
    )  # <--- generates a JWT valid for 1 hour
    return jsonify({"data": token, "status": 200}), 200
