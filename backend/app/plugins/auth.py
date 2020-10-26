from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from app.plugins.database import db
from app.database.user import User, Role
from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import LoginManager

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
login_manager = LoginManager()

def create_user(username, password):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if User.query.filter_by(email=username).first():
        raise RuntimeError(f'{username} ja esta cadastrado')
    user = user_datastore.create_user(email=username, password=password)
    db.session.commit()
    return user


def init_app(app):
    login_manager.init_app(app)
    security = Security(app, user_datastore)
