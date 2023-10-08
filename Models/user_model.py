from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db 

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    Deleted = db.Column(db.Boolean, default=False)
    Name = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(50), nullable=False, index=True)
    Username = db.Column(db.String(50), nullable=False, index=True)
    JoinDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, Username='{self.Username}')>"
