from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db 

class Project(db.Model):
    __tablename__ = 'Project'

    Deleted = db.Column(db.Boolean, default=False)
    NoOfReviews = db.Column(db.Integer, nullable=True)
    PercNeutral = db.Column(db.Integer, nullable=True)
    PercPositive = db.Column(db.Integer, nullable=True)
    PercNegative = db.Column(db.Integer, nullable=True)
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __init__(self, UserId, NoOfReviews=None, PercPositive=None, PercNegative=None, PercNeutral=None):
        self.UserId = UserId
        self.NoOfReviews = NoOfReviews
        self.PercPositive = PercPositive
        self.PercNegative = PercNegative
        self.PercNeutral = PercNeutral

    def __repr__(self):
        return f'<Project {self.Id}>'