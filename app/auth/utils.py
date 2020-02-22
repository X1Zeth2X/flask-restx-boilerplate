from flask_restx import Namespace, fields


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


# Validations
from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length, Email


class LoginSchema(Schema):
    """ /auth/login [POST]

    Parameters:
    - Email
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])


class RegisterSchema(Schema):
    """ /auth/register [POST]

    Parameters:
    - Email
    - Username (Str)
    - Name (Str)
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    username = fields.Str(
        required=True,
        validate=[
            Length(min=4, max=15),
            Regexp(
                r"^([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)$",
                error="Invalid username!",
            ),
        ],
    )
    name = fields.Str(
        validate=[
            Regexp(
                r"^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", error="Invalid name!",
            )
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])
