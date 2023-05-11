# from .person_app import *
from model.person import Person
from flask import Blueprint, request, redirect, url_for
from flask_cors import cross_origin
from model.user import *
# from ..app import s
# from flask_login import current_user, LoginManager, login_user, logout_user, login_required

# login_manager = LoginManager()
# login_manager.init_app(app)
auth = Blueprint("auth", __name__)
person = Person()
user = User()

@auth.route("/login")
# @cross_origin(allow_headers=['Content-Type','Authorization'])
def get_all():
    return person.display()

@auth.route("/login", methods=["POST"])
@cross_origin(allow_headers=['Content-Type','Authorization'])
# @login_manager.login_required
def sign_in():
    data = request.get_json()
    # data.check_presence(data)
    return redirect(url_for('home.get_id', id=user.check_presence(data)))

    # username = data.get('username')
    # password = data.get('password')

    # user = Person.query.filter_by(email=username, password=password).first()
    
    # if user:
    #     return redirect(url_for('home.get_id', id=user.id))
    # else:
    #     "Unknown User"