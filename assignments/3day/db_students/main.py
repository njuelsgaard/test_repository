#!/usr/bin/env python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *


#############################################################
#
# Read the file, parse the data
#
#############################################################

filename = '.\Data Files\student_data.txt'
with open(filename) as data:
  columns = None
  id = 0
  students = list()
  for line in data:
    if line[0] =='#':
      continue
    if columns == None:
      raw_columns = line.split('|')
      columns = list()
      for column in raw_columns:
        columns.append(column.rstrip())
      columns.insert(0,'id')
    else:
      info = line.split('|')
      info.insert(0,id)
      id+=1
      students.append(dict(zip(columns,info)))


#############################################################
#
# Create the lists of items, prepare to write to DB
#
#############################################################

#CLUB
#create all the clubs and then add them into a list with an id each
clubs = set()
for student in students:
  for club in student['club'].split(','):
    clubs.add(club.rstrip().strip())
clubs = list(clubs)
clubs.pop(0)
club_id = 1
clubs_to_add = list()
for club in clubs:
  new_club = Club()
  new_club.name = club
  new_club.id = club_id
  club_id+=1
  clubs_to_add.append(new_club)

#CITY
#create all the cities and then add them into a list with an id each
cities = set()
for student in students:
  cities.add(student['city'])
city_id=1
cities_to_add = list()
for city in cities:
  new_city = City()
  new_city.label = city
  new_city.id = city_id
  city_id+=1
  cities_to_add.append(new_city)

#STATUS
#create all the status values and add them to a list with an id
statuses = set()
for student in students:
  statuses.add(student['status'])
status_id=1
statuses_to_add = list()
for status in statuses:
  new_status = Status()
  new_status.label = status
  new_status.id = status_id
  status_id+=1
  statuses_to_add.append(new_status)

#SUPERVISOR
#create all the supervisor values and their rooms, add to a list with ids

raw_supervisors = list()
supervisors_to_add = list()
for student in students:
  raw_supervisors.append(student['supervisors'].split(','))
for line in raw_supervisors:
  for entry in line:
    if len(entry)>0:
      curr_supervisor = entry.strip().split('/')
      new_supervisor = Supervisor()
      #new_supervisor.first_name = ""
      new_supervisor.last_name = curr_supervisor[0]
      new_supervisor.room = int(curr_supervisor[1].split(" ")[1])
      add = True
      for supervisor in supervisors_to_add:
        if supervisor.last_name == new_supervisor.last_name and supervisor.room == new_supervisor.room:
          add = False
      if add:
        supervisors_to_add.append(new_supervisor)



#############################################################
#
# Open the session, do some DB writes
#
#############################################################

session = Session()

#CLUB
#Add clubs to table if they don't already exist
existing_clubs = list(session.query(Club))
existing_club_names = list()
for club in existing_clubs:
  existing_club_names.append(club.name)
for club in clubs_to_add:
  if club.name not in existing_club_names:
    session.add(club)

#CITY
#Add cities to table if they don't already exist
existing_cities = list(session.query(City))
existing_city_names = list()
for city in existing_cities:
  existing_city_names.append(city.label)
for city in cities_to_add:
  if city.label not in existing_city_names:
    session.add(city)

#STATUS
#Add statuses to table if they don't already exist
existing_statuses = list(session.query(Status))
existing_status_names = list()
for status in existing_statuses:
  existing_status_names.append(status.label)
for status in statuses_to_add:
  if status.label not in existing_status_names:
    session.add(status)

#SUPERVISORS
#add supervisors to table if they don't already exist
existing_supervisors = list(session.query(Supervisor))
existing_supervisor_names = list()
for supervisor in existing_supervisors:
  existing_supervisor_names.append(supervisor.last_name)
for supervisor in supervisors_to_add:
  if supervisor.last_name not in existing_supervisor_names:
    session.add(supervisor)



test_student = Student()
test_student.id = 1
test_student.





# your code here

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)
