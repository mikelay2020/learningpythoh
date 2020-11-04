import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'monkey-nipples'
#Расширение Flask-WTF использует его для защиты веб-форм от противной атаки под названием Cross-Site Request Forgery или CSRF
