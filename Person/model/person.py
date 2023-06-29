from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.sql import func
from keycloak.keycloak_admin import KeycloakAdmin

# keycloak_admin = KeycloakAdmin(server_url='http://localhost:8080/', username='myuser', password='myuser', realm_name='person', verify=True)


db = SQLAlchemy()


class SameValue(Exception):
    "Same value for a variable"


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Integer)
    address = db.Column(db.String(200))
    education = db.Column(db.String(500))
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           onupdate=func.current_timestamp())
    status = db.Column(db.String(3), nullable=False)
    
    #act
    # default
    # time, user type
    # aadhaar = db.Column(db.BigInteger, nullable=False)  # unique

    # def create(self, data):
    #     self.firstname = (data["firstname"],)
    #     self.lastname = (data["lastname"],)
    #     self.email = (data["email"],)
    #     self.contact = (data["contact"],)
    #     self.address = (data["address"],)
    #     self.education = (data["education"],)
    #     self.password = (data["password"],)
    #     self.aadhaar = data["aadhaar"]

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'contact': self.contact,
            'address': self.address,
            'education': self.education,
            # 'password': self.password,
            'created_at': self.created_at,
            'status': self.status,
            # 'aadhaar': self.aadhaar,
        }

    # Check ID
    def sameID(self, id):
        s = db.session.query(
            db.session.query(Person).filter_by(id=id).exists()
        ).scalar()
        if s is True:
            return True
        return False

    # GET
    def display(self):
        try:
            if Person.query.all() != []:
                return jsonify(
                    [
                        {
                            "_id": person.id,
                            "firstname": person.firstname,
                            "lastname": person.lastname,
                            "email": person.email,
                            "contact": person.contact,
                            "address": person.address,
                            "education": person.education,
                            # "password": person.password,
                            'created_at': person.created_at,
                            # "aadhaar": person.aadhaar,
                        }
                        for person in Person.query.all()
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "Table is empty!"

    # GET with ID
    #update
    def displayOne(self, id):
        try:
            # p = db.session.query.get(Person, id)
            # p = Person.query.filter_by(id=id).first_or_404()
            # print(id)
            # print(p)
            if self.sameID(id):
                self = db.session.query(Person).filter_by(id=id).first()
                return jsonify(
                    [
                        {
                            "_id": self.id,
                            "firstname": self.firstname,
                            "lastname": self.lastname,
                            "email": self.email,
                            "contact": self.contact,
                            "address": self.address,
                            "education": self.education,
                            'created_at': self.created_at,
                            'status': self.status,
                            # "aadhaar": self.aadhaar,
                        }
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"

    def displayEmail(self, data):
        try:
            # print(data)
            p = Person.query.filter_by(email=data["email"]).first()

            # should whole data be read from keycloak
            print(self)
            if not p:
                p = Person()
                p.firstname = data["firstname"]
                p.lastname = data["lastname"]
                p.email = data["email"]

                db.session.add(p)
                db.session.commit()
                print(p.id)
            return jsonify(
                [
                    {
                        "_id": p.id,
                        "firstname": p.firstname,
                        "lastname": p.lastname,
                        "email": p.email,
                        "contact": p.contact,
                        "address": p.address,
                        "education": p.education,
                        'created_at': p.created_at,
                    }
                ]
            )
        except NoResultFound:
            return False

    # POST
    def create(self, data):
        print(data)
        try:
            # if (
            #     not "firstname" in data
            #     or not "lastname" in data
            #     or not "email" in data
            #     or not "aadhaar" in data
            #     or not "contact" in data
            #     or not "address" in data
            # ):
            #     raise NoResultFound
            if (
                len(data["firstname"]) < 4
                or len(data["lastname"]) < 4
                or len(data["email"]) < 6
                # or len(data["password"]) < 8
            ):
                # return msg.badLetter()
                raise ValueError
            if Person.email_or_aadhaar(self, Person.email, data["email"]):
                # return msg.duplicate("email")
                raise SameValue
            # if Person.email_or_aadhaar(self, Person.aadhaar, data["aadhaar"]):
            #     # return msg.duplicate("aadhaar")
            #     raise SameValue

            newP = Person()
            newP.firstname = data["firstname"]
            newP.lastname = data["lastname"]
            newP.email = data["email"]
            newP.contact = data["contact"]
            newP.address = data["address"]
            newP.education = data["education"]
            # newP.password = data["password"]
            newP.created_at = func.now()
            newP.status = "new"
            # newP.aadhaar = data["aadhaar"]

            db.session.add(newP)
            db.session.commit()
            # users = keycloak_admin.create_user({"username": data["firstname"], "enabled": True})
            # print(keycloak_admin.get_users({"username": data["firstname"]}))
            # person = Person.query.filter_by(
            #     email=data['email'], aadhaar=data['aadhaar']).first()
            # return Person.displayOne(data, data.id)
            # return person.serialize

            # print(newP)
            # return
            return newP.displayOne(newP.id)
            # return Person.display(self)

        except NoResultFound:
            return "data doesn't exist"
        except ValueError:
            return "invalid character length"
        except SameValue:
            return "email or aadhaar is same"
        except Exception as e:
            return e

    def email_or_aadhaar(self, x, data):
        exist = db.session.query(db.exists().where(x == data)).scalar()
        return exist

    def loginPerson(self, data):
        # if data["username"] in Person.email:
        #     return "Present"
        # if Person.query.filter_by(email=data["username"], password=data["password"]).first():
        #     return "Present"
        # else:
        #     return "Not present"
        try:
            # self.email == Person.query.filter_by(email=data["username"]).first()
            if Person.query.filter_by(email=data["username"],  password=data["password"]).first():
                # Person.query.filter_by(id=id).first()
                # Person.id
                x = Person.query.filter_by(email=data["username"]).first()
                return jsonify(
                    [
                        {
                            "_id": x.id,
                            "firstname": x.firstname,
                            "lastname": x.lastname,
                            "email": x.email,
                            "contact": x.contact,
                            "address": x.address,
                            "education": x.education,
                            # "aadhaar": self.aadhaar,
                        }
                    ]
                )
                return print(Person.id, "present")
            # if self.email_or_aadhaar(Person.email, data["username"]):
            #     return self
            raise NoResultFound
        except NoResultFound:
            return "Data doesn't exist"

    # def existAadhaar(self, data):
    #     exist = db.session.query(db.exists().where(Person.aadhaar == data)).scalar()
    #     return exist

    def update(self, id, data):
        # print("Update: ", self, id, data)
        try:
            # if (
            #     "email" in data
            # ):
            #     print(data)
            #     raise NoResultFound
            if self.sameID(id):
                self = Person.query.filter_by(id=id).first()

                # self.firstname = data["firstname"]
                # self.lastname = data["lastname"]
                # self.contact = data["contact"]

                if "firstname" in data:
                    self.firstname = data["firstname"]
                if "lastname" in data:
                    self.lastname = data["lastname"]
                if "contact" in data:
                    self.contact = data["contact"]
                
                self.status = "old"

                db.session.commit()
                # print(self)
                return self.displayOne(id)
            raise NoResultFound
        except NoResultFound:
            return "No such ID/data exists"

    def personDelete(self, id):
        print(id)
        try:
            if self.sameID(id):
                self = Person.query.filter_by(id=id).first()
                if self.status == "tbd":
                    # db.session.delete(self)
                    db.session.commit()
                    return "Data deleted successfully!"
                else:
                    self.status = "tbd"
                    db.session.commit()
                    return "Data set for deletion"
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"
