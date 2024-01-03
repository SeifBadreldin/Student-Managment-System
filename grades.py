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

def add_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    grade = set_grade()
    grade_letter = calculate_grade_letter(grade)
    data = {"Name": students[student_code]["name"], "ID": student_code, "Course Code": course_code, "Course Name": courses[course_code]["name"], "Grade": f"{grade}%", "Grade Letter": grade_letter}
    write_csv("grades.csv", data.keys(), data)
    print("Grade Added Successfully")


def edit_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    new_grade = set_grade()
    new_grade_letter = calculate_grade_letter(new_grade)
    grades = []
    student_exists = False
    course_exists = False
    with open('grades.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == student_code:
                student_exists = True
                if row["Course Code"] == course_code:
                    course_exists = True
                    row["Grade"] = f"{new_grade}%"
                    row["Grade Letter"] = new_grade_letter
            grades.append(row)
    if not student_exists:
        print("Student not found in the file.")
        return
    if not course_exists:
        print("The student has not taken this course.")
        return
    write_csv('grades.csv', grades[0].keys(), grades)
    print("Grade Edited Successfully")

def view_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    grades = read_csv('grades.csv')
    for grade in grades:
        if grade["ID"] == student_code and grade["Course Code"] == course_code:
            print(f"Student Name: {grade['Name']}")
            print(f"Course Name: {grade['Course Name']}")
            print(f"Grade: {grade['Grade']}")
            print(f"Grade Letter: {grade['Grade Letter']}")
            return
    print("No grade found for this student in this course.")

def delete_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    grades = []
    student_exists = False
    course_exists = False
    with open('grades.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == student_code:
                student_exists = True
                if row["Course Code"] == course_code:
                    course_exists = True
                else:
                    grades.append(row)
    if not student_exists:
        print("Student not found in the file.")
        return
    if not course_exists:
        print("The student has not taken this course.")
        return
    write_csv('grades.csv', grades[0].keys(), grades)
    print("Grade Deleted Successfully")
