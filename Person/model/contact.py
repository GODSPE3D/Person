from model.db import db
from flask import jsonify
# from model.person import Person
# from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKey
from sqlalchemy.exc import NoResultFound
from model.custom_response import customResponse
from http import HTTPStatus


cr = customResponse()

class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    person_id = db.Column(db.ForeignKey("person.id"),
                          primary_key=True, nullable=False)
    person = db.relationship("Person", back_populates="contact")

    country_code = db.Column(db.Integer)
    region_code = db.Column(db.Integer)
    phone = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "country_code": self.country_code,
            "region_code": self.region_code,
            "phone": self.phone,
            "person_id": self.person_id
        }

    def sameID(self, id):
        s = db.session.query(
            db.session.query(Contact).filter_by(person_id=id).exists()
        ).scalar()
        if s is True:
            return True
        return False

    def display(self):
        contactAll = Contact.query.all()
        try:
            if contactAll() != []:
                cr.list.clear()
                for person in contactAll:
                    cr.list.append(person.serialize)
                
                cr.status_code = HTTPStatus.OK.value
                cr.url = "/person"
                cr.message = HTTPStatus.OK.phrase

                return (cr.list, str(cr.status_code))
                return jsonify(
                    [
                        {
                            "id": person.id,
                            "country_code": person.country_code,
                            "region_code": person.region_code,
                            "phone": person.phone,
                            "person_id": person.person_id
                        }
                        for person in Contact.query.all()
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            cr.status_code = HTTPStatus.NO_CONTENT.value
            cr.message = "Table is empty"

            return (cr.status_code, cr.message)
            return "Table is empty!"

    def displayOneCon(self, id):
        try:
            if self.sameID(id):
                self = db.session.query(Contact).filter_by(
                    person_id=id).first()
                
                cr.person.update(self.serialize)

                cr.message = HTTPStatus.OK.phrase
                cr.status_code = HTTPStatus.OK.value

                return (cr.person, str(cr.status_code))
                return jsonify(
                    {
                        "id": self.id,
                        "country_code": self.country_code,
                        "region_code": self.region_code,
                        "phone": self.phone,
                        "person_id": self.person_id
                    }
                )
            raise NoResultFound
        except NoResultFound:
            cr.message = "No such ID exists"
            cr.status_code = HTTPStatus.OK.value
            return (str(cr.status_code), cr.message)
            return "No such ID exists"

    def displayOneCon2(self, id):
        self = db.session.query(Contact).filter_by(id=id).first_or_404()
        cr.person.update(self.serialize)

        cr.message = HTTPStatus.OK.phrase
        cr.status_code = HTTPStatus.OK.value

        return (cr.person, str(cr.status_code))
        return jsonify(
            [
                {
                    "id": self.id,
                    "country_code": self.country_code,
                    "region_code": self.region_code,
                    "phone": self.phone,
                    # "person_id": self.person_id
                }
            ]
        )

    def create(self, data):
        print(data)
        try:
            if (
                not "person_id" in data
                or not "country_code" in data
                or not "region_code" in data
                or not "phone" in data
            ):
                raise NoResultFound
            if (
                # len(data["person_id"]) < 1
                # len(data["country_code"]) < 1
                # or len(data["region_code"]) < 1
                # or len(data["phone"]) < 1
            ):
                # return msg.badLetter()
                raise ValueError
            # if Contact.email_or_aadhaar(self, Contact.email, data["email"]):
                # return msg.duplicate("email")
                # raise SameValue
            # if Person.email_or_aadhaar(self, Person.aadhaar, data["aadhaar"]):
            #     # return msg.duplicate("aadhaar")
            #     raise SameValue

            newP = Contact()
            newP.person_id = data["person_id"]
            newP.country_code = data["country_code"]
            newP.region_code = data["region_code"]
            newP.phone = data["phone"]

            print(newP.person_id)
            # return jsonify([
            #     {
            #         "person_id": newP.person_id,
            #         "country_code": newP.country_code,
            #         "region_code": newP.region_code,
            #         "phone": newP.phone,
            #     }
            # ])
            db.session.add(newP)
            db.session.commit()

            cr.status_code = HTTPStatus.CREATED.value
            cr.message = HTTPStatus.CREATED.phrase
            return (str(cr.status_code), newP.serialize)

            return jsonify(
                {
                    "person_id": newP.person_id,
                    "country_code": newP.country_code,
                    "region_code": newP.region_code,
                    "phone": newP.phone,
                }
            )

        except NoResultFound:
            cr.message = "Field is missing!"
            cr.status_code = HTTPStatus.OK.value
            return (str(cr.status_code), cr.message)
            return "Field is missing!"
        except ValueError:
            cr.message = "Invalid character length"
            cr.status_code = HTTPStatus.OK.value
            return (str(cr.status_code), cr.message)
            return "Invalid character length!"
        # except SameValue:
        #     return "email or aadhaar is same"
        except Exception as e:
            cr.message = "An error occurred, please try again later"
            cr.status_code = HTTPStatus.OK.value
            return (str(cr.status_code), cr.message)
            return e

    def update(self, id, data):
        # print("Update: ", self, id, data)
        try:
            if self.sameID(id):
                self = Contact.query.filter_by(id=id).first()

                if "country_code" in data:
                    self.country_code = data["country_code"]
                if "phone" in data:
                    self.phone = data["phone"]

                self.status = "old"

                db.session.commit()
                # print(self)
                return self.displayOne(id)
            raise NoResultFound
        except NoResultFound:
            return "No such ID/data exists"

    def contactDelete(self, id):
        print(id)
        try:
            if self.sameID(id):
                self = Contact.query.filter_by(id=id).first()
                if self.status == "tbd":
                    # db.session.delete(self)
                    db.session.commit()
                    return "Data deleted successfully!"
                # else:
                #     self.status = "tbd"
                #     db.session.commit()
                #     return "Data set for deletion"
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"
