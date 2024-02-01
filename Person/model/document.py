from model.db import db
from flask import jsonify
# from model.person import Person
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import func
from model.custom_response import customResponse
from http import HTTPStatus

cr = customResponse()

class Document(db.Model):
    __tablename__ = "document"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    person_profile_id = db.Column(db.ForeignKey("person_profile.profile_id"),  primary_key=True)
    person_profile = db.relationship("PersonProfile", back_populates="document")

    doc_type = db.Column(db.String(50))
    doc_name = db.Column(db.String(50))
    doc_number = db.Column(db.Integer())
    doc_img = db.Column(db.String(50))


    def sameID(self, id):
        s = db.session.query(
            db.session.query(Document).filter_by(person_profile_id=id).exists()
        ).scalar()
        if s is True:
            return True
        return False

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'profile_id': self.person_profile_id,
            'doc_type': self.doc_type,
            'doc_name': self.doc_name,
            'doc_number': self.doc_number,
            'doc_img': self.doc_img
        }

    def display(self):
        # print(
        #     # [
        #         {
        #             "id": doc.id,
        #             "athlete_id": doc.athlete_id,
        #             "doc_type": doc.doc_type
        #         }
        #         for doc in Document.query.all()
        #     # ]       
        # )
        # print()
        # print(Document.query.all())
        # return jsonify ("OK")

        # return cr.createResponse()
    
        # return jsonify(
        #     [
        #         {
        #             "id": doc.id,
        #             "person_profile": doc.person_profile_id,
        #             "doc_type": doc.doc_type,
        #             "doc_name": doc.doc_name,
        #             "doc_img": doc.doc_img,
        #             "doc_number": doc.doc_number
        #         }
        #         for doc in Document.query.all()
        #         # print(doc)
        #     ]
        # )
        try:
            docAll = Document.query.all()
            if docAll != []:
                documentList = []
                
                for doc in docAll:
                    documentList.append(doc.serialize)

                cr.status_code = HTTPStatus.OK.value
                cr.url = "/person/profile/doc"
                cr.message = HTTPStatus.OK.phrase
                cr.list = documentList

                return cr.createResponse()
            raise NoResultFound
        except NoResultFound:
            cr.status_code = HTTPStatus.OK.value
            cr.message = "Table is empty"

            return cr.createResponse()
            return "Table is empty!"

    def displayOneAdd(self, id):
        try:
            if self.sameID(id):
                self = db.session.query(Document).filter_by(
                    person_profile_id=id).first()
                
                cr.person.update(self.serialize)

                cr.message = HTTPStatus.OK.phrase
                cr.status_code = HTTPStatus.OK.value

                return (cr.person, str(cr.status_code))
                # return jsonify(
                #     [
                #         {
                #             "id": self.id,
                #             "person_profile": self.person_profile_id,
                #             "doc_type": self.doc_type,
                #             "doc_name": self.doc_name,
                #             "doc_img": self.doc_img,
                #             "doc_number": self.doc_number
                #         }
                #     ]
                # )
            raise NoResultFound
        except NoResultFound:
            cr.message = "No such ID exists"
            cr.status_code = HTTPStatus.OK.value
            return cr.createIdResponse()
            return "No such ID exists"

    def create(self, data):
        print(data)
        try:
            if (
                not "person_profile_id" in data
                or not "doc_type" in data
                or not "doc_name" in data
                or not "doc_img" in data
                or not "doc_number" in data
            ):
                raise NoResultFound
            if (
                # len(data["person_id"]) < 1
                # len(data["country_code"]) < 1
                # or len(data["region_code"]) < 1
                # or len(data["phone"]) < 1
            ):
                raise ValueError

            newP = Document()
            newP.person_profile_id = data["person_profile_id"]
            newP.doc_type = data["doc_type"]
            newP.doc_name = data["doc_name"]
            newP.doc_img = data["doc_img"]
            newP.doc_number = data["doc_number"]

            print(newP.person_profile_id)
            
            db.session.add(newP)
            db.session.commit()

            cr.status_code = HTTPStatus.CREATED.value
            cr.message = HTTPStatus.CREATED.phrase
            return (str(cr.status_code), newP.serialize)

            return jsonify(
                [
                    {
                        "id": newP.id,
                        "person_profile": newP.person_profile_id,
                        "doc_type": newP.doc_type,
                        "doc_name": newP.doc_name,
                        "doc_img": newP.doc_img,
                        "doc_number": newP.doc_number
                    }
                ]
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
                self = Document.query.filter_by(id=id).first()

                if "country_code" in data:
                    self.firstname = data["country_code"]
                if "phone" in data:
                    self.lastname = data["phone"]

                self.status = "old"

                db.session.commit()
                # print(self)
                return self.displayOne(id)
            raise NoResultFound
        except NoResultFound:
            return "No such ID/data exists"

    # def addressDelete(self, id):
    #     print(id)
    #     try:
    #         if self.sameID(id):
    #             self = Document.query.filter_by(id=id).first()
    #             if self.status == "tbd":
    #                 # db.session.delete(self)
    #                 db.session.commit()
    #                 return "Data deleted successfully!"
    #             # else:
    #             #     self.status = "tbd"
    #             #     db.session.commit()
    #             #     return "Data set for deletion"
    #         raise NoResultFound
    #     except NoResultFound:
    #         return "No such ID exists"
