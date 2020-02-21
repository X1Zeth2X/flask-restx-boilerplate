from flask_restx import Api
from flask import Blueprint

# Import auth namespace
from .controller import api as auth_ns

auth_bp = Blueprint("auth", __name__)

auth = Api(
    auth_bp, title="Authenticate", description="Authenticate and receive tokens."
)

# API.
auth.add_namespace(auth_ns)
