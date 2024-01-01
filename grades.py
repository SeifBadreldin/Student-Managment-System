from students import *
from courses import *
from utility import *
def supply_grades():
    courses = ReadJson("courses.json")

    students = ReadJson("students.json")

    grades_data = {}

    course_code = input("Supply Grades,Enter course code to supply grades:")
    if course_code not in courses:
        print("Course not found.")
        return

    min_grade = 0
    max_grade = 100

    for student in students:
        grade = int(input("Supply Grades,Enter grade for:"))
        precentage = 100*grade/max_grade
        if grade>=95:
            print("You succeeded with A+ grade with percentage",precentage,"%")
        elif grade>=90:
            print("You succeeded with A grade with percentage",precentage,"%")
        elif grade>=85:
            print("You succeeded with A- grade with percentage",precentage,"%")
        elif grade>=80:
            print("You succeeded with B+ grade with percentage",precentage,"%")
        elif grade>=75:
            print("You succeeded with B grade with percentage",precentage,"%")
        elif grade>=70:
            print("You succeeded with B- grade with percentage",precentage,"%")
        elif grade>=65:
            print("You succeeded with C+ grade with percentage",precentage,"%")
        elif grade>=60:
            print("You succeeded with C grade with percentage",precentage,"%")
        elif grade>=57:
            print("You succeeded with C- grade with percentage",precentage,"%")
        elif grade>=54:
            print("You succeeded with D+ grade with percentage",precentage,"%")
        elif grade>=50:
            print("You succeeded with D grade with percentage",precentage,"%")
        else:
            print("You failed with F grade with percentage",precentage,"%")
            if grade < min_grade or grade > max_grade:
                print("Invalid grade. Please enter a grade between 0 and 100.")
                continue
            if course_code not in grades_data:
                grades_data[course_code] = []
            grades_data[course_code].append({'Student Code': student['code'], 'Grade': grade})

    print("Grades supplied successfully.")
    writecsv(grades_data, "grades.csv")