from app.model.user import User

from app import response, app, db
from flask import request

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
        'password': data.password,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }

    return data