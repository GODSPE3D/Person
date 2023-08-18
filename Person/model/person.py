from flask import jsonify, json, request, make_response
from model.db import db
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.sql import func
from sqlalchemy.orm import joinedload
# from model.contact import Contact
# from model.address import Address


class SameValue(Exception):
    "Same value for a variable"


class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    # contact = db.Column(db.Integer)
    contact = db.relationship("Contact", back_populates="person")
    address = db.relationship("Address", back_populates="person")
    # address = db.Column(db.String(200))
    education = db.Column(db.String(500))
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), onupdate=func.current_timestamp())
    status = db.Column(db.String(3), nullable=False) #profiletype
    profile_type = db.Column(db.String(80), unique=True, nullable=False)
    # person = db.relationship("Info", backref=db.backref("person", uselist=False))
    
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
            # 'contact': self.contact,
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
    
    def sameMail(self, email):
        s = db.session.query(
            db.session.query(Person).filter_by(email=email).exists()
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
                            "id": person.id,
                            "firstname": person.firstname,
                            "lastname": person.lastname,
                            "email": person.email,
                            "contact": [
                                {
                                    "phone": p.phone,
                                    "country_code": p.country_code,
                                    "region_code": p.region_code
                                }
                                for p in person.contact
                            ],
                            "address": [
                                {
                                    "address_type": p.address_type,
                                    "flat_no": p.flat_no,
                                    "area": p.area,
                                    "locality": p.locality,
                                    "city": p.city,
                                    "state": p.state,
                                    "country": p.country,
                                    "pin": p.pin,
                                }
                                for p in person.address
                            ],
                            "education": person.education,
                            "password": person.password,
                            'created_at': person.created_at,
                            # "aadhaar": person.aadhaar,
                        }
                        for person in Person.query.all()
                    ]
                )
                # person = Person.query.all()
                # # for person in Person.query.all():
                # self.common(person)
            raise NoResultFound
        except NoResultFound:
            return "Table is empty!"

    # GET with ID
    #update
    def displayOne(self, id):
        # self = db.session.query(Person).filter_by(id=id).first()
        try:
            # p = db.session.query.get(Person, id)
            # p = Person.query.filter_by(id=id).first_or_404()
            # print(id)
            # print(p)
            if self.sameID(id):
                p = Person.query.filter_by(id=id).first() #email
                print(p.id)
                return jsonify(
                    [
                        {
                            "id": p.id,
                            "firstname": p.firstname,
                            "lastname": p.lastname,
                            "email": p.email,
                            "contact": [
                                {
                                    "phone": per.phone,
                                    "country_code": per.country_code,
                                    "region_code": per.region_code
                                }
                                for per in p.contact
                            ],
                            "address": [
                                {
                                    "address_type": per.address_type,
                                    "flat_no": per.flat_no,
                                    "area": per.area,
                                    "locality": per.locality,
                                    "city": per.city,
                                    "state": per.state,
                                    "country": per.country,
                                    "pin": per.pin,
                                }
                                for per in p.address
                            ],
                            "education": p.education,
                            'created_at': p.created_at,
                            'status': p.status,
                            # "aadhaar": self.aadhaar,
                        }
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"

    def displayEmail(self):
        try:
            # print(data)
            # should whole data be read from keycloak

            # if not self.sameMail(data["email"]):
            #     p = Person()
            #     p.firstname = data["firstname"]
            #     p.lastname = data["lastname"]
            #     p.email = data["email"]

            #     db.session.add(p)
            #     db.session.commit()
            #     print(p.id)
            # Authorization process
            p = Person.query.filter_by(email="aeonflux@gmail.com").first()
            print(p)
            print(p.id)

            return jsonify(
                [
                    {
                        "id": p.id,
                        "firstname": p.firstname,
                        "lastname": p.lastname,
                        "email": p.email,
                        "contact": [
                            {
                                "phone": per.phone,
                                "country_code": per.country_code,
                                "region_code": per.region_code
                            }
                            for per in p.contact
                        ],
                        "address": [
                            {
                                "address_type": per.address_type,
                                "flat_no": per.flat_no,
                                "area": per.area,
                                "locality": per.locality,
                                "city": per.city,
                                "state": per.state,
                                "country": per.country,
                                "pin": per.pin,
                            }
                            for per in p.address
                        ],
                        "education": p.education,
                        'created_at': p.created_at,
                        'status': p.status,
                    }
                ]
            )
            # raise NoResultFound
        except NoResultFound:
            return "No data exists"

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
            # newP.contact = data["contact"]
            newP.address = data["address"]
            newP.education = data["education"]
            # newP.password = data["password"]
            newP.created_at = func.now()
            newP.status = "new"
            # newP.aadhaar = data["aadhaar"]

            db.session.add(newP)
            db.session.commit()

            return newP.displayOne(newP.id)

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
                            "id": x.id,
                            "firstname": x.firstname,
                            "lastname": x.lastname,
                            "email": x.email,
                            # "contact": x.contact,
                            # "address": x.address,
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

# class Info(db.Model):
#     __tablename__ = "info"

#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#     person = db.relationship("Person", backref=db.backref("person", uselist=False))

#     # contact = db.Column(db.Integer) class
#     # address = db.Column(db.String(200)) class
#     pin = db.Column(db.Integer())
#     # bod, aadhaar
#     city = db.Column(db.String(100))
#     state = db.Column(db.String(100))
#     country = db.Column(db.String(100))
#     education = db.Column(db.String(500))

#     def display(self):
#         try:
#             if Info.query.all() != []:
#                 return jsonify(
#                     [
#                         {
#                             "id": person.id,
#                             "contact": person.contact,
#                             "address": person.address,
#                             "pin": person.pin,
#                             "city": person.city,
#                             'state': person.state,
#                             "country": person.country,
#                             "education": person.education
#                         }
#                         for person in Info.query.all()
#                     ]
#                 )
#             raise NoResultFound
#         except NoResultFound:
#             return "Table is empty!"