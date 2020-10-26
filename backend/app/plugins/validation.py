from flask_marshmallow import Marshmallow

# def init_app(app):
#     ma = Marshmallow(app)
ma = Marshmallow()


def init_app(app):
    ma.init_app(app)