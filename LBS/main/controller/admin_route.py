from flask import Blueprint, request
import json
from ..service.admin_service import create_admin, get_admins, auth_admin_service
from ..auth.auth_guard import auth_guard
from ..utils.data_objects import RouteInfo

admin = Blueprint("admin", __name__)


@admin.route("/register", methods=["POST"])
def add_admin():
    data = json.loads(request.data.decode("utf-8").replace("json=", ""))
    route = RouteInfo(request.endpoint, request.method)
    return create_admin(data, route)


@admin.route("/auth", methods=["POST"])
def auth():
    data = json.loads(request.data.decode("utf-8").replace("json=", ""))
    route = RouteInfo(request.path, request.method)
    return auth_admin_service(data, route)


@admin.route("/", methods=["GET"])
@auth_guard("admin")
def get_admin():
    return get_admins()
