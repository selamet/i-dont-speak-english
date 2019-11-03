from flask import render_template, request, redirect, url_for, session, flash
from app.decorators import login_required, is_admin

from app.forms import LoginForm, PostForm

from app.models import User, Posts

from app import app, db


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


@app.route("/add_post", methods=['GET', 'POST'])
@login_required
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
@login_required
@is_admin
def post_remove(id):
    Posts.query.filter_by(id=id).delete()
    db.session.commit()
    flash('{} Başlıklı gönderi başarı ile silindi.', 'danger')


@app.route("/post_update/<string:id>", methods=['GET', 'POST'])
@login_required
def post_update(id):
    post = Posts.query.filter_by(id=id).first()
    if post.author == session['username']:
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
    else:
        flash('Erişim yetkiniz bulunmamaktadır.', 'info')
        return redirect(url_for('home'))


@app.route('/word_exercise', methods=['POST', 'GET'])
def word_exercise():
    value = {
        "word_1": {
            "eng_word": 'order',
            "user": 'selamet',
            "turk_word": ['sipariş vermek', 'Sıraya koymak', 'Çalışmıyor'],
            "created_date": '28.11.2019'
        },
        "word_2": {
            "eng_word": 'old',
            "user": 'selamet',
            "turk_word": ['eski', 'yaşlı'],
            "created_date": '28.11.2019'
        },
        "word_3": {
            "eng_word": 'age',
            "user": 'selamet',
            "turk_word": ['yaş'],
            "created_date": '28.11.2019'
        },
        "word_4": {
            "eng_word": 'carpet',
            "user": 'selamet',
            "turk_word": ['halı'],
            "creadet_date": '28.11.2019'
        },
        "word_5": {
            "eng_word": 'word',
            "user": 'selamet',
            "turk_word": ['kelime'],
            "creadet_date": '28.11.2019'
        }
    }

    return render_template('word_exercise.html', value=value)