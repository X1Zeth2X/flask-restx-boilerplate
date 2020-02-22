from flask_restx import Api
from flask import Blueprint

# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.")

# Core API namespaces
