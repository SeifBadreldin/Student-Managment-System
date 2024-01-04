import json
import os
import csv

def process_menu(items):
        for key in items.keys():
            print("{}:{}".format(key,items[key]))
        print("==============")
        while True:
            choice=(input("enter your choice: "))
            print("==============")
            if choice in items.keys():return choice
            else:
                print("wrong choice , try again !...")

def writeJson(items,filepath):
    file=open(filepath,"w")
    data=json.dumps(items)
    file.write(data)
    file.close()
    return

def ReadJson(filepath):
    if os.path.exists(filepath):
        file=open(filepath,"r")
        data=file.read()
        items=json.loads(data)
        file.close()
        return items
    else:
        return [] 

def entercode(items):
     while True:
        code=(input("enter the code: "))
        if code in items.keys():      
            print("==============")
        print("sorry code not exisit,try again...")
        print("==============")
        return code
     
def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        if data:
            fieldnames = data[0].keys()
        else:
            fieldnames = ['ID', 'Course Code', 'Grade in Numbers', 'Grade in Letters']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def get_valid_code(prompt, dictionary):
    while True:
        code = input(prompt)
        if isinstance(list(dictionary.keys())[0], str):
            code = str(code)
        if code in dictionary.keys():
            return code
        print("Invalid code. Please try again.")

def set_grade():
    while True:
        grade = int(input("Enter grade: "))
        if 0 <= grade <= 100:
            return grade
        print("Invalid grade. Please enter a grade between 0 and 100.")

def calculate_grade_letter(grade):
    if grade >= 95:
        return 'A+'
    elif grade >= 90:
        return 'A'
    elif grade >= 85:
        return 'A-'
    elif grade >= 80:
        return 'B+'
    elif grade >= 75:
        return 'B'
    elif grade >= 70:
        return 'B-'
    elif grade >= 65:
        return 'C+'
    elif grade >= 60:
        return 'C'
    elif grade >= 57:
        return 'C-'
    elif grade >= 54:
        return 'D+'
    elif grade >= 50:
        return 'D'
    else:
        return 'F'