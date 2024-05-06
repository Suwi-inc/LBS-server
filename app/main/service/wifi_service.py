from flask import jsonify
from ..model.models import WifiNetwork

def get_wifinetworks_service():
    wifi_data = WifiNetwork.query.all()
    wifi_list = [{
        'id': wifi.id,
        'mac': wifi.mac,
        'signal_strength': wifi.signal_strength,
        'age': wifi.age,
        'location': wifi.location_id
        } for wifi in wifi_data]
    response_object = {
            "wifi_networks": wifi_list,
        }
    return response_object, 200
