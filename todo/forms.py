from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class TodoForm(FlaskForm):
    title = StringField("제목", validators=[DataRequired()])
    desc = TextAreaField("내용", validators=[DataRequired()])

class UserCreationForm(FlaskForm):
    username = StringField("유저이름", validators=[DataRequired(), Length(min=3,max=32)])
    password1 = StringField("비번", validators=[DataRequired(), EqualTo('password2', "불일치")])
    password2 = StringField("비번2", validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])