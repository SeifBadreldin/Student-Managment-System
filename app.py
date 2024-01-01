from utility import *
from students import *
from courses import *
from grades import*
while True:
    os.system("cls")
    print("============")
    print("Students Mangement System Program")
    print("============")
    main_choice=process_menu({
    "1":"student information",
    "2":"course information",
    "3":"grade informaion" ,
    "4":"Exit"})
    if main_choice == "1":
            liststudents()
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
                elif second_operator==5: break
                input("press any key to continue...")
            else:
                print("wrong choice,try again!...")


    if main_choice=="2":
        liststcourses()
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
            elif second_operator==5: break
            input("press any key to continue...")
        else:
            print("wrong choice,try again!...")


    if main_choice=="3":supply_grades()
    
        




    if main_choice=="4":break
