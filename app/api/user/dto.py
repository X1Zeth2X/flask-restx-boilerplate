from flask_restx import Namespace, fields


class UserDto:

    api = Namespace("user", description="User related operations.")
    user = api.model(
        "user",
        {
            "email": fields.String,
            "name": fields.String,
            "username": fields.String,
            "joined_date": fields.DateTime,
            "role_id": fields.Integer,
        },
    )

    data_resp = api.model(
        "Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "user": fields.Nested(user),
        },
    )
