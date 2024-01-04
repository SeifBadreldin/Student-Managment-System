from utility import *

courses={}

def liststcourses():
    global courses
    courses=ReadJson("courses.json")
    print("courses list")
    print("============")
    for code in courses.keys():
        course=courses[code]
        print("{}:{}".format(code,course["name"]))

def add_course():
    courses = ReadJson("courses.json")
    course = {}
    course_code = input("Enter code: ")
    if course_code in courses.keys():
        print("This course already exists.")
    else:
        course["code"] = course_code
        course["name"] = input("Enter name: ")
        course["Max degree"] = input("Enter Max Degree: ")
        courses[course_code] = course
        writeJson(courses, "courses.json")
        print("Course Added Successfully")

def edit_course():
    global courses
    code=(input("enter the code: "))
    courses=ReadJson("courses.json")
    if code in courses.keys():    
        print("==============")
        course=courses[code]
        course["name"]=input("enter the new name : ").strip().title().replace("  "," ")
        course["maxdaegree"]=input("enter the new maxdagree: ").strip()
        courses[code]=course
        writeJson(courses,"courses.json")
    else:
        print("sorry code not exisit,try again...")

def view_course():
    global courses
    while True:
        code=(input("enter the code: "))
        courses=ReadJson("courses.json")
        if code in courses.keys():       
            print("==============")
            course = courses[code]
            print("code:{}".format(course["code"]))
            print("name:{}".format(course["name"]))
            print("Max degree:{}".format(course["maxdegree"]))
            break
        else:
             print("sorry code not exisit,try again...")

def delete_course():
    global courses
    code=(input("enter the code: "))
    courses=ReadJson("courses.json")
    if code in courses.keys():       
        del courses[code]
        writeJson(courses,"courses.json")
    else:
        print("sorry code not exisit,try again...")