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
# from 

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)
    CORS(app)
    login_manager = LoginManager(app)

    # login_manager.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(auth)
    app.register_blueprint(home)

    return app

if __name__ == "__main__":
    create_app().run(debug=True)

# from keycloak import KeycloakAdmin
# from keycloak import KeycloakOpenIDConnection

# keycloak_connection = KeycloakOpenIDConnection(
#                         server_url="http://localhost:8080/",
#                         username='admin',
#                         password='admin',
#                         realm_name="person",
#                         client_id="myClient",
#                         client_secret_key="client-secret",
#                         verify=True)

# # keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

# import os
# import json
# import logging
# from flask import Flask, jsonify, request
# import traceback
# from flask_cors import CORS
# import requests
# from keycloak import KeycloakAuthenticationError

# app = Flask(__name__)

# KEYCLOAK_URI = 'http://localhost:8080/'
# REALM = 'person'

# @app.route('/token_login/', methods=['POST'])
# def get_token():
#     body = request.get_json()
#     for field in ['username', 'password']:
#         if field not in body:
#             return error(f"Field {field} is missing!"), 400
#     data = {
#         'grant_type': 'password',
#         'client_id': 'myClient',
#         'client_secret': os.getenv('CLIENT_SECRET'),
#         'username': body['username'],
#         'password': body['password']
#     }
#     url = ''.join([KEYCLOAK_URI + 'realms/' + REALM + '/protocol/openid-connect/token'])
#     response = requests.post(url, data=data)
#     if response.status_code > 200:
#         message = "Error en username/password"
#         return error(message), 400
#     tokens_data = response.json()
#     ret = {
#         'tokens': {"access_token": tokens_data['access_token'],
#                    "refresh_token": tokens_data['refresh_token'], }
#     }
#     return jsonify(ret), 200


# @app.route('/token_refresh/', methods=['POST'])
# def refresh_token():
#     body = request.get_json()
#     for field in ['refresh_token']:
#         if field not in body:
#             return error(f"Field {field} is missing!"), 400
#     data = {
#         'grant_type': 'refresh_token',
#         'client_id': 'myClient',
#         'client_secret': os.getenv('CLIENT_SECRET'),
#         'refresh_token': body['refresh_token'],
#     }
#     url = KEYCLOAK_URI + 'realms/' + REALM + '/protocol/openid-connect/token'
#     response = requests.post(url, data=data)
#     if response.status_code != requests.codes.ok:
#         return error("Error en refresh token"), 400
#     data = response.json()
#     ret = {
#         "access_token": data['access_token'],
#         "refresh_token": data['refresh_token']
#     }
#     return jsonify(ret), 200


# @app.route('/users/', methods=['POST'])
# def create_user():
#     try:
#         body = request.get_json()
#         endpoint = '/users'
#         data = {
#             "email": body.get('email'),
#             "username": body.get('email'),
#             "firstName": body.get('name'),
#             "lastName": body.get('sirname'),
#             "credentials": [{"value": body.get('password'), "type": 'password', 'temporary': False}],
#             "enabled": True,
#             "emailVerified": False
#         }
#         response = keycloak_post(endpoint, data)
#     except KeycloakAdminError as e:
#         try:
#             message = e.response.json().get('errorMessage')
#         except Exception as err:
#             message = e.message
#         app.logger.error(e.traceback())
#         return error(message), 400
#     except Exception as e:
#         print(e)
#         return error('Error with keycloak'), 400
#     return "", 204


# @app.errorhandler(404)
# def not_found(e):
#     return error("No exite la ruta para la url deseada en esta api"), 404


# @app.errorhandler(405)
# def doesnt_exist(e):
#     return error("No exite la ruta para la url deseada en esta api"), 405


# def error(message):
#     return jsonify({
#         'success': False,
#         'message': message
#     })


# def keycloak_post(endpoint, data):
#     """
#     Realiza un POST request a Keycloak
#     :param {string} endpoint Keycloak endpoint
#     :data {object} data Keycloak data object
#     :return {Response} request response object
#     """
#     url = KEYCLOAK_URI + 'admin/realms/' + REALM + endpoint
#     headers = get_keycloak_headers()
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code >= 300:
#         app.logger.error(response.text)
#         raise KeycloakAdminError(response)
#     return response


# def get_keycloak_headers():
#     """
#     Devuelve los headers necesarios para comunicarlos con la API de Keycloak
#     utilizando el usuario de administración del Realm.
#     :return {object} Objeto con headers para API de Keycloak
#     """
#     return {
#         'Authorization': 'Bearer ' + get_keycloak_access_token(),
#         'Content-Type': 'application/json'
#     }


# def get_keycloak_access_token():
#     """
#     Devuelve los tokens del usuario `admin` de Keycloak
#     :returns {string} Keycloak admin user access_token
#     """
#     data = {
#         'grant_type': 'password',
#         'client_id': 'admin-cli',
#         'username': os.getenv('ADMIN_USER'),
#         'password': os.getenv('ADMIN_PASS')
#     }
#     response = requests.post(KEYCLOAK_URI + 'realms/' + REALM + '/protocol/openid-connect/token', data=data)
#     if response.status_code != requests.codes.ok:
#         raise KeycloakAuthenticationError
#     data = response.json()
#     return data.get('access_token')


# class KeycloakAdminError(Exception):
#     message = 'Keycloak error'

#     def __init__(self, response, message=None):
#         if message is not None:
#             self.message = message
#         # Call the base class constructor with the parameters it needs
#         super().__init__(self.message)
#         # Now for your custom code...
#         self.response = response

#     def traceback(self):
#         return traceback.format_exc()

#     def __str__(self):
#         return json.dumps({
#             'message': self.message,
#             'status_code': self.response.status_code,
#             'text': self.response.text
#         })

# from flask import Flask
# from flask_oidc import OpenIDConnect

# app = Flask(__name__)

# oidc = OpenIDConnect(app)

# @app.route('/')
# def index():
#     if oidc.user_loggedin:
#         return 'Welcome %s' % oidc.user_getfield('email')
#     else:
#         return 'Not logged in'
    
# @app.route('/login')
# @oidc.require_login
# def login():
#     return 'Welcome %s' % oidc.user_getfield('email')

# from keycloak.realm import KeycloakRealm

# realm = KeycloakRealm(server_url='http://localhost:8080/', realm_name='person')
# oidc_client = realm.open_id_connect(client_id='myClient', client_secret='client-secret')
# print(realm.realm_name, oidc_client.get_url)

# from keycloak.keycloak_openid import KeycloakOpenID
# # from keycloak import keycloak_openid, well_known

# keycloak_openid = KeycloakOpenID(server_url='http://localhost:8080/', client_id='python-client', realm_name='person', client_secret_key='vSTuwFZ0YCZ43Z0iER0AYlb7G3etUxHD')

# config_well_known = keycloak_openid.well_know()
# access_token = keycloak_openid.token(
#     grant_type='authorization_code',
#     code='the_code_you_get_from_auth_url_callback',
#     redirect_uri="your_call_back_url")
# token = keycloak_openid.token("user", "password")
# print(keycloak_openid.client_id)


# from keycloak.keycloak_admin import KeycloakAdmin

# keycloak_admin = KeycloakAdmin(server_url='http://localhost:8080/', username='myuser', password='myuser', realm_name='person', verify=True)

# print(keycloak_admin.get_users({"username": "derek"}))

# users = keycloak_admin.create_user({"username": "derek", "enabled": True})
# print(keycloak_admin.get_users({}), sep="\n")
# keycloak_admin.get_user(user_id=['dave'])