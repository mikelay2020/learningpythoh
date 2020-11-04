from app import app, db
from app.models import User, Skill
from flask import request

@app.route('/')
def home():
   return "hello world!"

#@app.route('/users/', methods = ['GET'])
@app.route('/users', methods = ['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        """return the information for <user_id>"""
        return "Test"

    if request.method == 'POST':
        name = request.form.get('username', default="Nouser", type=str)
        newuser = User(username=name,email="none")
        db.session.add(newuser)
        db.session.commit()
        return "Done"

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        pass
    else:
        # POST Error 405 Method Not Allowed
        pass

@app.route('/skills', methods = ['GET', 'POST', 'DELETE'])
def skills():
    if request.method == 'GET':
        """return the information for <user_id>"""
        return "Test"

    if request.method == 'POST':
        name = request.form.get('name', default="Nouser", type=str)
        text = request.form.get('text', default="No text", type=str)
        skill = Skill(name=name,text=text)
        
        db.session.add(skill)
        db.session.commit()
        return "Done"

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        pass
    else:
        # POST Error 405 Method Not Allowed
        pass
