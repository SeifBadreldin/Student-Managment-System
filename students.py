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
            print("age:{}".format(student["age"]))
            print("country:{}".format(student["country"]))
            break
        else:
             print("sorry code not exisit,try again...")
   

def add_student():
    global students
    students=ReadJson("students.json")
    student={}
    student["name"]=input("enter name : ")
    student["code"]=input("enter code : ")
    student["Birthdate"]=input("enter Birthdate : ")
    student["age"]=input("enter age : ")
    student["country"]=input("enter country : ")
    code=student["code"]
    students[code]=student
    writeJson(students , "students.json")
    return

def edit_student():
    global students
    code=(input("enter the code: "))
    students=ReadJson("students.json")
    if code in students.keys():    
        print("==============")
        student=students[code]
        student["name"]=input("enter the new name : ").strip().title().replace("  "," ")
        student["Birthdate"]=input("enter the new Birthdate : ").strip()
        student["age"]=input("enter the new age : ").strip()
        student["country"]=input("enter the new country : ").strip().capitalize()
        students[code]=student
        writeJson(students , "students.json")
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