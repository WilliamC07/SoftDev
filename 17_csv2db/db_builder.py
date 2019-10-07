#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


# Handle students.csv
db.execute("CREATE TABLE IF NOT EXISTS students (name STRING, age INTERGER, id INTERGER PRIMARY KEY);")
with open("./data/students.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        name = row['name']
        age = int(row['age'])
        student_id = int(row['id'])
        db.execute("INSERT INTO students (name, age, id) VALUES ('{}', {}, {});".format(name, age, student_id))

db.commit() #save changes
db.close()  #close database
