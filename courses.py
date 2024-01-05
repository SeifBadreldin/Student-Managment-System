from utility import *
import os

courses = {}

def list_courses():
    global courses
    courses = ReadJson("courses.json")
    print("Course List:")
    print("============")
    for course_code in courses.keys():
        course = courses[course_code]
        print("{}: {}".format(course_code, course["Course name"]))

def add_course():
    global courses
    courses = ReadJson("courses.json")
    course = {}
    course_code = input("Enter course code: ")
    if course_code in courses.keys():
        print("This course already exists.")
    else:
        course["code"] = course_code
        course["Course name"] = input("Enter Course name: ")
        course["Max Degree"] = input("Enter max degree: ")
        courses[course_code] = course
        writeJson(courses, "courses.json")
        print("Course has been added successfully.")

def edit_course():
    global courses
    course_code = input("Enter course code: ")
    courses = ReadJson("courses.json")
    if course_code in courses.keys():    
        print("==============")
        course = courses[course_code]
        course["Course name"] = input("Enter the new course name: ").strip().title().replace("  "," ")
        course["Max Degree"] = input("Enter the new max degree: ").strip()
        courses[course_code] = course
        writeJson(courses , "courses.json")
    else:
        print("Sorry, the course does not exist. Please try again.")

def view_course():
    global courses
    while True:
        course_code = input("Enter course code: ")
        courses = ReadJson("courses.json")
        if course_code in courses.keys():       
            print("==============")
            course = courses[course_code]
            print("Course Code: {}".format(course["Course code"]))
            print("course Name: {}".format(course["Course name"]))
            print("Max Degree: {}".format(course["max degree"]))
            break
        else:
             print("Sorry, the course does not exist. Please try again.")
   

def delete_course():
    global courses

    course_code = input("Enter course code: ")
    courses = ReadJson("courses.json")
    if course_code in courses.keys():       
        del courses[course_code]
        writeJson(courses,"courses.json")
    else:
        print("Sorry, the course does not exist. Please try again.")
