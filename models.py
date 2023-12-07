"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """A pet available in the agency

    Fields:
    id: primary key, serial
    name: text (20 chars), not null
    species: text (40 chars), not null
    photo_url: text, not null
    age: text, not null
    notes: text, nullable
    available: boolean, default = true
    """

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(20),
        nullable=False
    )

    species = db.Column(
        db.String(40),
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default = ''
    )

    age = db.Column(
        db.String(6),
        # db.CheckConstraint("age in ['baby', 'young', 'adult', 'senior']"),
        nullable=False
    )

    notes = db.Column(
        db.Text
    )

    available = db.Column(
        db.Boolean,
        default = True,
        nullable = False
    )
