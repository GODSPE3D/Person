import json
from flask_cors import cross_origin
from flask_login import login_required
from model.person import Person
# from model.info import Info
from model.address import Address
from model.contact import Contact
from model.athlete import Athlete
from model.document import Document
from model.competitions import Competition
from flask import Blueprint, request, Response, jsonify
from .middleware import token_required
# from flask_oidc import OpenIDConnect

home = Blueprint("home", __name__)

person = Person()
# info = Info()
address = Address()
contact = Contact()
athlete = Athlete()
doc = Document()
compi = Competition()
# oidc = OpenIDConnect()


@home.route("/")
def index():
    return {"message": "Welcome to API"}, 200

@home.route("/athlete")
def get_a():
    # print(athlete.display())
    return athlete.display()

@home.route("/comp/add")
def get_comp():
    for attribute, value in compi.__dict__.items():
        print(attribute, value)
    return compi.display()

# @home.route("/comp/add/1")
# def get_comp():
#     return compi.display()

@home.route("/comp/add", methods=["POST"]) # person_id/role_id/route_name
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

@home.route("/doc")
def get_d():
    return doc.display()

@home.route("/person")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @login_required
def get_all():
    return person.display()

# API


@home.route("/person/address")
def get_add():
    return address.display()


@home.route("/person/address/<id>")
def get_ad(id):
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

# API


@home.route("/person/contact")
def get_con():
    return contact.display()


@home.route("/person/contact/<id>")
def get_cn(id):
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


@home.route("/person/<id>")
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
# @token_required
# @login_required
# @oidc.accept_token()
def get_id(id):
    return person.displayOne(id)


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
