"""
Project: Student Record Manager
BootCamp Day: 06
Date: 04-07-26
Author: pyLearner
"""
def line():
   print("====================================================================================")

from datetime import date, datetime
def date_time():
     today= date.today()
     current_time = datetime.now().time()
     print(f"Date : {today}")
     print(f"Time : {current_time.strftime('%H:%M:%S')}")


def header():
    line()
    print("              :::: WELCOME TO STUDENT RECORD SYSTEM ::::")
    line()
    date_time()
   


def menu():
    line()
    print("Functionalities : ")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Count Total Student")
    print("6. Show Deleted Record ")
    print("0. Exit")
    line()
    choice=int(input("Enter your choice : "))
    line()
    return choice




def print_student(student):
   print(f"Roll no. : {student[0]}")
   print(f"Name     : {student[1]}")
   print(f"Class    : {student[2]}")
   print(f"Father   : {student[3]}")
   print(f"Mother   : {student[4]}")
   print(f"Contact  : {student[5]}")


def print_list(student):
    print(f"{student[0]} || {student[1]} ||  {student[2]} ||  {student[3]} ||  {student[4]} ||  {student[5]}")
         

def add_student():
 while True:
     roll_number = students[-1][0]+1
     name=input("Enter student name :")
     class_name=input("Enter Student class with section : ")
     father=input("Enter Student Father full name : ")
     mother=input("Enter Student mother full name : ")
     contact=input("Enter student contact number : ")
     new_student=[
         roll_number,
         name,
         class_name,
         father,
         mother,
         contact
     ]
     students.append(new_student)
     confirm=input(" Add more student detail (y/n) : ")
     if confirm=="n":
         break
     



def view_all_Student():
    print("Roll :  Name        : Class  : Father         : Mother         : Contact  ")
    for student in students:
         print_list(student)




def search_with_name():
    is_found=False
    name=input("Enter student full name : ")
    line()
    for student in students:
       if student[1].lower() == name.lower():
          is_found=True
          print("Record found : ")
          print_student(student)
          break
    if  not is_found:
      print("Record not Found")


   
def search_with_roll_no():
   is_found=False
   roll_no=int(input("Enter student roll number : "))
   line()
   for student in students:
       if student[0]== roll_no:
          is_found=True
          print("Record found : ")
          print_student(student)
          break
   if  not is_found:
      print("Record not Found")


def search_for_class_stdnt():
   is_found=False
   class_name=input("Enter Class : ")
   print("Roll :  Name        : Class  : Father         : Mother         : Contact  ")
   for student in students:
       if student[2]== class_name:
          is_found=True
          print_list(student)
         
   if  not is_found:
      print("Record not Found")
       

def search_student():
    print("1. Search with Name")
    print("2. Search with Roll number")
    print("3. Search  class Student list  ")
    line()
    option=int(input("Enter Your choice : "))
    line()
    match option:
       case 1:
          search_with_name()
       case 2:
          search_with_roll_no()
       case 3:
          search_for_class_stdnt()
       case _:
          print("Invalid choice")
    line()




def remove_student():
    global is_delete
    isfound=False
    roll=int(input("Enter student roll number : "))
    confirm = input("you want to delete this student info from record (y/n) : ")
    if confirm.lower()=="y":
       for student in students:
         if student[0]==roll:
           isfound=True
           deleted_students.append(student)
           students.remove(student)
           print("Deleted student record")
           break
       if not isfound:
          print("Record not found")
    else:
       return
   




def count_total_student():
    count=len(students)
    print(f"Number of student : {count}")



def show_deleted_record():
  # []list == False
  if deleted_students:
     print("Roll :  Name        : Class  : Father         : Mother         : Contact  ")
     for student in deleted_students:
        print_list(student)
  else:
     print("No record are Deleted")


   # RollNo., Name, class, father , mother, contact no.
students = [
    [101, "Aarav Sharma", "10A", "Rajesh Sharma", "Sunita Sharma", "9876543210"],
    [102, "Ananya Verma", "10A", "Rakesh Verma", "Pooja Verma", "9123456780"],
    [103, "Vivaan Patel", "10B", "Mahesh Patel", "Neeta Patel", "9988776655"],
    [104, "Diya Singh", "10B", "Sanjay Singh", "Kavita Singh", "9012345678"],
    [105, "Aditya Gupta", "10C", "Amit Gupta", "Rekha Gupta", "9898989898"],
    [106, "Ishita Mehta", "10C", "Deepak Mehta", "Anjali Mehta", "9765432109"],
    [107, "Krish Yadav", "10A", "Ramesh Yadav", "Sushma Yadav", "9871203456"],
    [108, "Myra Joshi", "10B", "Vikas Joshi", "Nidhi Joshi", "9900112233"],
    [109, "Arjun Nair", "10C", "Suresh Nair", "Lakshmi Nair", "9812345670"],
    [110, "Sara Khan", "10A", "Imran Khan", "Farah Khan", "9955667788"]
]
deleted_students=[]

header()
choice=1
while choice:
    choice=menu()
    match choice :
     case 0:
        print("Thankyou for visting.")
        line()
        break
     case 1:
        add_student()
     case 2:
        view_all_Student()
     case 3:
        search_student()
     case 4:
        remove_student()
     case 5:
        count_total_student()
     case 6:
        show_deleted_record()
     case _:
        print("Invalid Choice")
    
