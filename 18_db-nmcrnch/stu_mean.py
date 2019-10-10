# Peihua Huang, William Cao (Team Name: PeiCow)
# SoftDev1 pd2
#K18 - Average
# 2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

course_code = input("Enter course code: ")
course_mark = input("Enter mark: ")
course_id = input("Enter id: ")

def put_data_in(file_path: str, table_name):
    """
    Reads a csv file with three columns and enters into a table. Table must exist already
    :param file_path: Path to csv file to enter data in. The csv should only have 3 columns
    :param table_name: Name of table
    """
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            values = list(row.values())
            c.execute("INSERT INTO {} VALUES ('{}', {}, {});".format(table_name, *values))


c.execute("CREATE TABLE IF NOT EXISTS students (name STRING, age INTERGER, id INTERGER PRIMARY KEY);")
put_data_in("./data/students.csv", "students")
c.execute("CREATE TABLE IF NOT EXISTS courses (code STRING, mark INTERGER, id INTERGER);")
put_data_in("./data/courses.csv", "courses")
c.execute("INSERT INTO courses VALUES ('{}', {}, {})".format(course_code, course_mark, course_id))

c.execute("CREATE TABLE IF NOT EXISTS stu_avg (name STRING, id INTEGER, ave INTEGER);")

query = """
SELECT name, students.id, mark
FROM students, courses
WHERE students.id = courses.id;
"""
result = c.execute(query)

dict = {}

for name, id, mark in result:
    if (name not in dict):
        dict[name] = [int(id), int(mark), 1]
    else:
        dict[name] = [dict[name][0], dict[name][1] + int(mark), dict[name][2] + 1]

for row in dict:
    c.execute("INSERT INTO stu_avg VALUES(\"{}\", {}, {});".format(row, dict[row][0], dict[row][1]/dict[row][2]))

table = c.execute("SELECT * FROM stu_avg")
for row in table:
    print(row)

db.commit() #save changes
db.close()  #close database
