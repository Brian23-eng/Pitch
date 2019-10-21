from flask import render_template, redirect, url_for, flash, abort
from . import main
from ..models import User, Pitch, Comment
from flask_login import login_required



@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | One Minute Pitch"
    
    return render_template("index.html", title=title)

@main.route('/user/<uname>&<id_user>')
@login_required
def profile(uname, id_user):
    user = User.query.filter_by(username = uname).first()
    
    title = f"{uname.capitalize()}'s Profile"
    
    get_pitches = Pitch.query.filter_by(user_id = id_user).all()
    get_comments = Comment.query.filter_by(user_id = id-user).all()
    
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user, title = title, pitches_no = get_pitches, comments_no = get_comments)
    