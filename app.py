from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
import datetime

from forms import LoginForm, InputForm, PostForm
import json

from word_exercise import word_exercise

with open("bilgiler/bilgiler.json") as read_file:
    data = read_file.read()

obj = json.loads(data)
yol = obj['database_yolu']

app = Flask(__name__)

app.config['SECRET_KEY'] = 'linuxdegilgnulinux'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + yol + '/english.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    content = db.Column(db.Text)

    def __repr__(self):
        return 'Title :{} , Author: {}, Tarih: {}'.format(self.title, self.author, self.date_posted)


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
                session['username'] = name
                flash('You were successfully logged in', "success")
                return redirect(url_for('home'))
            else:
                return 'Dont Login'
        except Exception:
            return "Dont Login"


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/word_exercise", methods=['GET', 'POST'])
def word_exercise_url():
    form = InputForm()
    word_dict = word_exercise()

    if request.method == 'GET':
        return render_template(
            "word_exercise.html",
            word_dict=word_dict,
            form=form
        )
    else:
        pass


@app.route("/add_post", methods=['GET', 'POST'])
def add_post():
    try:
        if session['logged_in']:
            form = PostForm(request.form)
            if request.method == 'POST':
                title = form.title.data
                content = form.content.data
                post = Posts(title=title, content=content, author=session['username'])
                db.session.add(post)
                db.session.commit()
                flash('Postunuz başarı ile oluşturuldu', 'success')
                return redirect(url_for('home'))
            else:
                return render_template('post/add_post.html', form=form)
    except KeyError:
        flash('Buraya erişmek için yetkili olmalısınız. ', 'info')
        return redirect(url_for('home'))


@app.route("/post_list")
def post_list():
    posts = Posts.query.all()

    return render_template('post/post_list.html', posts=posts)


@app.route("/post/<string:id>")
def post_detail(id):
    post = Posts.query.filter_by(id=id).first()
    return render_template('post/post_detail.html', post=post)


@app.route("/post_remove/<string:id>")
def post_remove(id):
    if session['username'] == 'admin':
        Posts.query.filter_by(id=id).delete()
        db.session.commit()
        flash('{} Başlıklı gönderi başarı ile silindi.', 'danger')

    else:
        flash('Buraya erişmek için yetkili olmalısınız. ', 'info')
        return redirect(url_for('home'))


@app.route("/post_update/<string:id>", methods=['GET', 'POST'])
def post_update(id):
    post = Posts.query.filter_by(id=id).first()

    if request.method == 'GET':

        if post == None:
            flash('böyle bir sayfa yok', 'danger')
            return redirect(url_for('home'))
        else:
            form = PostForm()
            form.title.data = post.title
            form.content.data = post.content
            return render_template('post/post_update.html', form=form, post=post)
    else:

        form = PostForm()
        new_title = form.title.data
        new_content = form.content.data
        post.title = new_title
        post.content = new_content
        db.session.commit()
        return redirect(url_for('home'))
