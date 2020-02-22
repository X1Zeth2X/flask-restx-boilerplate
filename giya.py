import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_migrate import Migrate

from app import create_app, db
from app.models.user import User, Role, Permission


app = create_app(os.getenv("FLASK_CONFIG") or "prod")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission)


#    return dict(db=db, User=User, Follow=Follow, Role=Role,
#                Permission=Permission, Post=Post, Comment=Comment)


@app.cli.command()
def test():

    # Import unittest
    import unittest

    # Runs unit tests

    tests = unittest.TestLoader().discover("tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    # Return 1 if tests failed, won't reach here if succeeded.
    return 1
