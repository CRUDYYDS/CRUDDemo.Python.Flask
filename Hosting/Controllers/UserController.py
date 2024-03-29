import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from collections import OrderedDict
from DataAccess.Entity.User import User, db


def add():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')
    new_user = User(id=id,name=name, age=age, address=address)
    db.session.add(new_user)
    db.session.commit()
    return {"success": True, "msg": "Success add user"}


def get(userId):
    return User.query.get(userId).serialize


def update():
    data = request.get_json()
    id = data.get('id')
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')
    User.query.filter(User.id == id).update({"name":name, "age":age, "address": address})
    db.session.commit()
    return {"success": True, "msg": "Success update user"}


def delete(userId):
    User.query.filter(User.id == userId).delete()
    db.session.commit()
    return {"success": True, "msg": "Success delete user"}

