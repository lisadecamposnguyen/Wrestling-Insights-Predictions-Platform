# app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

db = SQLAlchemy()
migrate = Migrate()

class Wrestler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True, unique=True, nullable=False)
    country = db.Column(db.String)
    height_cm = db.Column(db.Integer)
    weight_kg = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    birthplace = db.Column(db.String)
    rating = db.Column(db.Float, nullable=True)

class Promotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

class Championship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    rating = db.Column(db.Float, nullable=True)

class TitleOwnership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"))
    wrestler_id = db.Column(db.Integer, db.ForeignKey("wrestler.id"))
    championship_id = db.Column(db.Integer, db.ForeignKey("championship.id"))
    startdate = db.Column(db.Date)
    enddate = db.Column(db.Date)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Date, index=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey("promotion.id"))

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"))
    date = db.Column(db.Date, index=True)
    # à refaire cette partie car on a des triple threat ect aussi
    wrestler_a_id = db.Column(db.Integer, db.ForeignKey("wrestler.id"), index=True)
    wrestler_b_id = db.Column(db.Integer, db.ForeignKey("wrestler.id"), index=True)
    winner_id = db.Column(db.Integer, db.ForeignKey("wrestler.id"), index=True)
    stipulation = db.Column(db.String)
