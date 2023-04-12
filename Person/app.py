import json
from flask import Flask, request, jsonify, Response
from model.person import db, Person
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

person = Person()
db.init_app(app)
# cors = CORS(app, resources={r"/person": {"origins": "*"}})
CORS(app)

with app.app_context():
    db.create_all()


# DEFAULT
@app.route("/")
def home():
    return {"message": "Welcome to API"}, 200


# GET
@app.route("/person")
def get_people():
    return person.display()


# GET with ID
@app.route("/person/<int:id>")
def get_person(id):
    return person.displayOne(id)


# POST
@app.route("/person", methods=["POST"])
# @cross_origin(headers=['Content-Type','Authorization'])
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
        print (e)
        ErrorMessage = {
                "error": str(e)  ,
                "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage), status=400, mimetype='application/json')
    return response


# PUT
@app.route("/person/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    print(data)
    return person.update(id, data)


# DELETE
@app.route("/person/<id>", methods=["DELETE"])
# @cross_origin(headers=['Content-Type','Authorization'])
def delete_user(id):
    print(id)
    try:
        response = person.personDelete(id)
    except Exception as e:
        print (e)
        ErrorMessage = {
                "error": str(e)  ,
                "helpString": " Refer the Client Model for Details "
        }
        response = Response(json.dumps(ErrorMessage), status=400, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run()