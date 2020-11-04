from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    
    username = StringField('Имя Скила', validators=[DataRequired()])
    text = StringField('Описание скила', validators=[DataRequired()])
#    time_created = DateTimeField(verbose_name='Дата активации')
    
    remember_me = BooleanField('Авто добавление')
    submit = SubmitField('Сохранить Нах..')


