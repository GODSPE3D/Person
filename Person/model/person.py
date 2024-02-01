from flask import jsonify
from model.db import db
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.sql import func
from model.custom_response import customResponse
from http import HTTPStatus



class SameValue(Exception):
    "Same value for a variable"


cr = customResponse()

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.relationship("Contact", back_populates="person")
    address = db.relationship("Address", back_populates="person")
    education = db.Column(db.String(500))
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           onupdate=func.current_timestamp())
    status = db.Column(db.String(3), nullable=False)
    person_profile = db.relationship("PersonProfile", back_populates="person")
    participated_competitions = db.relationship("Participated_Competitions", back_populates="person")

    # aadhaar = db.Column(db.BigInteger, nullable=False)  # unique

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            "contact": [
                {
                    "id": p.id,
                    "country_code": p.country_code,
                    "region_code": p.region_code,
                    "phone": p.phone,
                    "person_id": p.person_id
                }
                for p in self.contact
            ],
            "address": [
                {
                    "id": p.id,
                    "address_type": p.address_type,
                    "flat_no": p.flat_no,
                    "area": p.area,
                    "locality": p.locality,
                    "city": p.city,
                    "state": p.state,
                    "country": p.country,
                    "pin": p.pin
                }
                for p in self.address
            ],
            'education': self.education,
            # 'password': self.password,
            'created_at': self.created_at,
            'status': self.status,
            "person_profile": [
                {
                    "profile_type": p.profile_type,
                    "person_docs": [
                        {
                            "id": doc.id,
                            "person_profile": doc.person_profile_id,
                            "doc_type": doc.doc_type,
                            "doc_name": doc.doc_name,
                            "doc_img": doc.doc_img,
                            "doc_number": doc.doc_number
                        }
                        for doc in p.document
                    ]
                }
                for p in self.person_profile
            ]
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
        personAll = Person.query.all()
        personList = []
        try:
            if personAll != []:
                # personList = []
                # cr.list.clear()
                for person in personAll:
                    personList.append(person.serialize)
                
                cr.status_code = HTTPStatus.OK.value
                cr.url = "/person"
                cr.message = HTTPStatus.OK.phrase
                cr.list = personList
                # cr = customResponse(HTTPStatus.OK.value, "/person", HTTPStatus.OK.phrase, personList, "")
                # print(HTTPStatus.OK.value)
                # cr.list = personList
                # cr.__init__()
                
                # set all variables when returning any response
                # cr(HTTPStatus.OK.value, "/person", HTTPStatus.OK.phrase)
                # print(HTTPStatus.NO_CONTENT.phrase)
                print(cr.message)
                # return customResponse.createResponse(cr)
                return cr.createResponse()
                # return (cr.list, cr.message, cr.url, str(cr.status_code))
                return (cr.list)
            raise NoResultFound
        except NoResultFound:
            cr.status_code = HTTPStatus.OK.value
            cr.message = "Table is empty"

            return cr.createResponse()
            # return (cr.status_code, cr.message)
            # return "Table is empty!"

    # GET with ID
    # update
    def displayOne(self, id):
        # self = db.session.query(Person).filter_by(id=id).first()
        try:
            # p = db.session.query.get(Person, id)
            # p = Person.query.filter_by(id=id).first_or_404()
            # print(id)
            # print(p)
            if self.sameID(id):
                p = Person.query.filter_by(id=id).first()  # email
                # print(p.id)
                # return jsonify(
                cr.person.update(p.serialize)
                # cr.list = cr.person
                cr.message = HTTPStatus.OK.phrase
                cr.status_code = HTTPStatus.OK.value
                return cr.createIdResponse()

                # return (cr.person, str(cr.status_code))
                # cr.person.update(
                #     {
                #         "id": p.id,
                #         "firstname": p.firstname,
                #         "lastname": p.lastname,
                #         "email": p.email,
                #         "contact": [
                #             {
                #                 "phone": pr.phone,
                #                 "country_code": pr.country_code,
                #                 "region_code": pr.region_code
                #             }
                #             for pr in p.contact
                #         ],
                #         "address": [
                #             {
                #                 "address_type": pr.address_type,
                #                 "flat_no": pr.flat_no,
                #                 "area": pr.area,
                #                 "locality": pr.locality,
                #                 "city": pr.city,
                #                 "state": pr.state,
                #                 "country": pr.country,
                #                 "pin": pr.pin,
                #             }
                #             for pr in p.address
                #         ],
                #         "education": p.education,
                #         "password": p.password,
                #         'created_at': p.created_at,
                #         # "aadhaar": person.aadhaar,
                #     }
                # )
                # print(cr.person.values())
                # print(cr.person.items())
                # return jsonify(cr.person)
                # print(cr.showDetails)
                return p.serialize
            raise NoResultFound
        except NoResultFound:
            cr.message = "No such ID exists"
            cr.status_code = HTTPStatus.OK.value
            return cr.createIdResponse()

    def displayEmail(self, data):
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
            p = Person.query.filter_by(email=data["email"]).first()
            print(p)
            print(p.id)
            if p != {}:

                cr.person.update(p.serialize)
                cr.status_code = HTTPStatus.OK.value
                cr.message = HTTPStatus.OK.phrase
                
                return cr.createIdResponse()
            raise NoResultFound
            return p.serialize
        except NoResultFound:
            cr.message = "No data exists"
            cr.status_code = HTTPStatus.OK.value
            return cr.createIdResponse()
            return

    # POST
    def create(self, data):
        print(data)
        try:
            if (
                not "firstname" in data
                or not "lastname" in data
                or not "email" in data
                or not "password" in data
                # or not "aadhaar" in data
                # or not "contact" in data
                # or not "address" in data
            ):
                raise NoResultFound
            # if (
            #     len(data["firstname"]) < 4
            #     or len(data["lastname"]) < 4
            #     or len(data["email"]) < 6
            #     # or len(data["password"]) < 8
            # ):
            #     # return msg.badLetter()
            #     print("ValueError")
            #     raise ValueError
            # if Person.email_or_aadhaar(self, Person.email, data["email"]):
            #     # return msg.duplicate("email")
            #     print("SameValue")
            #     raise SameValue
            # if Person.email_or_aadhaar(self, Person.aadhaar, data["aadhaar"]):
            #     # return msg.duplicate("aadhaar")
            #     raise SameValue

            newP = Person()
            newP.firstname = data["firstname"]
            newP.lastname = data["lastname"]
            newP.email = data["email"]
            # newP.contact = data["contact"]
            # newP.address = data["address"]
            # newP.education = data["education"]
            newP.password = data["password"]
            newP.created_at = func.now()
            newP.status = "new"
            # newP.aadhaar = data["aadhaar"]

            print(newP)
            db.session.add(newP)
            db.session.commit()

            cr.status_code = HTTPStatus.CREATED.value
            cr.message = HTTPStatus.CREATED.phrase
            cr.person.update(newP.serialize)
            return cr.createIdResponse()
        
            return newP
            return jsonify(
                    {
                        "id": newP.id,
                        "firstname": newP.firstname,
                        "lastname": newP.lastname,
                        "email": newP.email,
                        "password": newP.password,
                        'created_at': newP.created_at,
                    }
                )

        except NoResultFound:
            cr.message = "Please enter all fields"
            cr.status_code = HTTPStatus.OK.value
            return cr.createIdResponse()
            return "data doesn't exist"
        # except ValueError:
        #     # cr.message = "Invalid character length"
        #     # cr.status_code = HTTPStatus.OK.value
        #     # return (str(cr.status_code), cr.message)
        #     return "invalid character length"
        # except SameValue:
        #     # cr.message = "email or aadhaar is same"
        #     # cr.status_code = HTTPStatus.OK.value
        #     # return (str(cr.status_code), cr.message)
        #     return "email or aadhaar is same"
        # except Exception as e:
        #     # cr.message = "An error occurred, please try again later"
        #     # cr.status_code = HTTPStatus.OK.value
        #     # return (str(cr.status_code), cr.message)
        #     return e

    def email_or_aadhaar(self, x, data):
        exist = db.session.query(db.exists().where(x == data)).scalar()
        return exist

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
                    cr.message = "Data deleted successfully!"
                    # cr.status_code = 200
                    return cr.createIdResponse()
                else:
                    self.status = "tbd"
                    db.session.commit()
                    return "Data set for deletion"
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"
        