import hashlib
import datetime
import logging
from Models.project_model import Project, db
from flask import Blueprint, abort, flash, render_template, redirect, request, url_for, session
from Models.user_model import User

project_bp = Blueprint("project", __name__)
logger = logging.getLogger(__name__)

# Main Page
@project_bp.route('/')
def index():
    
    
    
    return render_template('test.html')



@project_bp.route('/addProject', methods=['GET','POST'])
def addUser():
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    if user is None:
        abort(404)  # User not found
    else:
        if request.method == 'POST':
            request.form.get('name')
            new_project = Project(
                    UserId = user.id,
                    )
            db.session.add(new_project)
            db.session.commit()
            
            return render_template('test.html') # return redirect(url_for('user.userLogin'))


@project_bp.route('/delProject', methods=['GET','POST'])
def delete_project():
    if request.method == 'POST':
        project_id = int(request.form['project_id'])
        project = Project.query.get(project_id)
        if project:
            project.deleted = True
            db.session.commit()
            return redirect(url_for('project.delete_project'))
    else:
        projects = Project.query.filter_by(deleted=False).all()
        return render_template('delete_project.html', projects=projects)


