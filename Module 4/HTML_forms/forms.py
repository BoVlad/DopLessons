from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator

class LoginForm(FlaskForm):
    name = StringField("Ваше Ім'я", validators=[DataRequired(), Length(min=1, max=32, message="Ім'я має бути від 1 до 32 символів")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Неправильній email")])
    message = TextAreaField('Повідомлення', validators=[DataRequired(), Length(min=50, max=1024, message="Повідомлення має бути від 50 до 1024 символів")])
    submit = SubmitField('Увійти')
    # FlaskForm: Базовий клас для всіх форм.
    # StringField, PasswordField, SubmitField: Типи полів форми.
    # validators: Список правил для перевірки.
    #     DataRequired(): Перевіряє, чи поле не порожнє.
    #     Email(): Перевіряє, чи це коректна адреса електронної пошти.
    #     Length(min=6): Перевіряє довжину пароля.