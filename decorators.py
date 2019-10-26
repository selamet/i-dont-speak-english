from functools import wraps
from flask import request, redirect, url_for, flash, session


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
