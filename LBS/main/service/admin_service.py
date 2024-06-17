from flask import jsonify

from .. import db
from ..model.models import Admin
from ..utils.data_objects import RouteInfo
from ..utils.logger import log_action
from ..auth.auth_provider import authenticate_admin
from ..auth.jwt_handler import generate_jwt, decode_jwt


def create_admin(data, route: RouteInfo):
    admin = Admin.query.filter_by(user_name=data["user_name"]).first()
    if not admin:
        new_admin = Admin(user_name=data["user_name"], password=data["password"])
        db.session.add(new_admin)
        db.session.commit()
        response_object = {"status": "success", "message": "Admin created"}
        log_action(
            __name__,
            response_object.get("message"),
            route.endpoint,
            route.methods,
            data.get("user_name"),
            "info",
        )
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Admin already exists",
        }
        return response_object, 409


def auth_admin_service(data, route: RouteInfo):
    user_name = data["user_name"]
    password = data["password"]
    if not user_name or not password:
        return jsonify({"message": "Email or password missing", "status": 400}), 400

    user_data = authenticate_admin(user_name, password)
    if not user_data:
        return jsonify({"message": "Invalid credentials", "status": 400}), 400

    token = generate_jwt(
        payload=user_data, lifetime=60
    )  # <--- generates a JWT with valid within 1 hour by now
    log_action(
        __name__,
        "Admin was succefully authenticated",
        route.endpoint,
        route.methods,
        user_name,
        "info",
    )
    return jsonify({"token": token, "status": 200}), 200


def get_admins():
    admin_data = Admin.query.all()
    admin_list = [{"User_name": x.user_name} for x in admin_data]

    return jsonify({"Admins ": admin_list}), 200
