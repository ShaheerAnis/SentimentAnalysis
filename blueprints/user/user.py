import logging
import hashlib
import datetime
from Models.user_model import User, db
from flask import Blueprint, abort, flash, render_template, redirect, request, url_for, session

user_bp = Blueprint("user", __name__)
logger = logging.getLogger(__name__)

# Main Page
@user_bp.route('/')
def index():
    new_user = User(
            Name = "shaheer", 
            Username="test", 
            Password=hashlib.sha256("123123".encode()).hexdigest(), 
            Email="shaheer786anis@gmail.com",
            JoinDate = datetime.datetime.now())
        
    db.session.add(new_user)
    db.session.commit()
    
    return render_template('test.html')



@user_bp.route('/addUser', methods=['GET','POST'])
def addUser():
    
    
    if request.method == 'POST':
        
        # Get data from form
        name = request.form.get('name')
        username = request.form.get('username')  
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check whether username already exists or not
        user = User.query.filter_by(
                                Username = username,
                                ).first()
        
        # if user already exists
        if user:
            flash("Username already exists.", "message")
            return redirect(url_for('user.addUser'))
        
        
        # if new user
        new_user = User(
            Name = name, 
            Username=username, 
            Password=hashlib.sha256(password.encode()).hexdigest(), 
            Email=email,
            JoinDate = datetime.datetime.now())
        
        db.session.add(new_user)
        db.session.commit()
       
        
        return redirect(url_for('user.userLogin'))
    else:
        return render_template('addUser.html')






@user_bp.route('/userLogin', methods=['GET'])
def show_login():
    return render_template('userLogin.html')

    
#login
@user_bp.route('/userLogin', methods=['POST'])
def userLogin():
    if request.method == 'POST':
        username = request.form.get('username')  # Assuming your login form has 'username' and 'password' fields
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        
        user = User.query.filter_by(Username=username, Password=hashlib.sha256(password.encode()).hexdigest(), RoleId=3).first()
        
        if user:
            session.clear()
            session['user_id'] = user.id
            session['user_role'] = user.RoleId # Storing user ID in the session
            if remember_me:
                session.permanent = True
            else:
                session.permanent = False
                
            print(session.permanent)
            return redirect(url_for('user.index'))  # Redirect to contributor dashboard
        else:
            flash("Login failed. Please try again.", "error")
            return redirect(url_for('user.show_login'))
    else:
        return render_template('UserLogin.html')




@user_bp.route('/changePassword', methods=['GET', 'POST'])
def changePassword():
    if 'user_id' not in session:
        abort(403) 


    user_id = session['user_id']
    user = User.query.get(user_id)

    if user is None:
        abort(404)  # User not found

    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Check if the current password matches the user's actual password
        if  user.Password == hashlib.sha256(current_password.encode()).hexdigest():
            if new_password == confirm_password:
                user.Password = hashlib.sha256(new_password.encode()).hexdigest()
                db.session.commit()
                return redirect(url_for('user.profile'))
            else:
                flash('New password and confirmation password do not match', 'error')
        else:
            flash('Current password is incorrect', 'error')
            
    return render_template('UserChangePpassword.html', user=user)



@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
