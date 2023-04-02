from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound, IntegrityError


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
    contact = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    education = db.Column(db.String(500))
    password = db.Column(db.String(200), nullable=False)
    aadhaar = db.Column(db.BigInteger, nullable=False)  # unique

    # def create(self, data):
    #     self.firstname = (data["firstname"],)
    #     self.lastname = (data["lastname"],)
    #     self.email = (data["email"],)
    #     self.contact = (data["contact"],)
    #     self.address = (data["address"],)
    #     self.education = (data["education"],)
    #     self.password = (data["password"],)
    #     self.aadhaar = data["aadhaar"]

    # Check ID
    def sameID(self, id):
        # try:
        s = db.session.query(
            db.session.query(Person).filter_by(id=id).exists()
        ).scalar()
        if s is True:
            # return self.displayOne(id)
            return True
        return False
        #     raise NoResultFound
        # except NoResultFound:
        #     return "No such ID exists"

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
                            "aadhaar": person.aadhaar,
                        }
                        for person in Person.query.all()
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "Table is empty!"

    # GET with ID
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
                            "aadhaar": self.aadhaar,
                        }
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"

    # POST
    def create(self, data):
        try:
            if (
                not "firstname" in data
                or not "lastname" in data
                or not "email" in data
                or not "aadhaar" in data
                or not "contact" in data
                or not "address" in data
            ):
                raise NoResultFound
            if (
                len(data["firstname"]) < 4
                or len(data["lastname"]) < 4
                or len(data["email"]) < 6
                or len(data["password"]) < 8
            ):
                # return msg.badLetter()
                raise ValueError
            if Person.email_or_aadhaar(self, Person.email, data["email"]):
                # return msg.duplicate("email")
                raise SameValue
            if Person.email_or_aadhaar(self, Person.aadhaar, data["aadhaar"]):
                # return msg.duplicate("aadhaar")
                raise SameValue

            self.firstname = (data["firstname"],)
            self.lastname = (data["lastname"],)
            self.email = (data["email"],)
            self.contact = (data["contact"],)
            self.address = (data["address"],)
            self.education = (data["education"],)
            self.password = (data["password"],)
            self.aadhaar = data["aadhaar"]

            db.session.add(self)
            db.session.commit()

            print(self.firstname)
            return Person.displayOne(self, self.id)

        except NoResultFound:
            return "data doesn't exist"
        except ValueError:
            return "invalid character length"
        except SameValue:
            return "email or aadhaar is same"
        except Exception as e:
            return e

    # def existAll(self, data):
    #     exist = 'firstname' not in data or 'lastname' not in data or 'email' not in data or 'contact' not in data or 'education' not in data
    #     return exist

    def email_or_aadhaar(self, x, data):
        exist = db.session.query(db.exists().where(x == data)).scalar()
        return exist

    # def existAadhaar(self, data):
    #     exist = db.session.query(db.exists().where(Person.aadhaar == data)).scalar()
    #     return exist

    def update(self, id, data):
        try:
            if (
                "email" in data
            ):
                raise NoResultFound
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

                db.session.commit()

                return self.displayOne(id)
            raise NoResultFound
        except NoResultFound:
            return "No such ID/data exists"

    def personDelete(self, id):
        try:
            if self.sameID(id):
                self = Person.query.filter_by(id=id).first()
                db.session.delete(self)
                db.session.commit()
                return "Data deleted successfully!"
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"
