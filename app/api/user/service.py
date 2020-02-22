from app.utils import err_resp, message
from app.models.user import User


class UserService:
    @staticmethod
    def get_user_data(username):
        """ Get user data by username """
        user = User.query.filter_by(username=username).first()

        if not user:
            return err_resp("User not found!", "user_404", 404)

        from .utils import load_data

        user_data = load_data(user)

        resp = message(True, "User data sent")
        resp["user"] = user_data
        return resp, 200
