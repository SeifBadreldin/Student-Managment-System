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

def add_course():
    global students
    courses=ReadJson("courses.json")
    course={}
    course["code"]=input("enter code : ")
    course["name"]=input("enter name : ")
    course["Max daegree"]=input("enter Max Degree : ")
    code=course["code"]
    courses[code]=course
    writeJson(courses, "courses.json")
    return

def edit_course():
    global courses
    code=(input("enter the code: "))
    courses=ReadJson("courses.json")
    if code in courses.keys():    
        print("==============")
        course=courses[code]
        course["code"]=input("enter the new code : ")
        course["name"]=input("enter the new name : ")
        course["maxdagree"]=input("enter the new max dagree : ")
        courses[code]=courses
        writeJson(courses, "courses.json")
    else:print("sorry code not exisit,try again...")

def delete_course():
    global courses
    code=(input("enter the code: "))
    courses=ReadJson("courses.json")
    if code in courses.keys():       
        del courses[code]
        writeJson(courses,"courses.json")
    else:
        print("sorry code not exisit,try again...")
