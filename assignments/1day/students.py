#!usr/bin/env python

student_list_path = r"C:\Users\njuelsgaard\Desktop\SciCoder\SciCoder-2019-Keck\Data Files\student_data.txt"

f = open(student_list_path)
student_info = list()
lines = f.readlines()
lines = lines[5:]

f.close()

for line in lines:
  student_info.append(line.split("|"))
  #print(line)
  
# Find all students fom Attleboro
att_students = list()
for student in student_info:
  if student[2] == "Attleboro":
    att_students.append(student[0] + " " + student[1])
print("\n")
print("Students from Attelboro:")
for student in att_students:
  print(student)
print("\n")

# Find all students with Baker
baker_students = list()
for student in student_info:
  if "Baker" in student[3]:
    baker_students.append(student[0] + " " + student[1])
print("Students advised by Baker:")
for student in baker_students:
  print(student)
print("\n")

#Find all clubs and their members
clubs = set()
my_clubs = list()
for student in student_info:
  my_clubs = student[5].split(",")
  for club in my_clubs:
    curr_club = club.rstrip().strip()
    if curr_club != "" and club != " ":
      clubs.add(curr_club)
      
club_list = list(clubs)

club_members = list()
for club in club_list:
  members = list()
  for student in student_info:
    if club in student[5]:
      members.append(student[0] + " " + student[1])
  #print(members)
  club_members.append(members)

club_mani = dict(zip(club_list, club_members))

for key in club_mani:
  print(f"Members in the {key} Club:")
  for mbr in club_mani[key]:
    print(mbr)
  print()


