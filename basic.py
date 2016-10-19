# Team DasMeme -- Alan Chen, Jason Mohabir, Haley Zeng
# SoftDev pd8
# HW08 -- Average
# 2016-10-18

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


roster = dict()
cap = 10
while cap > 0:
    q = "SELECT AVG(mark) FROM courses WHERE id=" + str(cap)
    c.execute(q)
    avg_grade = c.fetchone()[0]

    q = "SELECT name FROM students WHERE id=" + str(cap)
    c.execute(q)
    name = c.fetchone()[0]

    roster[cap] = [name, avg_grade]
    cap -= 1

for ID in roster:
    print roster[ID][0], ID, roster[ID][1]

db.commit() #save changes
db.close()  #close database
