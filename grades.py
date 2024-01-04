import csv
from students import *
from courses import *
from utility import *

def get_valid_code(prompt, dictionary):
    while True:
        code = input(prompt)
        if isinstance(list(dictionary.keys())[0], str):
            code = str(code)
        if code in dictionary.keys():
            return code
        print("Invalid code. Please try again.")

def set_grade():
    while True:
        grade = int(input("Enter grade: "))
        if 0 <= grade <= 100:
            return grade
        print("Invalid grade. Please enter a grade between 0 and 100.")

def calculate_grade_letter(grade):
    if grade >= 95:
        return 'A+'
    elif grade >= 90:
        return 'A'
    elif grade >= 85:
        return 'A-'
    elif grade >= 80:
        return 'B+'
    elif grade >= 75:
        return 'B'
    elif grade >= 70:
        return 'B-'
    elif grade >= 65:
        return 'C+'
    elif grade >= 60:
        return 'C'
    elif grade >= 57:
        return 'C-'
    elif grade >= 54:
        return 'D+'
    elif grade >= 50:
        return 'D'
    else:
        return 'F'

import csv
from students import *
from courses import *
from utility import *

def add_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    grade = set_grade()
    grade_letter = calculate_grade_letter(grade)
    data = {"ID": student_code, "Course Code": course_code, "Grade": grade_letter}
    filename = f"{course_code}.csv"
    file_exists = os.path.isfile(filename)
    if file_exists:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ID"] == student_code and row["Course Code"] == course_code:
                    print("This student already has a grade for this course.")
                    return
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    print("Grade Added Successfully")

def edit_grade():
  students

def view_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    grades = ReadCsv(f"{course_code}.csv")
    for row in grades:
        if row["ID"] == student_code and row["Course Code"] == course_code:
            print("ID: {}".format(row["ID"])) 
            print("Course Code: {}".format(row["Course Code"]))
            print("Grade Letter: {}".format(row["Grade Letter"]))
            break
    else:
        print("No matching grade found.")

def delete_grade():
     students

     