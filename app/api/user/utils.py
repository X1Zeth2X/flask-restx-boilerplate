def load_data(user_db_obj):
    """ Load user's data

    Parameters:
    - User db object
    """
    from app.models.schemas import UserSchema

    user_schema = UserSchema()

    data = user_schema.dump(user_db_obj)

    return data
