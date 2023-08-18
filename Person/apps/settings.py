from flask import Flask
from flask_cors import CORS
from model.db import db

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
db.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()