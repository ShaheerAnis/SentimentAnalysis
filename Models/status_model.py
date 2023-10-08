from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db 

class Status(db.Model):
    __tablename__ = 'Status'

    Deleted = db.Column(db.Boolean, default=False)
    Name = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.String(100), nullable=True)
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __init__(self, Name, Description=None):
        self.Name = Name
        self.Description = Description

    def __repr__(self):
        return f'<Status {self.Id}>'