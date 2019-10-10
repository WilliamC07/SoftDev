# Team Name: PeiCow

# 2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


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
            db.execute("INSERT INTO {} VALUES ('{}', {}, {});".format(table_name, *values))


db.execute("CREATE TABLE IF NOT EXISTS students (name STRING, age INTERGER, id INTERGER PRIMARY KEY);")
put_data_in("./data/students.csv", "students")
db.execute("CREATE TABLE IF NOT EXISTS courses (code STRING, mark INTERGER, id INTERGER);")
put_data_in("./data/courses.csv", "courses")

query = """
select name, students.id, mark
from students, courses
where students.id = courses.id;
"""

result = c.execute(query)
for i in result:
    print(i)

db.commit() #save changes
db.close()  #close database
