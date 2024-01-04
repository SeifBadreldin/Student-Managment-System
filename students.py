from utility import * 
import os

students={}

def liststudents():
    global students
    students=ReadJson("students.json")
    print("students list")
    print("============")
    for code in students.keys():
        student=students[code]
        print("{}:{}".format(code,student["name"]))

def add_student():
    global students
    students = ReadJson("students.json")
    student = {}
    student_code = input("Enter code: ")
    if student_code in students.keys():
        print("This student already exists.")
    else:
        student["code"] = student_code
        student["name"] = input("Enter name: ")
        student["Birthdate"] = input("Enter Birthdate: ")
        students[student_code] = student
        writeJson(students, "students.json")
        print("Student Added Successfully")

def edit_student():
    global students
    code=(input("enter the code: "))
    students=ReadJson("students.json")
    if code in students.keys():    
        print("==============")
        student=students[code]
        student["name"]=input("enter the new name : ").strip().title().replace("  "," ")
        student["Birthdate"]=input("enter the new Birthdate : ").strip()
        students[code]=student
        writeJson(students , "students.json")
    else:
        print("sorry code not exisit,try again...")

def view_student():
    global students
    while True:
        code=(input("enter the code: "))
        students=ReadJson("students.json")
        if code in students.keys():       
            print("==============")
            student = students[code]
            print("code:{}".format(student["code"]))
            print("name:{}".format(student["name"]))
            print("Birthdate:{}".format(student["Birthdate"]))
            break
        else:
             print("sorry code not exisit,try again...")
   

def delete_student():
    global students

    code=(input("enter the code: "))
    students=ReadJson("students.json")
    if code in students.keys():       
        del students[code]
        writeJson(students,"students.json")
    else:
        print("sorry code not exisit,try again...")