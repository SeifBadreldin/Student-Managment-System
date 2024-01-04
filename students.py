from utility import * 
import os

students = {}

def list_students():
    global students
    students = ReadJson("students.json")
    print("Student List:")
    print("============")
    for student_code in students.keys():
        student = students[student_code]
        print("{}: {}".format(student_code, student["Student Name"]))

def add_student():
    global students
    students = ReadJson("students.json")
    student = {}
    student_code = input("Enter student code: ")
    if student_code in students.keys():
        print("This student already exists.")
    else:
        student["Student Code"] = student_code
        student["Studennt Name"] = input("Enter Student Name: ")
        student["Birthdate"] = input("Enter birthdate: ")
        students[student_code] = student
        writeJson(students, "students.json")
        print("Student added successfully.")

def edit_student():
    global students
    student_code = input("Enter student code: ")
    students = ReadJson("students.json")
    if student_code in students.keys():    
        print("==============")
        student = students[student_code]
        student["Student Name"] = input("Enter the new Student Name: ").strip().title().replace("  "," ")
        student["Birthdate"] = input("Enter the new birthdate: ").strip()
        students[student_code] = student
        writeJson(students , "students.json")
    else:
        print("Sorry, the student does not exist. Please try again.")

def view_student():
    global students
    while True:
        student_code = input("Enter student code: ")
        students = ReadJson("students.json")
        if student_code in students.keys():       
            print("==============")
            student = students[student_code]
            print("Student Code: {}".format(student["Student Code"]))
            print("Student Name: {}".format(student["Student Name"]))
            print("Birthdate: {}".format(student["Birthdate"]))
            break
        else:
             print("Sorry, the student does not exist. Please try again.")
   

def delete_student():
    global students

    student_code = input("Enter student code: ")
    students = ReadJson("students.json")
    if student_code in students.keys():       
        del students[student_code]
        writeJson(students,"students.json")
    else:
        print("Sorry, the student does not exist. Please try again.")
