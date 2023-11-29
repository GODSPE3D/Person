from model.db import db
from flask import jsonify
# from model.person import Person
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import func


class Document(db.Model):
    __tablename__ = "document"

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    athlete_id = db.Column(db.ForeignKey("athlete.id"),  primary_key=True)
    athlete = db.relationship("Athlete", back_populates="document")

    doc_type = db.Column(db.String(50))
    doc_name = db.Column(db.String(50))
    doc_number = db.Column(db.Integer())
    doc_img = db.Column(db.String(50))


    # def sameID(self, id):
    #     s = db.session.query(
    #         db.session.query(Document).filter_by(person_id=id).exists()
    #     ).scalar()
    #     if s is True:
    #         return True
    #     return False

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'Id': self.id,
            'athlete_id': self.athlete_id,
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
        return jsonify(
                [
                    {
                        "id": doc.id,
                        "athlete_id": doc.athlete_id,
                        "doc_type": doc.doc_type,
                        "doc_name": doc.doc_name,
                        "doc_img": doc.doc_img,
                        "doc_number": doc.doc_number
                    }
                    for doc in Document.query.all()
                    # print(doc)
                ]
            )
        # try:
        #     if Document.query.all() != []:
        #         return jsonify(
        #             [
        #                 {
        #                     "id": doc.id,
        #                     "address_type": doc.doc_type,
        #                     "flat_no": doc.doc_name,
        #                     "area": doc.doc_number,
        #                     "locality": doc.doc_img,
        #                 }
        #                 for doc in Document.query.all()
        #             ]
        #         )
        #     raise NoResultFound
        # except NoResultFound:
        #     return "Table is empty!"

    # def displayOneAdd(self, id):
    #     try:
    #         if self.sameID(id):
    #             self = db.session.query(Document).filter_by(
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

    # def create(self, data):
    #     print(data)
    #     try:
    #         if (
    #             not "person_id" in data
    #             or not "address_type" in data
    #             or not "flat_no" in data
    #             or not "area" in data
    #             or not "locality" in data
    #             or not "city" in data
    #             or not "state" in data
    #             or not "country" in data
    #             or not "pin" in data
    #         ):
    #             raise NoResultFound
    #         if (
    #             # len(data["person_id"]) < 1
    #             # len(data["country_code"]) < 1
    #             # or len(data["region_code"]) < 1
    #             # or len(data["phone"]) < 1
    #         ):
    #             raise ValueError

    #         newP = Document()
    #         newP.person_id = data["person_id"]
    #         newP.address_type = data["address_type"]
    #         newP.flat_no = data["flat_no"]
    #         newP.area = data["area"]
    #         newP.locality = data["locality"]
    #         newP.city = data["city"]
    #         newP.state = data["state"]
    #         newP.country = data["country"]
    #         newP.pin = data["pin"]

    #         print(newP.person_id)
            
    #         db.session.add(newP)
    #         db.session.commit()

    #         return newP.displayOneAdd(newP.person_id)

    #     except NoResultFound:
    #         return "Field is missing!"
    #     except ValueError:
    #         return "Invalid character length!"
    #     # except SameValue:
    #     #     return "email or aadhaar is same"
    #     except Exception as e:
    #         return e

    # def update(self, id, data):
    #     # print("Update: ", self, id, data)
    #     try:
    #         if self.sameID(id):
    #             self = Document.query.filter_by(id=id).first()

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
