from flask import Flask,Blueprint,request
from ..service.admin_service import create_admin,get_admins

admin = Blueprint("admin",__name__)

@admin.route('/', methods=['POST'])
def add_admin():
    
    data = request.get_json()
    return create_admin(data)

@admin.route('/', methods=['GET'])
def get_admin():
    
    return get_admins()