from functools import wraps
from flask import request, redirect, url_for, flash, session

from app.models import Posts, WordsModel


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash('Buraya girmeye yetkiniz yok', 'danger')
            return redirect(url_for('home', next=request.url))

    return decorated_function


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['username'] == 'admin':
            return f(*args, **kwargs)
        else:
            flash('Buraya girmeye yetkiniz yok', 'danger')
            return redirect(url_for('home', next=request.url))

    return decorated_function


def page_not_found_post(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        id = kwargs['id']
        post = Posts.query.filter_by(id=id).first()
        if post:
            return f(*args, **kwargs)
        else:

            return ''' Tatlım böyle bir sayfa yok. <a href="/"> ana sayfaya gitmek için click me</a> '''

    return decorated_function


def page_not_found_word(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        id = kwargs['id']
        post = WordsModel.query.filter_by(unit=id).first()
        if post:
            return f(*args, **kwargs)
        else:

            return ''' Tatlım böyle bir sayfa yok. <a href="/"> ana sayfaya gitmek için click me</a> '''

    return decorated_function
