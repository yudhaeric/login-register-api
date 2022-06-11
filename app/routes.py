from flask import request
from app import app
from app.controller import UserController
from app.model.user import User

@app.route('/')
def index():
    return "Hello Flask App"

@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()

# @app.route('/login', methods=['POST'])
# def logins():
#     return UserController.login()