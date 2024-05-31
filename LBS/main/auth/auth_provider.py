from ..model.models import Admin, Device


def authenticate_device(device, serial):
    existing_device = Device.query.filter_by(
        serial_number=serial, device_model=device
    ).first()
    if existing_device:
        return {
            "device": {
                "device_model": existing_device.device_model,
                "serial_number": existing_device.serial_number,
            },
            "roles": ["user"],
        }
    else:
        return {
            "status": "fail",
            "message": "Device not found",
        }


def authenticate_admin(user_name, password):
    admin = Admin.query.filter_by(user_name=user_name, password=password).first()
    if admin:
        return {
            "admin": {"user_name": admin.user_name},
            "roles": ["admin", "user"],
        }
    else:
        return {"status": "fail", "message": "User does not exist"}
