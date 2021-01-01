# Validations with Marshmallow
from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length


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
