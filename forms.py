from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, TextAreaField


class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")


class InputForm(FlaskForm):
    word = StringField("Your Guess")


class PostForm(FlaskForm):
    title = StringField("Başlık")
    content = TextAreaField("İçerik")
