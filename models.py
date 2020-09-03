from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, default="https://secure.gravatar.com/avatar/a97703cbfea6a0ccee000eefa1cde37a?s=256&d=mm&r=g")
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True)