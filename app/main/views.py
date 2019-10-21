from flask import render_template, redirect, url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | One Minute Pitch"
    
    return render_template("index.html", title=title)
    