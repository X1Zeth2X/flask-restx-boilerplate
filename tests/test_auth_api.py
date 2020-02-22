import json

from tests.utils.base import BaseTestCase
from tests.utils.common import register_user, login_user


class TestAuthBlueprint(BaseTestCase):
    def test_register_and_login(self):
        """ Test Auth API registration and login """
        # Test registration
        data = dict(
            email="test@user.com",
            username="test.User",
            name="Test User",
            password="test1234",
        )

        register_resp = register_user(self, data)
        register_data = json.loads(register_resp.data.decode())

        self.assertEquals(register_resp.status_code, 201)
        self.assertTrue(register_resp.status)
        self.assertEquals(register_data["user"]["username"], data["username"])

        # Test account login
        login_resp = login_user(self, data["email"], data["password"])
        login_data = json.loads(login_resp.data.decode())

        self.assertEquals(login_resp.status_code, 200)
        self.assertTrue(login_resp.status)
        self.assertEquals(login_data["user"]["email"], data["email"])
