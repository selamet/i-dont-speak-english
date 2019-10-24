from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField


class RegisterForm(FlaskForm):
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=3, max=15)])
    email = StringField("Email Adresi", validators=[validators.Email(message="Lütfen geçerli bir email adresi girin.")])
    password = PasswordField("Parola", validators=[
        validators.DataRequired(message="Lütfen bir parala belirleyin"), validators.EqualTo(fieldname="confirm",
                                                                                            message="Parolalar uyuşmuyor")])
    confirm = PasswordField("Parola Doğrula")

class LoginForm(FlaskForm):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")