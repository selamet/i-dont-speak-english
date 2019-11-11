from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, TextAreaField
from flask_ckeditor import CKEditorField


class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")


class InputForm(FlaskForm):
    word = StringField("Your Guess")


class PostForm(FlaskForm):
    title = StringField("Başlık")
    content = TextAreaField("İçerik")
    unit = StringField('Unit')


class WordForm(FlaskForm):
    eng_word = StringField('English Word')
    trk_word = StringField('Turkish Word')
    unit = StringField('Unit')
