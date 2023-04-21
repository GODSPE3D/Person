# import json
# from flask import Flask, request, jsonify, Response, session
# from model.person import db, Person
# from flask_cors import CORS, cross_origin
# from flask_login import current_user, LoginManager, login_user, logout_user, login_required
# import flask_login


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# person = Person()
# login_manager = LoginManager()
# db.init_app(app)
# login_manager.init_app(app)
# app.config['SECRET_KEY'] = 'random key'
# CORS(app)
# # login_manager.login_view = 'login'
# # cors = CORS(app, resources={r"/person": {"origins": "*"}})

# with app.app_context():
#     db.create_all()


# # DEFAULT
# @app.route("/")
# def home():
#     return {"message": "Welcome to API"}, 200


# # GET
# @app.route("/person")
# def get_people():
#     return person.display()


# # GET with ID
# @app.route("/person/<int:id>")
# def get_person(id):
#     return person.displayOne(id)


# # POST
# @app.route("/person", methods=["POST"])
# # @cross_origin(headers=['Content-Type','Authorization'])
# def create_user():
#     try:
#         data = request.get_json()
#         return person.create(data)
# #    return jsonify(person.create(data))
#     #     p = person.create(data)
#     #     #p.create(data)
#         # response = Response(json.dumps(person),201,mimetype='application/json')
#         # response.headers['Person'] = "/person/" + str(data['firstname'])
#     except Exception as e:
#         print(e)
#         ErrorMessage = {
#             "error": str(e),
#             "helpString": " Refer the Client Model for Details "
#         }
#         response = Response(json.dumps(ErrorMessage),
#                             status=400, mimetype='application/json')
#     return response


# # PUT
# @app.route("/person/<id>", methods=["PUT"])
# def update_user(id):
#     data = request.get_json()
#     print(data)
#     return person.update(id, data)


# # DELETE
# @app.route("/person/<id>", methods=["DELETE"])
# # @cross_origin(allow_headers=['Content-Type','Authorization'])
# def delete_user(id):
#     print(id)
#     try:
#         response = person.personDelete(id)
#     except Exception as e:
#         print(e)
#         ErrorMessage = {
#             "error": str(e),
#             "helpString": " Refer the Client Model for Details "
#         }
#         response = Response(json.dumps(ErrorMessage),
#                             status=400, mimetype='application/json')
#     return response

# # @login_manager.user_loader
# # def load_user(user_id):
# #     return Person.objects(id=user_id).first()

# @app.route("/login", methods=["POST"])
# @cross_origin(allow_headers=['Content-Type','Authorization'])
# def login():
#     data = request.get_json()
#     # username = info.get('username', 'guest')
#     # password = info.get('password', '')
#     # user = db.session.query(Person).filter_by(username=email)
#     # user = Person.objects(email=username,
#     #                       password=password).first()

#     # user = Person()
#     # user.email_or_aadhaar(user.email, username)
#     u = data.get('username')
#     p = data.get('password')
#     user = Person.query.filter_by(email=u).first()

#     if user:
#         login_user(user)
#         return person.display()
#     else:
#         msg = "Unkown user"

#     # print(data, u, p)
#     # user = Person.query.filter_by(email=data["username"]).first()
#     # try:
#     #     if user == u:
#     #         response = "Present"
#     #     raise NoResultFound
#     #     except
#     # return response
#     # exists = db.session.query(Person.id).filter_by(email=data["username"], password=data["password"]).first() is not None
#     # print(person.loginPerson(data))
#     # return person.display()
#     # return person.display()
#     # try:
#     #     response = person.loginPerson(data)
#     #     print(response)
#     # except Exception as e:
#     #     print(e)
#     #     ErrorMessage = {
#     #         "error": str(e),
#     #         "helpString": " Refer the Client Model for Details "
#     #     }
#     #     response = Response(json.dumps(ErrorMessage),
#     #                         status=400, mimetype='application/json')
#     # return response

#     # if user:
#     #     # login_user(user)
#     #     return jsonify(data)
#     # else:
#     #     return jsonify({"status": 401,
#     #                     "reason": "Username or Password Error"})


# @app.route('/logout', methods=['POST'])
# def logout():
#     logout_user()
#     return jsonify(**{'result': 200,
#                       'data': {'message': 'logout success'}})


# # @app.route('/user_info', methods=['POST'])
# # def user_info():
# #     if current_user.is_authenticated:
# #         resp = {"result": 200,
# #                 "data": current_user.to_json()}
# #     else:
# #         resp = {"result": 401,
# #                 "data": {"message": "user no login"}}
# #     return jsonify(**resp)


# # class User(db.Model):
# #     name = db.StringField()
# #     password = db.StringField()
# #     email = db.StringField()

# #     def to_json(self):
# #         return {"name": self.name,
# #                 "email": self.email}

# #     def is_authenticated(self):
# #         return True

# #     def is_active(self):
# #         return True

# #     def is_anonymous(self):
# #         return False

# #     def get_id(self):
# #         return str(self.id)

# if __name__ == "__main__":
#     app.config['SESSION_TYPE'] = 'filesystem'
    
#     # sess.init_app(app)
#     app.debug = True
#     app.run()


from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from model.person import db, Person
from apps.login_app import *
from apps.person_app import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    CORS(app)
    login_manager = LoginManager()

    login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth)
    app.register_blueprint(home)

    return app

if __name__ == "__main__":
    create_app().run(debug=True)