"""
Extensions module

Each extension is initialized when app is created.
"""

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

bcrypt = Bcrypt()
migrate = Migrate()
cors = CORS()

jwt = JWTManager()
ma = Marshmallow()
