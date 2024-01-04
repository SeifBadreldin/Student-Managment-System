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
    WriteCsv("grades.csv", data.keys(), data)
    print("Grade Added Successfully")

def edit_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code to edit grade: ", students)
    course_code = get_valid_code("Enter course code to edit grade: ", courses)
    grade = set_grade()
    grade_letter = calculate_grade_letter(grade)
    data = {"Name": students[student_code]["name"], "ID": student_code, "Course Code": course_code, "Course Name": courses[course_code]["name"], "Grade": f"{grade}%", "Grade Letter": grade_letter}
    WriteCsv("grades.csv", data.keys(), data)
    print("Grade Edited Successfully")


    
def view_grade():

    grades = ReadCsv('grades.csv')
    for row in grades:
        print(row)
    grades = ReadCsv('grades.csv')
    for row in grades:
        if row[1] == student_code and row[2] == course_code:
            row[4] = f"{grade}%"
            row[5] = grade_letter
            break
    WriteCsv('grades.csv', grades[0].keys(), grades)
    print("Grade Edited Successfully")

def delete_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code to delete grade: ", students)
    course_code = get_valid_code("Enter course code to delete grade: ", courses)
    grades = ReadCsv('grades.csv')
    grades = [row for row in grades if not (row[1] == student_code and row[2] == course_code)]
    WriteCsv('grades.csv', grades[0].keys(), grades)
    print("Grade Deleted Successfully")
