from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = ''


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True)

    name = db.Column(db.Text,
                     nullable=False)

    species = db.Column(db.Text,
                        nullable=False)

    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMG_URL)

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
