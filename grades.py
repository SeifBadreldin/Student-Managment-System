import csv
from students import *
from courses import *
from utility import *

def add_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    filename = f"{course_code}.csv"
    if os.path.isfile(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ID"] == student_code and row["Course Code"] == course_code:
                    print("This student already has a grade for this course.")
                    return
    Grade_Number = set_grade()
    Grade_Letter = calculate_grade_letter(Grade_Number)
    data = {"ID": student_code, "Course Code": course_code, "Grade in Numbers": Grade_Number, "Grade in Letters": Grade_Letter}
    writetocsv(filename, data)
    print("Grade Added Successfully")


def edit_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    filename = f"{course_code}.csv"
    if os.path.isfile(filename):
        data = read_csv(filename)
        for row in data:
            if row["ID"] == student_code and row["Course Code"] == course_code:
                print("==============")
                print("Current grade: ", row["Grade in Numbers"])
                Grade_Number = set_grade()
                row["Grade in Numbers"] = Grade_Number
                row["Grade in Letters"] = calculate_grade_letter(Grade_Number)  
        write_csv(filename, data)
        print("Grade Edited Successfully")
    else:
        print("No grades found for this course.")

def view_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code: ", students)
    course_code = get_valid_code("Enter course code: ", courses)
    filename = f"{course_code}.csv"
    if os.path.isfile(filename):
        data = read_csv(filename)
        for row in data:
            if row["ID"] == student_code and row["Course Code"] == course_code:
                print("==============")
                print("Student Code:", row["ID"])
                print("Course Code:", row["Course Code"])
                print("Grade in Numbers:", row["Grade in Numbers"])
                print("Grade in Letters:", row["Grade in Letters"])
                print("==============")
                return
    print("No grade found for this student in this course.")

def delete_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code:", students)
    course_code = get_valid_code("Enter course code:", courses)
    filename = f"{course_code}.csv"
    if os.path.isfile(filename):
        data = read_csv(filename)
        new_data = [row for row in data if not (row["ID"] == student_code and row["Course Code"] == course_code)]
        if not new_data:
            new_data = [{}]
        write_csv(filename, new_data)
        print("Grade Deleted Successfully")
    else:
        print("No grades found for this course.")
