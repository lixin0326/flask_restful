import datetime
from apps.ext import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    url = db.Column(db.String(100))
    is_delete = db.Column(db.Boolean, default=False)
