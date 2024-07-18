from ..model.models import Location, WifiNetwork


def get_wifinetworks_service():
    wifi_data = WifiNetwork.query.join(Location).all()
    wifi_list = [
        {
            "id": wifi.id,
            "mac": wifi.mac,
            "signal_strength": wifi.signal_strength,
            "age": wifi.age,
            "location": {"latitude": wifi.location.latitude, "longitude": wifi.location.longitude, "location_precision": wifi.location.location_precision},
        }
        for wifi in wifi_data
    ]
    response_object = {
        "wifi_networks": wifi_list,
    }
    return response_object, 200
