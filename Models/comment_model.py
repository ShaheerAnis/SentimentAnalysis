from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db 

class Comment(db.Model):
    __tablename__ = 'Comment'

    Line = db.Column(db.String, nullable=False)
    Deleted = db.Column(db.Boolean, default=False)
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    StatusId = db.Column(db.Integer, db.ForeignKey('Status.Id'), nullable=False)
    ProjectId = db.Column(db.Integer, db.ForeignKey('Project.Id'), nullable=False)

    def __init__(self, Line, StatusId, ProjectId):
        self.Line = Line
        self.StatusId = StatusId
        self.ProjectId = ProjectId

    def __repr__(self):
        return f'<Comment {self.Id}>'