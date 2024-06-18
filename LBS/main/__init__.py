from os import getenv

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()

# app_config = {"SQLALCHEMY_DATABASE_URI": getenv("DB_URI")}


def create_app():
    app = Flask(__name__)

    # app.config["SQLALCHEMY_DATABASE_URI"] = app_config.get("SQLALCHEMY_DATABASE_URI")

    app.config["SQLALCHEMY_BINDS"] = {
        "lbs_db": getenv("DB_URI"),
        "logs_db": getenv("LOGS_DB"),
    }
    db.init_app(app)
    return app
