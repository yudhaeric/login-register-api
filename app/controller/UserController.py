from app.model.user import User

from app import response, app, db
from flask import request
from flask_jwt_extended import *

import datetime

# GET Method
def index():
    try:
        user = User.query.all()
        data = formatarray(user)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    
    return array


def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }

    return data

# POST Method
def save():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        users = User(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', 'Registrasi Berhasil!')
    except Exception as e:
        print(e)

# def login():
#     try:
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()

#         if not user:
#             return response.badRequest([], 'Email kamu belum terdaftar nih!')

#         if not user.checkPassword(password):
#             return response.badRequest([], 'Password kamu salah!')

#         data = singleObject(user)

#         expires = datetime.timedelta(days=7)
#         expires_refresh = datetime.timedelta(days=7)

#         access_token = create_access_token(data, fresh=True, expires_delta= expires)
#         refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

#         return response.success({
#             "data" : data,
#             "access_token" : access_token,
#             "refresh_token" : refresh_token,
#         }, "Login berhasil, selamat datang!")

#     except Exception as e:
#         print(e)