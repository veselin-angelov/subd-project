from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


db = SQLAlchemy()
admin = Admin(template_mode='bootstrap3', url='/')
