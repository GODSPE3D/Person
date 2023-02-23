from flask import Flask, request, jsonify
from Person.P.person import db, Person
from Person.P.message import Message
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

CORS(app)

# @app.route('/api/v1/users/')
# def hello():
#     return jsonify("Hello, Welcomos")

# cors = CORS(app, resources={r"/person/*": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'

with app.app_context():
    db.create_all()

person = Person()
msg = Message()


# DEFAULT
@app.route("/")
# @cross_origin()
def home():
    return {"message": "Welcome to API"}, 200


# GET
@app.route("/person/")
# @cross_origin()
def get_people():
    return person.display()


# GET with ID
@app.route("/person/<id>/")
def get_person(id):
    # print(id)
    # person = Person.query.filter_by(id=id).first_or_404()
    # person = db.session.query(Person.id).first() is not None
    # person = db.session.query(db.session.query(Person).filter_by(id=id).exists()).scalar()
    # if person is True:
    #     # person2 = Person.query.filter_by(id=id).first()
    #     return "This should display if id exists: True"
    # return "False"
    # return person.displayOne(id)
    return person.displayOne(id)


# POST
@app.route("/person/", methods=["POST"])
def create_user():
    data = request.get_json()
    return person.create(data)


# PUT
@app.route("/person/<id>/", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    # if (
    #     "firstname" not in data
    #     or "lastname" not in data
    #     or "email" not in data
    #     or "contact" not in data
    #     or "education" not in data
    # ):
    #     return msg.badReq()

    # person = Person.query.filter_by(id=id).first_or_404()
    # person.update(id, data)
    # person.firstname=data['firstname']
    # person.lastname=data['lastname']
    # person.contact=data['contact']

    # if 'email' in data:
    #     person.email=data['email']
    # if 'aadhaar' in data:
    #     person.aadhaar=data['aadhaar']

    # db.session.commit()
    return person.update(id, data)


# DELETE
@app.route("/person/<id>/", methods=["DELETE"])
def delete_user(id):
    # person = Person.query.filter_by(id=id).first_or_404()
    return person.personDelete(id)


if __name__ == "__main__":
    app.run(port=5002)
