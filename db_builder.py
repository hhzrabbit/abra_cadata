# Alan Chen
# SoftDev pd8
# HW08: Average
# 2016-10-18

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==================== TABLE CREATION ======================

#----- INSERTING STUDENTS ---------------------------------

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)    #run SQL query

csv_peeps = open("peeps.csv") 
csv_contents = csv.DictReader(csv_peeps)

for record in csv_contents:
    p = 'INSERT INTO students VALUES ("' + record['name'] +  '", "' \
        + record['age'] +  '", "' + record['id'] + '" )'
    c.execute(p)

#----- INSERTING COURSES ----------------------------------

q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)    #run SQL query

csv_courses = open("courses.csv") 
csv_contents = csv.DictReader(csv_courses)

for record in csv_contents:
    p = 'INSERT INTO courses VALUES ("' + record['code'] +  '", "' \
        + record['mark'] +  '", "' + record['id'] + '" )'
    c.execute(p)
#==================== END TABLE CREATION ==================


#==================== FUN STUFF XP ===============

roster = dict()
cap = 10 #HARDCODED FOR TESTING
while cap > 0:
    q = "SELECT AVG(mark) FROM courses WHERE id=" + str(cap)
    c.execute(q)
    avg_grade = c.fetchall()

    q = "SELECT name FROM students WHERE id=" + str(cap)
    c.execute(q)
    name = c.fetchall()

    roster[cap] = [name, avg_grade]
    cap -= 1

for student in roster:
    print student, roster[student]
#==========================================================
db.commit() #save changes
db.close()  #close database


