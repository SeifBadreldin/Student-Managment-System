from utility import *
from students import *
from courses import *
from grades import *
from Results import *
from Analysis import *

while True:
    os.system("cls")
    print("============")
    print("Students Management System Program")
    print("============")
    main_choice=process_menu({
    "1":"Student information",
    "2":"Course information",
    "3":"Grade information" ,
    "4":"Analysis" ,
    "5":"Generate students results" ,
    "6":"Exit"})

    if main_choice == "1":
        list_students()
        print("==============")
        print("1. Add Student")
        print("2. Edit student")
        print("3. View student")
        print("4. delete student")
        print("5. Exit")
        print("==============")
        while True:
            second_operator = input("Enter the operator you need: ")
            if second_operator.isdigit() and 1 <= int(second_operator) <= 5:
                second_operator = int(second_operator)
                if second_operator==1:add_student()
                elif second_operator==2:edit_student()
                elif second_operator==3:view_student()
                elif second_operator==4:delete_student()
                elif second_operator==5: break
                input("press any key to continue...")
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

    if main_choice=="2":
        list_courses()
        print("==============")
        print("Student Management System Operation ")
        print("==============")
        print("1. Add Course")
        print("2. Edit Course")
        print("3. View Course")
        print("4. delete Course")
        print("5. Exit")
        print("==============")
        while True:
            second_operator = input("Enter the operator you need: ")
            if second_operator.isdigit() and 1 <= int(second_operator) <= 5:
                second_operator = int(second_operator)
                if second_operator==1:add_course()
                elif second_operator==2:edit_course()
                elif second_operator==3:view_course()
                elif second_operator==4:delete_course()
                elif second_operator==5: break
                input("press any key to continue...")
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

    if main_choice=="3":
         print("==============")
         print("Student Management System Operation ")
         print("==============")
         print("1. Add Grade")
         print("2. Edit Grade")
         print("3. View Grade")
         print("4. delete Grade")
         print("5. Exit")
         print("==============")
         while True:
             second_operator = input("Enter the operator you need: ")
             if second_operator.isdigit() and 1 <= int(second_operator) <= 5:
                second_operator = int(second_operator)
                if second_operator==1:add_grade()
                elif second_operator==2:edit_grade()
                elif second_operator==3:view_grade()
                elif second_operator==4:delete_grade()
                elif second_operator==5: break
                input("press any key to continue...")
             else:
                print("Invalid input. Please enter a number between 1 and 5.")

    if main_choice=="4":
         print("==============")
         print("Student Management System Operation ")
         print("==============")
         print("1. Student results per course (Bar Chart)")
         print("2. Course Registeration (Pie Chart)")
         print("3. Exit")
         print("==============")
         while True:
             second_operator = input("Enter the operator you need: ")
             if second_operator.isdigit() and 1 <= int(second_operator) <= 3:
                second_operator = int(second_operator)
                if second_operator==1:Bar_chart(results)
                elif second_operator==2:Pie_chart()
                elif second_operator==3: break
                input("press any key to continue...")
             else:
                print("Invalid input. Please enter a number between 1 and 3.")

    if main_choice=="5": Generate_Results()
    
    
    if main_choice=="6":break
    