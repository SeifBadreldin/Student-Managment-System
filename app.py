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
            second_operator=int(input("enter the operator you need: "))
            if second_operator>=1 and second_operator<=5:
                if second_operator==1:add_student()
                elif second_operator==2:edit_student()
                elif second_operator==3:view_student()
                elif second_operator==4:delete_student()
                elif second_operator==5: continue
                input("press any key to continue...")
            else:
                print("wrong choice,try again!...")


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
        second_operator=int(input("enter the operator you need: "))
        if second_operator>=1 and second_operator<=5:
            if second_operator==1:add_course()
            elif second_operator==2:edit_course()
            elif second_operator==3:view_course()
            elif second_operator==4:delete_course()
            elif second_operator==5: continue
            input("press any key to continue...")
        else:
            print("wrong choice,try again!...")


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
         second_operator=int(input("enter the operator you need: "))
         if second_operator>=1 and second_operator<=5:
            if second_operator==1:add_grade()
            elif second_operator==2:edit_grade()
            elif second_operator==3:view_grade()
            elif second_operator==4:delete_grade()
            elif second_operator==5: continue
            input("press any key to continue...")
         else:
            print("wrong choice,try again!...")

    if main_choice=="4":
         print("==============")
         print("Student Management System Operation ")
         print("==============")
         print("1. Student result per course (Bar Chart)")
         print("2. Course Registeration (Pie Chart)")
         print("3. Exit")
         print("==============")
        #  second_operator=int(input("enter the operator you need: "))
        #  if second_operator>=1 and second_operator<=5:
        #     if second_operator==1:Bar_chart()
        #     elif second_operator==2:Pie_Chart()
        #     elif second_operator==3: continue
        #     input("press any key to continue...")
        #  else:
        #     print("wrong choice,try again!...")

    if main_choice=="5": Generate_Results()
    print("Results are successfully generated")   
    input("press any key to continue...")
    
    if main_choice=="6":break


