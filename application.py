from flask import Flask
from flask_mongoengine import MongoEngine

from settings import MONGODB_SETTINGS

db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.config.update(config_overrides)

    app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
    db.init_app(app)

    from user.views import user_app
    app.register_blueprint(user_app)

    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)

    return app
