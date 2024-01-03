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
     
def WriteCsv(filename, fieldnames, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)

def ReadCsv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)
