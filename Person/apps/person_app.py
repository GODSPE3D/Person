import json
from flask_cors import cross_origin
from model.person import Person
from flask import Blueprint, request, Response

home = Blueprint("home", __name__)
person = Person()

@home.route("/")
def index():
    return {"message": "Welcome to API"}, 200

@home.route("/person")
def get_all():
    return person.display()

@home.route("/person/<int:id>")
def get_id(id):
    return person.displayOne(id)

@home.route("/person", methods=["POST"])
@cross_origin(allow_headers=['Content-Type','Authorization'])
def create_user():
    try:
        data = request.get_json()
        return person.create(data)
#    return jsonify(person.create(data))
    #     p = person.create(data)
    #     #p.create(data)
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
def update_user(id):
    data = request.get_json()
    print(data)
    return person.update(id, data)

@home.route("/person/<id>", methods=["DELETE"])
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