from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = TextAreaField('Повідомлення', validators=[DataRequired(), Length(min=50, max=1024)])
    # FlaskForm: Базовий клас для всіх форм.
    # StringField, PasswordField, SubmitField: Типи полів форми.
    # validators: Список правил для перевірки.
    #     DataRequired(): Перевіряє, чи поле не порожнє.
    #     Email(): Перевіряє, чи це коректна адреса електронної пошти.
    #     Length(min=6): Перевіряє довжину пароля.