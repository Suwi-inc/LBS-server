from flask import Blueprint, request

from ..service.admin_service import create_admin, get_admins, auth_admin_service
from ..auth.auth_guard import auth_guard

admin = Blueprint("admin", __name__)


@admin.route("/register", methods=["POST"])
def add_admin():
    data = request.get_json()
    return create_admin(data)


@admin.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    return auth_admin_service(data)


@admin.route("/", methods=["GET"])
@auth_guard("admin")
def get_admin():
    return get_admins()
