# from model.db import db
# from flask import jsonify
# from model.person_profile import PersonProfile
# # from model.competitions import Competition


# class Participated_Competitions(db.Model):
#     __tablename__ = "participated_competitions"
    
#     person_id = db.Column(db.Integer, db.ForeignKey('person_profile.person_id'), primary_key=True)
#     competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), primary_key=True)
#     person_profile_id = db.Column(db.Integer, db.ForeignKey('person_profile.profile_id'), primary_key=True)

#     person = db.relationship("PersonProfile", foreign_keys=[person_id])
#     competition = db.relationship("Competition", foreign_keys=[competition_id])
#     person_profile = db.relationship("PersonProfile", foreign_keys=[person_profile_id])

#     def display(self):
#         return jsonify(
#             [
#                 {
#                     "person_id": compi.person_id,
#                     "competition_id": compi.competition_id,
#                     "person_profile_id": compi.person_profile_id
#                 }
#                 for compi in Participated_Competitions.query.all()
#             ]
#         )
    
#     # def displayOne(self, id, profile_id):
#         # join_query = db.session.query(Participated_Competitions, Competition).join(PersonProfile, PersonProfile.profile_id == Participated_Competitions.person_profile_id and PersonProfile.person_id == Participated_Competitions.person_id).join(Competition, Participated_Competitions.competition_id == Competition.id)