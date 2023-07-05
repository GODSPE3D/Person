from flask import Flask
from flask_cors import CORS
# from model.person import db
from model.db import db
# from apps.login_app import auth
# from apps.person_app import home

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db.init_app(app)
CORS(app)

# with app.app_context():
#     db.create_all()

# app.register_blueprint(auth)
# app.register_blueprint(home)
