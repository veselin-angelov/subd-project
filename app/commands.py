import click
from flask.cli import with_appcontext


from app.extensions import db


@click.command(name='delete_database')
@with_appcontext
def delete_database():
    db.drop_all()


@click.command(name='create_database')
@with_appcontext
def create_database():
    db.create_all()


@click.command(name='import_initial_data')
@with_appcontext
def import_initial_data():
    pass
