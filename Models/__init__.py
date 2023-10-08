from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import your models so that they are registered with the db instance
from .user_model import User
from .project_model import Project
from .status_model import Status
from .comment_model import Comment
