
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