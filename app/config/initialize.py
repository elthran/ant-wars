from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask import Flask

from .extensions import flask_db as db
from . import private_config
from . import environment
from . import commands
from . import hooks


def initialize(name, models=None):
    app = Flask(name.split('.')[0], static_url_path='', static_folder='dist')

    load_configs(app)
    load_extensions(app)
    load_commands(app)
    load_hooks(app)
    load_models(models)

    with app.app_context():
        db.drop_all()
        db.create_all()

        game_world = World()
        game_world.save()

        player = User("elthran")
        player.save()
        player_colony_1 = Colony(game_world.id, player.id)
        player_colony_1.save()

        ai = User("computer_easy")
        ai.save()
        ai_colony_1 = Colony(game_world.id, ai.id)
        ai_colony_1.save()

        db.session.commit()

    return app


def load_configs(app):
    env = app.config['ENV'].title()
    app.config.from_object(private_config)
    config = getattr(environment, f'{env}Config')
    app.config.from_object(config)


def load_commands(app):
    app.cli.add_command(commands.db_cli)


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
