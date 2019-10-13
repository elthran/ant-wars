from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask import Flask

from .extensions import flask_db as db
from . import private_config
from . import environment
from . import hooks


def initialize(name, models=None):
    app = Flask(name.split('.')[0], static_url_path='', static_folder='dist')

    load_configs(app)
    load_extensions(app)
    load_hooks(app)
    load_models(models)

    with app.app_context():
        db.drop_all()
        db.create_all()

        game_world = World()
        game_world.save()
        player1 = Colony(game_world.id)
        player1.save()
        player1_nest = Nest(player1.id, 25, 25)
        player1_nest.save()
        player1_ant = Ant(player1.id, player1_nest.id, 20, 20)
        player1_ant.save()
        db.session.commit()
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

    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


def load_hooks(app):
    hooks.add_auto_commit(app, db)


def load_models(models):
    for model in models:
        globals()[model.__name__] = model
