from model.db import db
from flask import jsonify
from model.role import Role
from model.person import Person
from sqlalchemy.sql import func
from model.document import Document
from sqlalchemy.orm import relationship
from sqlalchemy.exc import NoResultFound
from model.competitions import Competition
from sqlalchemy.schema import ForeignKeyConstraint, UniqueConstraint
from sqlalchemy import ForeignKey, ForeignKeyConstraint, Table, Integer, String, Column


class Participated_Competitions(db.Model):
    __tablename__ = "participated_competitions"
    
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), primary_key=True)
    person_profile_id = db.Column(db.Integer, db.ForeignKey('person_profile.profile_id'), primary_key=True)

    competition = db.relationship("Competition", back_populates="participated_competitions")
    person = db.relationship("Person", back_populates="participated_competitions")
    person_profile = db.relationship("PersonProfile", back_populates="participated_competitions")

    def display(self, id):
        query_all = Participated_Competitions.query.all()
        if (query_all != []):
            return jsonify(
                [
                    {
                        'person_id': details.person_id,
                        'competition_id': details.competition_id,
                        'person_profile_id': details.person_profile_id,
                        'competition': 
                            [
                                {
                                    "name": compi.name,
                                    "venue": compi.venue,
                                    "organizer": compi.organizer,
                                    "sponsers": compi.sponsers,
                                    "criteria": compi.criteria,
                                    "prize": compi.prize,
                                    "schedule": compi.schedule,
                                    "start_date": compi.start_date,
                                    "end_data": compi.end_data
                                }
                                for compi in details.competition
                            ]
                    }
                    for details in Participated_Competitions.query.all()
                ]
            )
        return []
    
    def displayOne(self, person_id, profile_id):
        join_query = db.session.query(Participated_Competitions).filter_by(person_id = person_id).filter_by(person_profile_id = profile_id).join(Competition, Competition.id == Participated_Competitions.competition_id)
        print(join_query)
        print(person_id, profile_id)
        allQuery = join_query.all()
        print(allQuery)

        return jsonify(
            [
                {
                    'person_id': details.person_id,
                    'competition_id': details.competition_id,
                    # "conpetition": [
                    #     {
                    #         "name": comp.name,
                    #         "venue": comp.venue,
                    #         "organizer": comp.organizer,
                    #         "sponsers": comp.sponsers,
                    #         "criteria": comp.criteria,
                    #         "prize": comp.prize,
                    #     }
                    #     for comp in 
                    # ],
                    # Competition.displayOneAdd(details.competition_id)
                    'person_profile_id': details.person_profile_id
                }
                for details in allQuery
            ]
        )


# no API
class PersonProfile(db.Model): # universal Role table
    __tablename__ = "person_profile"

    profile_id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    
    person_id = db.Column(db.ForeignKey("person.id"),  primary_key=True)
    person = db.relationship("Person", back_populates="person_profile")

    profile_type = db.Column(db.ForeignKey("roles.role_type"))
    role = db.relationship("Role", back_populates="person_profile")

    document = db.relationship("Document", back_populates="person_profile")
    # competitions = db.relationship("Competition", back_populates="person_profile")
    # parti_id = db.Column(db.Integer, db.ForeignKey("participated_competitions.competition_id"))
    participated_competitions = db.relationship("Participated_Competitions", back_populates="person_profile")

    @property
    def serialize(self):
       # """Return object data in easily serializable format"""
        return {
            'Id': self.profile_id,
            'person_id': self.person_id,
            # 'doc': self.document
        }

    def sameID(self, id):
        s = db.session.query(
            db.session.query(PersonProfile).filter_by(profile_id=id).exists()
        ).scalar()
        if s is True:
            return True
        return False
    


    def display(self):
        # Athlete.query.all() != []
        # query_person_role = PersonProfile.query.join(association_table).join(Competition).filter((association_table.c.person_profile_id == PersonProfile.id) & (association_table.c.competition_id == Competition.id)).all()
        # print(query_person_role)

        return jsonify(
            [
                {
                    "profile_id": person.profile_id,
                    "person_id": person.person_id,
                    # "document": person.document,
                    "document": [
                        {
                            "id": p.id,
                            "person_profile": p.person_profile_id,
                            "doc_type": p.doc_type,
                            "doc_name": p.doc_name,
                            "doc_img": p.doc_img,
                            "doc_number": p.doc_number
                        }
                        for p in person.document
                    ],
                    # "competition": [
                    #     {
                    #         "id": self.id,
                    #         "name": self.name,
                    #         "venue": self.venue,
                    #         "organizer": self.organizer,
                    #         "sponsers": self.sponsers,
                    #         "criteria": self.criteria,
                    #         "prize": self.prize,
                    #         "schedule": self.schedule,
                    #         "start_date": self.start_date,
                    #         "end_data": self.end_data
                    #     }
                    # ]
                    # "participated_compi": person.parti_id,
                    "participated_compi": [
                        {
                            # 'person_id': details.person_id,
                            'competition_id': details.competition_id,
                            "name": details.competition.name,
                            "venue": details.competition.venue,
                            "organizer": details.competition.organizer,
                            "sponsers": details.competition.sponsers,
                            "criteria": details.competition.criteria,
                            "prize": details.competition.prize,
                            "schedule": details.competition.schedule,
                            "start_date": details.competition.start_date,
                            "end_data": details.competition.end_data
                            # 'competition': 
                            # [
                                # {
                                #     "name": compi.name,
                                # }
                                # for compi in details.competition
                            # ]
                        }
                        for details in person.participated_competitions
                    ],
                    # "participated": [
                    #     {
                    #         "person_id": 
                    #     }
                    #     for c in person
                    # ]
                    # [
                        # attribute: {
                        #     value
                        # }
                        # for attribute, value in self.__dict__.items()
                    # ]
                        # print(attribute, value)
                }
                for person in PersonProfile.query.all()
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

# person_id
    def displayOneAdd(self, id, profile_id):
        try:
            # print(id, profile_id)
            if self.sameID(id):
                # print(db.session.query(Participated_Competitions)
                #       .join(PersonProfile, Participated_Competitions.person_profile_id == PersonProfile.profile_id)
                #       .join(Competition, Participated_Competitions.competition_id == Competition.id)
                #       .join(Person, Participated_Competitions.person_id == Person.id)
                #       .filter(PersonProfile.profile_id == profile_id and PersonProfile.person_id == id).first())
            # join_query = db.session.query(Participated_Competitions, Competition).join(PersonProfile, PersonProfile.profile_id == Participated_Competitions.person_profile_id and PersonProfile.person_id == Participated_Competitions.person_id).join(Competition, Participated_Competitions.competition_id == Competition.id)
            # print(join_query)

            # allQuery = join_query.all()
            # print(allQuery)
        

                # print("(")

                # for item in row:

                #     print("   ", item)

                # print(")")
            # self = db.session.query(PersonProfile).filter_by(
            #     profile_id=).first()
                return jsonify(
                    # [
                        {
                            "id": self.profile_id,
                            "person_id": self.person_id,
                            # "document": person.document,
                            "document": [
                                {
                                    "doc_type": p.doc_type,
                                    "doc_name": p.doc_name,
                                    "doc_number": p.doc_number,
                                    # "doc_img": p.doc_img
                                }
                                for p in self.document
                            ]
                        }
                    # ]
                )
            raise NoResultFound
        except NoResultFound:
            return "No such ID exists"

    def create(self, data):
        print(data)
        try:
            if (
                not "person_id" in data
                or not "profile_type" in data
                # or not "document" in data
            ):
                raise NoResultFound
            # if (
                # len(data["person_id"]) < 1
                # len(data["country_code"]) < 1
                # or len(data["region_code"]) < 1
                # or len(data["phone"]) < 1
            # ):
                # raise ValueError

            newP = PersonProfile()
            newP.person_id = data["person_id"]
            newP.profile_type = data["profile_type"]
            # newP.document = data["document"]

            print(newP.id)
            
            db.session.add(newP)
            db.session.commit()

            return newP.serialize
            # return newP.displayOneAdd(newP.id)

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
