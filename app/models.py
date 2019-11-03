import datetime

from slugify import slugify

from app import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    content = db.Column(db.Text)
    slug = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return 'Title :{} , Author: {}, Tarih: {}'.format(self.title, self.id, self.date_posted)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)
