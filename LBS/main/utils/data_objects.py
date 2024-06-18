class GSMCell:
    def __init__(self, country_code, operator_id, cell_id, lac, signal_strength, age):
        self.country_code = country_code
        self.operator_id = operator_id
        self.cell_id = cell_id
        self.lac = lac
        self.signal_strength = signal_strength
        self.age = age


class WiFiNetwork:
    def __init__(self, mac, signal_strength, age):
        self.mac = mac
        self.signal_strength = signal_strength
        self.age = age


class IPAddress:
    def __init__(self, address_v4):
        self.address_v4 = address_v4


class Device:
    def __init__(self, device_model="default", serial_number="default"):
        self.device_model = device_model
        self.serial_number = serial_number


class RouteInfo:
    def __init__(self, endpoint, methods):
        self.endpoint = endpoint
        self.methods = methods

    def __repr__(self):
        return f"<endpoint={self.endpoint}, methods={self.methods}>"
