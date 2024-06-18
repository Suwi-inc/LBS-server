from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .. import db


class Admin(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    __table_args__ = {"extend_existing": True}


class Device(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "device"
    serial_number = db.Column(db.String(50), primary_key=True)
    device_model = db.Column(db.String(128))
    __table_args__ = {"extend_existing": True}


class Location(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Double())
    longitude = db.Column(db.Double())
    location_precision = db.Column(db.Integer())
    location_type = db.Column(db.String(10))
    created_on = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_on = db.Column(
        db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    __table_args__ = {"extend_existing": True}


class GsmCell(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "gsm_cell"
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.Integer())
    operator_id = db.Column(db.Integer())
    cell_id = db.Column(db.Integer())
    lac = db.Column(db.Integer())
    signal_strength = db.Column(db.Integer())
    age = db.Column(db.Integer())
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}


class WifiNetwork(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "wifi_network"
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(128))
    signal_strength = db.Column(db.Integer())
    age = db.Column(db.Integer())
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}


class IP(db.Model):
    __bind_key__ = "lbs_db"
    __tablename__ = "ip"
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50))
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}


class LOGS(db.Model):
    __bind_key__ = "logs_db"
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(128))
    log_type = db.Column(db.String(10))
    endpoint = db.Column(db.String(128))
    methods = db.Column(db.String(128))
    message = db.Column(db.String(128))
    serial_number = db.Column(db.String(50))
    time = db.Column(db.TIMESTAMP, default=datetime.now())
    __table_args__ = {"extend_existing": True}
