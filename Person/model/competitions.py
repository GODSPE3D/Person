from sqlalchemy import Column, Date, DateTime, ForeignKey, String, Table
# from model.participated_competitions import association_table
from model.db import db
from flask import jsonify
from model.person import Person
from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import func
# from model.athlete import Athlete
# from sqlalchemy import MetaData
# from model.athlete import Athlete

# metadata_obj = MetaData()

# association_table = Table(
#     "association_table",
#     metadata_obj,
#     Column("athlete_id", ForeignKey("athlete.id"), primary_key=True),
#     Column("competition_id", ForeignKey("competition.id"), primary_key=True),
# )
# db.session.configure(bind=engine)

class Competition(db.Model):
    __tablename__ = "competition"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    # athlete_id = db.Column(db.ForeignKey("athlete.id"),  primary_key=True)
    # athlete = db.relationship("Athlete", back_populates="athlete")
    # athelete = db.relationship("Athlete", secondary=association_table, back_populates="competition")

    name = Column(String(100))
    venue = Column(String(10))
    organizer = Column(String(100))
    sponsers = Column(String(100))
    criteria = Column(String(100))
    prize = Column(String(100))
    schedule = Column(String(100))
    start_date = Column(Date(), nullable=False)
    end_data = Column(Date(), nullable=False)
    # end_date = db.Column(DateTime, onupdate=func)
    # start-end date

    # def sameID(self, id):
    #     s = db.session.query(
    #         db.session.query(Competition).filter_by(person_id=id).exists()
    #     ).scalar()
    #     if s is True:
    #         return True
    #     return False

    def display(self):
        try:
            # for attribute, value in self.__dict__.items():
            #     print(attribute, value)
            if Competition.query.all() != []:
                return jsonify(
                    [
                        {
                            "id": person.id,
                            "name": person.name,
                            "venue": person.venue,
                            "organizer": person.organizer,
                            "sponsers": person.sponsers,
                            "criteria": person.criteria,
                            "prize": person.prize,
                            "schedule": person.schedule,
                            "start_date": person.start_date,
                            "end_data": person.end_data
                        }
                        for person in Competition.query.all()
                    ]
                )
            raise NoResultFound
        except NoResultFound:
            return "Table is empty!"

    def displayOneAdd(self, id):
        try:
            # if self.sameID(id):
            self = db.session.query(Competition).filter_by(id=id).first()
            for attribute, value in self.__dict__.items():
                print(attribute, value)
            return jsonify(
                [
                    {
                        "id": self.id,
                        "name": self.name,
                        "venue": self.venue,
                        "organizer": self.organizer,
                        "sponsers": self.sponsers,
                        "criteria": self.criteria,
                        "prize": self.prize,
                        "schedule": self.schedule,
                        "start_date": self.start_date,
                        "end_data": self.end_data
                    }
                    # self
                    # {
                    #     attribute: value,
                    # }
                    # for attribute, value in self.
                        # print(attribute, value)
                ]
            )
            # raise NoResultFound
        except NoResultFound:
            return "No such ID exists"

    def create(self, data):
        print(data)
        try:
            if (
                not "name" in data
                or not "venue" in data
                or not "organizer" in data
                or not "sponsers" in data
                or not "criteria" in data
                or not "prize" in data
                or not "schedule" in data
                or not "start_date" in data
                or not "end_data" in data
            ):
                raise NoResultFound
            # if (
                # len(data["person_id"]) < 1
                # len(data["country_code"]) < 1
                # or len(data["region_code"]) < 1
                # or len(data["phone"]) < 1
            # ):
                # raise ValueError

            newP = Competition()
            newP.name = data["name"]
            newP.venue = data["venue"]
            newP.organizer = data["organizer"]
            newP.sponsers = data["sponsers"]
            newP.criteria = data["criteria"]
            newP.prize = data["prize"]
            newP.schedule = data["schedule"]
            newP.start_date = data["start_date"]
            newP.end_data = data["end_data"]

            print(newP.id)
            
            db.session.add(newP)
            db.session.commit()

            return newP.displayOneAdd(newP.id)

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
    #             self = Competition.query.filter_by(id=id).first()

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
    #             self = Competition.query.filter_by(id=id).first()
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
