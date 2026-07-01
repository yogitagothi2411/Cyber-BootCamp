"""
Project: Cyber Security Console
BootCamp Day: 04
Date: 01-07-2026
Author: pyLearner
"""
username="pyLearner0123"
password="Learner0123"
login_attempt=0
login_success=0
login_failed=0
is_Logged_in=False
def line():
  print("========================================================================")

def login():
   global login_attempt, login_failed, login_success, is_Logged_in
   
   if is_Logged_in:
      print("Already Logged in.")
      return
   
   count=0
   logged_in=False

   while count<3: 
      login_attempt+=1
      entered_username=input("Enter your Username : ")
      entered_password=input("Enter your password : ")
      if  entered_username==username and entered_password==password :
        line()
        print("      !! Acess granted !!")
        login_success+=1
        logged_in=True
        is_Logged_in=True
        break
      else :
         print("Invalid credentials")
         login_failed+=1
         count+=1
         logged_in=False
         print(f"Attemp {count}/3")

   if not logged_in:
      print("System Locked")
   line()

def changePswd():
   global password
   if(is_Logged_in):
     old_password=input("Enter your password : ")
     if old_password==password :
        new_password=input("Enter your new password : ")
        confirm_password=input("Enter your new password (to confirm) : ")
        if new_password==confirm_password :
          password=new_password
          print("!! Password Updated !!")
        else:
           print("--- passwords do not match --- ")
     else:
      print("--- Incorrect Password ---")
      line()
      return
   else:
      print("!!! You are not Logged in !!!")
      print("Before change password You need to login ")
   line()

   
def viewLogin():
   print(f"Total Attemp : {login_attempt}")
   print(f"Successful Logins : {login_success}")
   print(f"Failed Attempts : {login_failed}")
   line()

def logout():
   global is_Logged_in
   if is_Logged_in:
      is_Logged_in=False
      print("--- Logged out successfully ---")
   else:
      print("--- You are not logged in ---")
   line()
      

line()
print("         !!! CYBER SECURITY CONSOLE !!!")
line()
choice=1
while choice : 
    print()
    print("===============!!! MENU !!!===============")
    print("1. Login")
    print("2. Change Password")
    print("3. View Login Attempts")
    print("4. Logout")
    print("0. Exit")
    line()
    choice=int(input("Enter Your Choice : "))
    match choice:
        case 0:
          line()
          break
        case 1:
          login()
        case 2:
          changePswd()
        case 3:
          viewLogin()
        case 4:
          logout()
        case _:
          print("!!! Invalid choice !!!")
          
