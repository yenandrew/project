from flask import Flask

from extension import login_manager, db
from flask_sqlalchemy import SQLAlchemy


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from model import User
    @login_manager.user_loader
    def load_user(user_id):  # reload user object from the user ID stored in the session
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    extension(app)
    return app


def extension(app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param app: Flask application instance
    :return:
    """
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
