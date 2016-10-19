# Team DasMeme: Alan Chen, Jason Mohabir, Haley Zeng
# Softdev pd8
# HW08 -- Average
# 2016-10-18

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==================== STUDENT'S AVERAGES ===============

def averageGrades(ID):
    q = "SELECT mark FROM courses WHERE id = '%s'" % (ID)
    c.execute(q)
    grades = c.fetchall() #grades is a list of tuples
    summ = 0.0 #avoid integer division
    count = 0;
    for grade in grades: #grade is a tuple
        summ += grade[0] #get the mark from the tuple
        count += 1
    return summ / count

#================== DISPLAYING STUDENT DATA  ===============

q = "SELECT name, id FROM students"
c.execute(q)
people = c.fetchall()

for person in people:
    name = person[0]
    ID = person[1]
    avg = averageGrades(ID)
    print name, ID, avg


db.commit() #save changes
db.close()  #close database
