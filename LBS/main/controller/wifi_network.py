from flask import Blueprint

from ..auth.auth_guard import auth_guard
from ..service.wifi_service import get_wifinetworks_service

wifi = Blueprint("wifi", __name__)


@wifi.route("/", methods=["GET"])
@auth_guard()
def get_wifinetworks():
    return get_wifinetworks_service()
