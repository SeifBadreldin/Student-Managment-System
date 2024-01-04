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
                print("Current grade: ", calculate_grade_number(row["Grade"]))
                grade = set_grade()
                grade_letter = calculate_grade_letter(grade)
                row["Grade"] = grade_letter
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
                print("Grade:", row["Grade"])
                print("==============")
                return
    print("No grade found for this student in this course.")

def delete_grade():
    students = ReadJson("students.json")
    courses = ReadJson("courses.json")
    student_code = get_valid_code("Enter student code:", students)
    course_code = get_valid_code("Enter course code", courses)
    filename = f"{course_code}.csv"
    if os.path.isfile(filename):
        data = read_csv(filename)
        new_data = [row for row in data if not (row["ID"] == student_code and row["Course Code"] == course_code)]
        write_csv(filename, new_data)
        print("Grade Deleted Successfully")
    else:
        print("No grades found for this course.")
