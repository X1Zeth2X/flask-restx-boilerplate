from flask_restx import Namespace, fields
from re import compile

# Basic Email REGEX
EMAIl_REGEX = compile(r"[^@]+@[^@]+\.[^@]+")


class AuthDto:
    api = Namespace("auth", description="Authenticate and receive tokens.")

    user_obj = api.model(
        "user",
        {
            "email": fields.String,
            "name": fields.String,
            "username": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    auth_login = api.model(
        "login_data",
        {
            "email": fields.String(required=True),
            "password": fields.String(required=True),
        },
    )

    auth_register = api.model(
        "register_data",
        {
            "email": fields.String(required=True),
            "username": fields.String(required=True),
            # Name is optional
            "name": fields.String,
            "password": fields.String,
        },
    )

    auth_success = api.model(
        "Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "access_token": fields.String,
            "user": fields.Nested(user_obj),
        },
    )
