from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from .extensions import db
from . import private_config
from . import environment


def initialize(models=None):
    app = Flask(__name__)

    load_configs(app)
    load_extensions(app)
    load_models(models)

    with app.app_context():
        db.create_all()

        game_world = World()
        game_world.save()
        player1 = Colony(game_world.id)
        player1.save()
        player1_nest = Nest(player1.id, 25, 25)
        player1_nest.save()
        player1_ant = Ant(player1.id, player1_nest.id, 20, 20)
        player1_ant.save()
    return app


def load_configs(app):
    env = app.config['ENV'].title()
    app.config.from_object(private_config)
    config = getattr(environment, f'{env}Config')
    app.config.from_object(config)


def load_extensions(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
    db.init_app(app)


def load_models(models):
    for model in models:
        globals()[model.__name__] = model
