import json
from flask_cors import cross_origin
from flask_login import login_required
from model.person import Person
from flask import Blueprint, request, Response, jsonify
from .middleware import token_required
# from flask_oidc import OpenIDConnect

home = Blueprint("home", __name__)
person = Person()
# oidc = OpenIDConnect()

@home.route("/")
def index():
    return {"message": "Welcome to API"}, 200

@home.route("/person")
@cross_origin(allow_headers=['Content-Type','Authorization'])
# @login_required
def get_all():
    return person.display()

@home.route("/person/<id>")
# @cross_origin(allow_headers=['Content-Type','Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def get_id(id):
    return person.displayOne(id)

@home.route("/person/login", methods=["POST"])
@cross_origin(allow_headers=['Content-Type','Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def get_email():
    data = request.get_json()
    if person.displayEmail(data):
        print(data)
        print(person.displayEmail(data))
    # return jsonify(data)
    return person.displayEmail(data)
    # return jsonify({"firstname": "Success"})
    # return person.display()

@home.route("/person", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type','Authorization'])
def create_user():
    try:
        data = request.get_json()
        return person.create(data)
#    return jsonify(person.create(data))
        response = person.create(data)
        #p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage), status=400, mimetype='application/json')
    return response

@home.route("/person/<id>", methods=["PUT"])
@login_required
def update_user(id):
    data = request.get_json()
    print(data)
    return person.update(id, data)

@home.route("/person/<id>", methods=["DELETE"])
# @login_required
# @cross_origin(allow_headers=['Content-Type','Authorization'])
def delete_user(id):
    print(id)
    try:
        response = person.personDelete(id)
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage), status=400, mimetype='application/json')
    return response