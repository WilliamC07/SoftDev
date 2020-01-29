# Peihua Huang, William Cao (Team Name: PeiCow)
# SoftDev1 pd2
#K18 - Average
# 2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
from collections import namedtuple

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def read_csv_to_database(file_path: str, table_name):
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


def create_tables():
    c.execute("CREATE TABLE IF NOT EXISTS students (name STRING, age INTERGER, id INTERGER PRIMARY KEY);")
    read_csv_to_database("./data/students.csv", "students")

    c.execute("CREATE TABLE IF NOT EXISTS courses (code STRING, mark INTERGER, id INTERGER);")
    read_csv_to_database("./data/courses.csv", "courses")

    c.execute("CREATE TABLE IF NOT EXISTS stu_avg (id INTEGER, average REAL);")


def get_students_grades():
    query = """
    SELECT name, students.id, mark
    FROM students, courses
    WHERE students.id = courses.id;
    """
    query_results = c.execute(query)

    Student = namedtuple("Student", ["name", "grades"])
    # Key: Student ID Value: Student Tuple
    students = {}

    # Use id for dictionary keys since it is guaranteed to be unique
    for name, id, mark in query_results:
        if id not in students:
            students[id] = Student(name, [mark])
        else:
            students[id].grades.append(mark)

    return students


def generate_and_store_averages():
    students = get_students_grades()
    # Calculate and store average
    for student_id in students.keys():
        student = students[student_id]
        average = sum(student.grades) / len(student.grades)
        c.execute("INSERT INTO stu_avg VALUES('{}', {});".format(student_id, average))


def print_averages():
    query = """
    SELECT name, stu_avg.id, average
    FROM students, stu_avg
    WHERE students.id = stu_avg.id
    """
    result = c.execute(query)
    for name, id, average in result:
        print("Name: {} (id: {}) Average: {}".format(name, id, average))


def look_up_grade(id):
    print("Looking up grade for {}: \n".format(id))
    query = """
    SELECT name, students.id, code, mark
    FROM students, courses
    WHERE students.id = courses.id;
    """
    result = c.execute(query)
    for name, student_id, course_name, mark in result:
        if student_id == id:
            print("Student: {} (id {}) \t Course: {} \t Grade: {}".format(name, student_id, course_name, mark))

"""
We will check:
- No single quote in course field
- No non int grade
- User id must exist in db
-
"""
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def ids():
    list = []
    for row in c.execute("SELECT id FROM students"):
        list.append(row[0])
    return list

def add_grade():
    valid = False
    code = input("Enter course code: ")
    while(not valid):
        if (not code or "'" in code):
            # Basic check for sql injection
            code = input("Enter course code without single quotes:")
        else:
            valid = True

    valid = False
    mark = input("Enter mark: ")
    while (not valid):
        if (not is_number(mark)):
            mark = input("Please enter a valid mark: ")
        else:
            valid = True

    valid = False
    id = input("Enter id: ")
    while (not valid):
        if (not is_number(id) or (not int(id) in ids())):
            id = input("Please enter a valid id: ")
        else:
            valid = True
    c.execute("INSERT INTO courses VALUES ('{}', {}, {})".format(code, int(mark), int(id)))


create_tables()
add_grade()
generate_and_store_averages()
print_averages()
look_up_grade(1)
# look_up_grade(int(input("Student's grade to look at: ")))

db.commit()
db.close()
