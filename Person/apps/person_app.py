import json
from flask_cors import cross_origin
from flask_login import login_required
from model.person import Person
# from model.info import Info
from model.address import Address
from model.contact import Contact
from model.person_profile import PersonProfile
from model.document import Document
from model.competitions import Competition
from flask import Blueprint, request, Response, jsonify
from .middleware import token_required
import requests
from model.custom_response import customResponse
# from flask_oidc import OpenIDConnect


home = Blueprint("home", __name__)

person = Person()
# info = Info()
address = Address()
contact = Contact()
personProfile = PersonProfile()
doc = Document()
compi = Competition()
# oidc = OpenIDConnect()


# API

@home.route("/")
def index():
    return {"message": "Welcome to API"}, 200


# Person
@home.route("/person")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @login_required
def get_all():
    # cr = customResponse(200, "Success", "/person", person, person)
    # cr.__init__(200, "Success", "/person", person, person)
    # cr.showDetails()
    return person.display()

@home.route("/person/<id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def get_id(id):
    return person.displayOne(id)

@home.route("/person", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_user():
    try:
        data = request.get_json()
        return person.create(data)
#    return jsonify(person.create(data))
        response = person.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response

@home.route("/person/<id>", methods=["PUT"])
# @login_required
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
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response


# Profile

@home.route("/person/profile")
def get_profile():
    # print(athlete.display())
    return personProfile.display()

@home.route("/person/profile/<id>")
def get_profile_by_id(id):
    # print(athlete.display())
    return personProfile.displayOneAdd(id)


# Competitions

@home.route("/person/compi")
def get_compi():
    return compi.display()

@home.route("/person/compi/<id>")
def get_compi_by_id(id):
    return compi.displayOneAdd(id)

@home.route("/person/compi", methods=["POST"]) # person_id/role_id/route_name
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_compi():
    try:
        data = request.get_json()
        print(data)
        # return compi.create(data)
#    return jsonify(person.create(data))
        response = compi.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response


# Document

@home.route("/person/profile/doc")
def get_document():
    return doc.display()

@home.route("/person/peofile/doc", methods=["POST"])
def post_document():
    try:
        data = request.get_json()
        print(data)
        # return compi.create(data)
#    return jsonify(person.create(data))
        response = doc.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response


# Address

@home.route("/person/address")
def get_address():
    return address.display()

@home.route("/person/address/<id>")
def get_address_by_id(id):
    return address.displayOneAdd(id)

@home.route("/person/address", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_add():
    try:
        data = request.get_json()
        print(data)
        return address.create(data)
#    return jsonify(person.create(data))
        response = person.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response


# Contact

@home.route("/person/contact")
def get_con():
    return contact.display()

@home.route("/person/contact/<id>")
def get_contact_by_id(id):
    return contact.displayOneCon(id)

@home.route("/person/contact", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_cont():
    try:
        data = request.get_json()
        print(data)
        return contact.create(data)
#    return jsonify(person.create(data))
        response = person.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    except Exception as e:
        print(e)
        ErrorMessage = {
            "error": str(e),
            "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage),
                            status=400, mimetype='application/json')
    return response

#     return person.displayEmail()

@home.route("/person/login", methods=["POST"])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def post_email():
    data = request.get_json()
    # if data:
    # response = Response(json.dumps(person),201,mimetype='application/json')
    # response.headers['Content-Type'] = "/person/login" + str(data['email'])
    print(data)
    return person.displayEmail(data)


# @home.route("/person/login", methods=["GET"])
# @cross_origin(allow_headers=['Content-Type', 'Authorization'])
# # @token_required
# # @login_required
# # @oidc.accept_token()
# def get_email():
#     # data = request.get_json()
#     # if data:
#     # response = Response(json.dumps(person),201,mimetype='application/json')
#     # response.headers['Content-Type'] = "/person/login" + str(data['email'])
#     # print(data)
