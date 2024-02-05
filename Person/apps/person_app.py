import json
# import requests
from flask_cors import cross_origin
# from flask_login import login_required
# from Person.apps.middleware import token_required
from flask import Blueprint, request, Response
# , jsonify, make_response
from model.address import Address
from model.competitions import Competition
from model.contact import Contact
from model.document import Document
from model.person import Person
from model.person_profile import PersonProfile, Participated_Competitions
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
Resp = Response
part_compi = Participated_Competitions()
Cr = customResponse


# API

@home.route("/")
def index():
    return {"message": "Welcome to API"}, 200

# Person

@home.route("/person")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @login_required
def get_all():
    return person.display()

@home.route("/person/<person_id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def get_id(person_id):
    return person.displayOne(person_id)

@home.route("/person", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_user():
    try:
        data = request.get_json()
        # return person.create(data)
#    return jsonify(person.create(data))
        # person.create(data)
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

@home.route("/person/<person_id>", methods=["PUT"])
# @login_required
def update_user(person_id):
    data = request.get_json()
    print(data)
    return person.update(person_id, data)

@home.route("/person/<person_id>", methods=["DELETE"])
# @login_required
@cross_origin(allow_headers=['Content-Type','Authorization'])
def delete_user(person_id):
    print(person_id)
    try:
        response = person.personDelete(person_id)
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

@home.route("/person/profile/<person_id>/<profile_id>")
def get_profile_by_id(person_id, profile_id):
    # print(athlete.display())
    return personProfile.displayOneAdd(person_id, profile_id)

@home.route("/person/profile", methods=["POST"])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def post_profile():
    data = request.get_json()
    print(data)
    return personProfile.create(data)

@home.route("/person/profile/partCompi")
def get_profile_partCompi():
    # print(athlete.display())
    return personProfile.display()

@home.route("/person/profile/partCompi", methods=["POST"])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def post_partCompi():
    data = request.get_json()
    print(data)
    return personProfile.create(data)


# Competitions

@home.route("/person/compi")
def get_compi():
    return compi.display()

@home.route("/person/compi/<compi_id>")
def get_compi_by_id(compi_id):
    return compi.displayOneAdd(compi_id)

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


# Participated Competitions

@home.route("/person/profile/part_compi/<profile_id>")
# @cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_parti_compi(profile_id):
    return part_compi.display(profile_id)

@home.route("/person/profile/part_compi/<id>/<profile_id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_one_compi(id, profile_id):
    return part_compi.displayOne(id, profile_id)


# Document

@home.route("/person/profile/doc")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_document():
    return doc.display()

@home.route("/person/profile/doc/<doc_id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_document_id(doc_id):
    return doc.displayOneAdd(doc_id)

@home.route("/person/profile/doc", methods=["POST"])
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

@home.route("/person/address/<address_id>")
def get_address_by_id(address_id):
    return address.displayOneAdd(address_id)

@home.route("/person/address", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_add():
    # try:
    data = request.get_json()
    print(data)
    return address.create(data)
#    return jsonify(person.create(data))
        # response = person.create(data)
        # p.create(data)
        # response = Response(json.dumps(person),201,mimetype='application/json')
        # response.headers['Person'] = "/person/" + str(data['firstname'])
    # except Exception as e:
    #     print(e)
    #     ErrorMessage = {
    #         "error": str(e),
    #         "helpString": " Refer the Client Model for Details "
    #     }
    #     response = Response(json.dumps(ErrorMessage),
    #                         status=400, mimetype='application/json')
    # return response


# Contact

@home.route("/person/contact")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_con():
    return contact.display()

@home.route("/person/contact/<contact_id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def get_contact_by_id(contact_id):
    return contact.displayOneCon(contact_id)

@home.route("/person/contact", methods=["POST"])
# @login_required
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
def create_cont():
    try:
        data = request.get_json()
        print(data)
        return contact.create(data)
#    return jsonify(person.create(data))
        # response = person.create(data)
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
