from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .. import db


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    __table_args__ = {"extend_existing": True}


class Device(db.Model):
    __tablename__ = "device"
    serial_number = db.Column(db.String(50), primary_key=True)
    device_model = db.Column(db.String(128))
    __table_args__ = {"extend_existing": True}


class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 7))
    longitude = db.Column(db.Numeric(10, 7))
    location_precision = db.Column(db.Numeric)
    location_type = db.Column(db.String(10))
    created_on = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_on = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = {"extend_existing": True}


class GsmCell(db.Model):
    __tablename__ = "gsm_cell"
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String(50))
    operator_id = db.Column(db.String(50))
    cell_id = db.Column(db.String(50))
    lac = db.Column(db.String(50))
    signal_strength = db.Column(db.String(50))
    age = db.Column(db.String(50))
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}


class WifiNetwork(db.Model):
    __tablename__ = "wifi_network"
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(128))
    signal_strength = db.Column(db.String(50))
    age = db.Column(db.String(50))
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}


class IP(db.Model):
    __tablename__ = "ip"
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(50))
    location_id = db.Column(db.Integer, ForeignKey("location.id", ondelete="CASCADE"))
    location = relationship("Location")
    __table_args__ = {"extend_existing": True}
