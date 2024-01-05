from sqlalchemy import Column, ForeignKey, Table
from model.db import db
from flask import jsonify
from model.person import Person
from sqlalchemy.exc import NoResultFound
from sqlalchemy import MetaData
# from model.athlete import Athlete
from model.competitions import Competition
# import model.athlete

metadata_obj = MetaData()

association_table = Table(
    "association_table",
    metadata_obj,
    Column("athlete_id", ForeignKey("athlete.id"), primary_key=True),
    Column("competition_id", ForeignKey("competition.id"), primary_key=True)
)

# class ParticipatedCompi(db.Model):
#     __tablename__ = "ParticipatedCompi"

#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

#     athlete_id = db.Column(db.ForeignKey("athlete.id"),  primary_key=True)
#     athlete = db.relationship(back_populates="participated_compi")

#     compi_id = db.Column(db.ForeignKey("competition.id"), primary_key=True)
#     # competition = db.relationship("Competition", back_populates="participated_compi")