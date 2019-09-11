#!/usr/bin/python

import sys

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relation, exc, column_property, validates
from sqlalchemy import orm
from sqlalchemy.orm.session import Session

from DatabaseConnection import DatabaseConnection

dbc = DatabaseConnection()

# ========================
# Define database classes
# ========================
Base = declarative_base(bind=dbc.engine)

class Student(Base):
	__tablename__ = 'student'
	__table_args__ = {'autoload' : True}
	
class Status(Base):
	__tablename__ = 'status'
	__table_args__ = {'autoload' : True}
  
class City(Base):
  __tablename__ = 'city'
  __table_args__ = {'autoload' : True}

class Club(Base):
	__tablename__ = 'club'
	__table_args__ = {'autoload' : True}

class StudentToClub(Base):
	__tablename__ = 'student_to_club'
	__table_args__ = {'autoload' : True}

class Supervisor(Base):
	__tablename__ = 'supervisor'
	__table_args__ = {'autoload' : True}

class StudentToSupervisor(Base):
	__tablename__ = 'student_to_supervisor'
	__table_args__ = {'autoload' : True}

# =========================
# Define relationships here
# =========================

Student.clubs = relation(Club,
                         secondary=StudentToClub.__table__,
                         backref="students")
Student.status = relation(Status, backref="students")
Student.supervisors = relation(Supervisor,
                               secondary=StudentToSupervisor.__table__,
                               backref="students")
Student.city = relation(City, backref="students")


# THIS IS INCOMPLETE FOR THE EXERCISE -
# add additional required relationships here

# Student.clubs = relation(Club,
# 						 secondary=StudentToClub.__table__, # the join table
# 						 primaryjoin=Student.id==StudentToClub.student_id,
# 						 secondaryjoin=StudentToClub.club_id==Club.id, # note that this is the Table, not the object class!
# 						 foreign_keys=[StudentToClub.student_id,StudentToClub.club_id],
# 						 backref="students")
# 
# Student.status = relation(Status,
# 						  primaryjoin=Student.status_id==Status.id,
# 						  foreign_keys=[Student.status_id],
# 						  backref="students")
# 
# Student.supervisors = relation(Supervisor,
# 							   secondary=StudentToSupervisor.__table__,
# 							   primaryjoin=Student.id==StudentToSupervisor.student_id,
# 							   secondaryjoin=StudentToSupervisor.supervisor_id==Supervisor.id,
# 							   foreign_keys=[StudentToSupervisor.student_id, StudentToSupervisor.supervisor_id],
# 							   backref="students")

# ---------------------------------------------------------
# Test that all relations/mappings are self-consistent.
# ---------------------------------------------------------

from sqlalchemy.orm import configure_mappers
try:
	configure_mappers()
except RuntimeError:
	print("""
An error occurred when verifying the relations between the database tables.
Most likely this is an error in the definition of the SQLAlchemy relations - 
see the error message below for details.
""")
	print("Error type: %s" % sys.exc_info()[0])
	print("Error value: %s" % sys.exc_info()[1])
	print("Error trace: %s" % sys.exc_info()[2])
	sys.exit(1)
