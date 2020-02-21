from flask import request
from flask_restx import Resource

from .service import AuthService
from .utils import AuthDto

api = AuthDto.api
auth_success = AuthDto.auth_success


@api.route("/login")
class AuthLogin(Resource):
    """ User login endpoint
    User registers then receives the user's information and access_token
    """

    auth_login = AuthDto.auth_login

    @api.doc(
        "Auth login",
        responses={
            200: ("Logged in", auth_success),
            403: "Incorrect password or incomplete credentials.",
            404: "Email does not match any account.",
        },
    )
    @api.expect(auth_login, validate=True)
    def post(self):
        """ Login using email and password """
        # Grab the json data
        login_data = request.get_json()
        return AuthService.login(login_data)


@api.route("/register")
class AuthRegister(Resource):
    """ User register endpoint
    User registers then receives the user's information and access_token
    """

    auth_register = AuthDto.auth_register

    @api.doc(
        "Auth registration",
        responses={
            201: ("Successfully registered user.", auth_success),
            400: "Bad request, malformed data.",
            403: "Validations failed.",
        },
    )
    @api.expect(auth_register, validate=True)
    def post(self):
        """ User registration """
        # Grab the json data
        register_data = request.get_json()
        print(register_data)
        pass
