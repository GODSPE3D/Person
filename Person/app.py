from flask import Flask, request, jsonify
from model.person import db, Person
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

person = Person()
db.init_app(app)
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
def create_user():
    data = request.get_json()
    return person.create(data)


# PUT
@app.route("/person/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    print(data)
    return person.update(id, data)


# DELETE
@app.route("/person/<int:id>", methods=["DELETE"])
def delete_user(id):
    return person.personDelete(id)


if __name__ == "__main__":
    app.run(port=5002)