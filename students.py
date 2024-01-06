from utility import * 

students = {}

def list_students():
    global students
    students = ReadJson("students.json")
    print("students List:")
    print("============")
    for student_code in sorted(students.keys(), reverse=True):
        student= students[student_code]
        print("{}: {}".format(student_code, student["Student name"]))

def add_student():
    global students
    students = ReadJson("students.json")
    student = {}
    while True:
        student_code = input("Enter Student Code: ")
        if not student_code.isdigit() or len(student_code) != 9:
            print("Invalid input. Student Code should be numeric and contain exactly 9 digits.")
        else:
            break
    if student_code in students.keys():
        print("This student already exists.")
    else:
        student["Student Code"] = student_code
        student["Student name"] = input("Enter Student Name: ")
        student["Birthdate"] = input("Enter birthdate: ")
        students[student_code] = student
        writeJson(students, "students.json")
        print("Student added successfully.")

def edit_student():
    global students
    student_code = input("Enter Student Code: ")
    students = ReadJson("students.json")
    if student_code in students.keys():    
        print("==============")
        student = students[student_code]
        student["Student name"] = input("Enter the new Student Name: ").strip().title().replace("  "," ")
        student["Birthdate"] = input("Enter the new birthdate: ").strip()
        students[student_code] = student
        writeJson(students , "students.json")
        print("student edited sucessfully")
    else:
        print("Sorry, the student does not exist. Please try again.")

def view_student():
    global students
    while True:
        student_code = input("Enter Student Code: ")
        students = ReadJson("students.json")
        if student_code in students.keys():       
            print("==============")
            student = students[student_code]
            print("Student Code: {}".format(student["Student Code"]))
            print("Student Name: {}".format(student["Student name"]))
            print("Birthdate: {}".format(student["Birthdate"]))
            break
        else:
             print("Sorry, the student does not exist. Please try again.")
   

def delete_student():
    global students

    student_code = input("Enter Student Code: ")
    students = ReadJson("students.json")
    if student_code in students.keys():       
        del students[student_code]
        writeJson(students,"students.json")
        print("student deleted sucessfully")
    else:
        print("Sorry, the student does not exist. Please try again.")

