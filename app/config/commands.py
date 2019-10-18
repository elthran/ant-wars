import click
from flask import current_app
from flask.cli import with_appcontext


"""command group access follows the pattern `flask db drop`"""
@click.group('db')
def db_cli():
    """Some simple database commands."""


@db_cli.command('drop')
@with_appcontext
def drop_db():
    """Remove the database."""
    from sqlalchemy import create_engine
    from sqlalchemy_utils import drop_database

    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    drop_database(engine.url)
