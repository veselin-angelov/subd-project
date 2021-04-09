from flask import Flask
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView

from app.commands import create_database, import_initial_data, delete_database
from app.extensions import db, admin
from app.models import *


def register_extensions(app):
    db.init_app(app)
    admin.init_app(app)


def register_admin_views(app):
    admin.add_view(ModelView(Item, db.session))
    admin.add_view(ModelView(Group, db.session))
    admin.add_view(ModelView(SubGroup, db.session))
    admin.add_view(ModelView(Change, db.session))
    admin.add_view(ModelView(BluePrint, db.session))
    admin.add_link(MenuLink(url='/search', name='Search'))


def register_blueprints(app):
    from app.views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


def register_commands(app):
    app.cli.add_command(delete_database)
    app.cli.add_command(create_database)
    app.cli.add_command(import_initial_data)


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    register_extensions(app)
    register_admin_views(app)
    register_blueprints(app)
    register_commands(app)

    return app
