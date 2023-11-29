from model.db import db
from flask import jsonify
# from flask_sqlalchemy import fore
from model.document import Document
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
# from model.participated_competitions import association_table
from model.competitions import Competition

association_table = db.Table(
    "association_table",
    db.Column("athlete_id", db.ForeignKey("athlete.id"), primary_key=True),
    db.Column("competition_id", db.ForeignKey("competition.id"), primary_key=True)
)

# no API
class Athlete(db.Model): # universal Role table
    __tablename__ = "athlete"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    person_id = db.Column(db.ForeignKey("person.id"),  primary_key=True)
    # role_id = db.Column(db.ForeignKey("roles.id"), primary_key=True)
    # person = db.relationship("Person", back_populates="athlete")
    document = db.relationship("Document", back_populates="athlete")
    competitions = db.relationship("Competition", secondary=association_table, backref="athlete")

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'person_id': self.person_id,
            # 'doc': self.document
        }

    # def sameID(self, id):
    #     s = db.session.query(
    #         db.session.query(Athlete).filter_by(person_id=id).exists()
    #     ).scalar()
    #     if s is True:
    #         return True
    #     return False

    def display(self):
        # Athlete.query.all() != []
        return jsonify(
            [
                {
                    # "id": person.id,
                    # "person_id": person.person_id,
                    # # "document": person.document,
                    # "document": [
                    #     {
                    #         "doc_type": p.doc_type,
                    #         "doc_name": p.doc_name,
                    #         "doc_number": p.doc_number,
                    #         # "doc_img": p.doc_img
                    #     }
                    #     for p in person.document
                    # ]
                    # [
                        attribute: {
                            value
                        }
                        for attribute, value in self.__dict__.items()
                    # ]
                        # print(attribute, value)
                }
                for person in Athlete.query.all()
            ]
        )
        # try:
        #     if Athlete.query.all() != []:
        #         return jsonify(
        #             [
        #                 {
        #                     "id": person.id,
        #                     "address_type": person.person_id,
        #                     "document": [
        #                         {
        #                             "doc_type": p.doc_type,
        #                             "doc_name": p.doc_name,
        #                             "doc_number": p.doc_number,
        #                             "doc_img": p.doc_img
        #                         }
        #                         for p in person.document
        #                     ]
        #                 }
        #                 for person in Athlete.query.all()
        #             ]
        #         )
        #     raise NoResultFound
        # except NoResultFound:
        #     return "Table is empty!"

    # def displayOneAdd(self, id):
    #     try:
    #         if self.sameID(id):
    #             self = db.session.query(Athlete).filter_by(
    #                 person_id=id).first()
    #             return jsonify(
    #                 [
    #                     {
    #                         "id": self.id,
    #                         "address_type": self.address_type,
    #                         "flat_no": self.flat_no,
    #                         "area": self.area,
    #                         "locality": self.locality,
    #                         "city": self.city,
    #                         "state": self.state,
    #                         "country": self.country,
    #                         "pin": self.pin,
    #                     }
    #                 ]
    #             )
    #         raise NoResultFound
    #     except NoResultFound:
    #         return "No such ID exists"

    def create(self, data):
        print(data)
        try:
            if (
                not "person_id" in data
                or not "address_type" in data
                or not "flat_no" in data
                or not "area" in data
                or not "locality" in data
                or not "city" in data
                or not "state" in data
                or not "country" in data
                or not "pin" in data
            ):
                raise NoResultFound
            if (
                # len(data["person_id"]) < 1
                # len(data["country_code"]) < 1
                # or len(data["region_code"]) < 1
                # or len(data["phone"]) < 1
            ):
                raise ValueError

            newP = Athlete()
            newP.person_id = data["person_id"]
            newP.address_type = data["address_type"]
            newP.flat_no = data["flat_no"]
            newP.area = data["area"]
            newP.locality = data["locality"]
            newP.city = data["city"]
            newP.state = data["state"]
            newP.country = data["country"]
            newP.pin = data["pin"]

            print(newP.person_id)
            
            db.session.add(newP)
            db.session.commit()

            return newP.displayOneAdd(newP.person_id)

        except NoResultFound:
            return "Field is missing!"
        except ValueError:
            return "Invalid character length!"
        # except SameValue:
        #     return "email or aadhaar is same"
        except Exception as e:
            return e

    # def update(self, id, data):
    #     # print("Update: ", self, id, data)
    #     try:
    #         if self.sameID(id):
    #             self = Athlete.query.filter_by(id=id).first()

    #             if "country_code" in data:
    #                 self.firstname = data["country_code"]
    #             if "phone" in data:
    #                 self.lastname = data["phone"]

    #             self.status = "old"

    #             db.session.commit()
    #             # print(self)
    #             return self.displayOne(id)
    #         raise NoResultFound
    #     except NoResultFound:
    #         return "No such ID/data exists"

    # def addressDelete(self, id):
    #     print(id)
    #     try:
    #         if self.sameID(id):
    #             self = Athlete.query.filter_by(id=id).first()
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
