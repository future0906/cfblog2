# -*- encoding:utf -8 -*-

from flask.blueprints import Blueprint

front = Blueprint("front", __name__, static_folder="static", template_folder="templates")


def init(app):
    from . import views
    app.register_blueprint(front)
