from DataObjects import GSMCell, WiFiNetwork, IPAddress
#from models import db, Admin, Device, GsmCell, WifiNetwork, IP, Location
from flask import Flask, jsonify, Response,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    __table_args__ = {'extend_existing': True}

class Device(db.Model):
    __tablename__ = 'device'
    serial_number = db.Column(db.String(50), primary_key=True)
    device_model = db.Column(db.String(128))
    __table_args__ = {'extend_existing': True}

class GsmCell(db.Model):
    __tablename__ = 'gsm_cell'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(50))
    operator_id = db.Column(db.String(50))
    cell_id = db.Column(db.String(50))
    lac = db.Column(db.String(50))
    signal_strength = db.Column(db.String(50))
    age = db.Column(db.String(50))
    __table_args__ = {'extend_existing': True}

class WifiNetwork(db.Model):
    __tablename__ = 'wifi_network'
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(128))
    signal_strength = db.Column(db.String(50))
    age = db.Column(db.String(50))
    __table_args__ = {'extend_existing': True}

class IP(db.Model):
    __tablename__ = 'ip'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50))
    __table_args__ = {'extend_existing': True}

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 7))
    longitude = db.Column(db.Numeric(10, 7))
    location_precision = db.Column(db.Numeric)
    location_type = db.Column(db.String(10))
    gsm_id = db.Column(db.Integer, ForeignKey('gsm_cell.id', ondelete='CASCADE'))
    wifi_id = db.Column(db.Integer, ForeignKey('wifi_network.id', ondelete='CASCADE'))
    ip_id = db.Column(db.Integer, ForeignKey('ip.id', ondelete='CASCADE'))
    created_on = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_on = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    gsm_cell = relationship("GsmCell", backref="locations")
    wifi_network = relationship("WifiNetwork", backref="locations")
    ip = relationship("IP", backref="locations")
    __table_args__ = {'extend_existing': True}


dummy_location = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "altitude": 10,
    "precision": 5,
    "altitude_precision": 2,
    "type": "GSM"
}
@app.route("/")
def main_page():
    return "<p>Main!</p>"
@app.route('/admin', methods=['POST'])
def add_admin():
    data = request.get_json()
    new_admin = Admin(user_name=data['user_name'], password=data['password'])
    db.session.add(new_admin)
    db.session.commit()
    return "Admin added!", 201

@app.route('/location', methods=['GET'])
def get_location():
    data = request.json
    if 'wifi_networks' not in data and 'gsm_cells' not in data and 'ip' not in data:
        return jsonify({"error": "Not enough data provided"}), 400
    #location simuation
    location = dummy_location
    return jsonify({"Location": location}), 200

@app.route('/wifi', methods=['GET'])
def get_wifi():
    data = request.get_json()
    if 'device_id' not in data or 'jwt_token' not in data: # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401
    
    wifi_data = WifiNetwork.query.all()
    wifi_list = [{'id': wifi.id, 'mac': wifi.mac, 'signal_strength': wifi.signal_strength, 'age': wifi.age} for wifi in wifi_data]

    return jsonify({"device": data['device_id'], "wifi": wifi_list}), 200

@app.route('/celltowers', methods=['GET'])
def get_celltowers():
    data = request.get_json()
    if 'device_id' not in data or 'jwt_token' not in data: # replace with impl later
        return jsonify({"No Access": "Unauthorized device"}), 401
    
    cell_data = GsmCell.query.all()
    cell_list = [{'id': cell.id, 'country_code': cell.country_code,'operator_id': cell.operator_id,'cell_id':cell.cell_id,'lac':cell.lac,'signal_strength': cell.signal_strength, 'age': cell.age} for cell in cell_data]

    return jsonify({"device": data['device_id'], "gsm": cell_list}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

