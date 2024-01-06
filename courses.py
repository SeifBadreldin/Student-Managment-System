from utility import * 

courses = {}

def list_courses():
    global courses
    courses = ReadJson("courses.json")
    print("Course List:")
    print("============")
    for course_code in sorted(courses.keys(), reverse=True):
        course = courses[course_code]
        print("{}: {}".format(course_code, course["Course name"]))

def add_course():
    global courses
    courses = ReadJson("courses.json")
    course = {}
    while True:
        course_code = input("Enter course code: ").upper()
        if len(course_code) != 6:
            print("Invalid input. Course code should contain exactly 6 characters.")
        else:
            break
    if course_code in courses.keys():
        print("This course already exists.")
    else:
        course["code"] = course_code
        course["Course name"] = input("Enter Course name: ")
        course["Credit Hours"] = input("Enter Credit Hours: ")
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
        course["Credit Hours"] = input("Enter Credit Hours: ").strip()
        course["Max Degree"] = input("Enter the new max degree: ").strip()
        courses[course_code] = course
        writeJson(courses , "courses.json")
        print("course edited sucssefully")
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
            print("Course Code: {}".format(course["code"]))
            print("Course Name: {}".format(course["Course name"]))
            print("Credit Hours: {}".format(course["Credit Hours"]))
            print("Max Degree: {}".format(course["Max Degree"]))
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
        print("course deleted sucssefully")
    else:
        print("Sorry, the course does not exist. Please try again.")