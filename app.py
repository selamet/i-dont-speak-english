from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'linuxdegilgnulinux'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/selametsamli/Desktop/i-dont-speak-english/english.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.username)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('auths/login.html', form=form)
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return 'login'
            else:
                return 'Dont Login'
        except:
            return "Dont Login"
