#!/usr/bin/env python3.6
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    ma.init_app(app)
    # bcrypt.init_app(app)

    return app


db = SQLAlchemy()
ma = Marshmallow()
# bcrypt = Bcryt()
