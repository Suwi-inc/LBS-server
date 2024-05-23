from flask import jsonify

from .. import db
from ..model.models import Admin


def create_admin(data):
    admin = Admin.query.filter_by(user_name=data["user_name"]).first()
    if not admin:
        new_admin = Admin(user_name=data["user_name"], password=data["password"])
        db.session.add(new_admin)
        db.session.commit()
        response_object = {"status": "success", "message": "Admin created"}
        return response_object, 201
    else:
        response_object = {
            "status": "fail",
            "message": "Admin already exists",
        }
        return response_object, 409


def get_admins():
    admin_data = Admin.query.all()
    admin_list = [{"User_name": x.user_name} for x in admin_data]

    return jsonify({"Admins ": admin_list}), 200
