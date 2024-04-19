from DataObjects import GSMCell, WiFiNetwork, IPAddress
from flask import Flask, jsonify, Response,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
from models import Admin, Device, GsmCell, WifiNetwork, IP, Location

migrate = Migrate(app, db)

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

