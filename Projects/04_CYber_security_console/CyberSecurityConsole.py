"""
Project: Cyber Security Console
update-User Authentication Manager
BootCamp Day: 04 / 07
Date: 01-07-2026 /05-07-2026
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


def header():
    line()
    print("         !!! CYBER SECURITY CONSOLE !!!")
    line()
      

def menu():
    print()
    print("===============!!! MENU !!!===============")
    print(" 1. Add User")
    print(" 2. Remove User")
    print(" 3. Search User")
    print(" 4. Login")
    print(" 5. Lock Account")
    print(" 6. Unlock Account")
    print(" 7. Change Password")
    print(" 8. View All User ")
    print(" 9. Count Users ")
    print("10. Failed Login Tracking")
    print("11. Logout")
    print("0. Exit")
    line()
    choice=int(input("Enter Your Choice : "))
    return choice


def print_user(user):
   print(f"User Id       : {user[0]}")
   print(f"username      : {user[1]}")
   print(f"password      : {user[2]}")
   print(f"Role          : {user[3]}")
   print(f"Status        : {user[4]}")
   print(f"Failed Attemp : {user[5]}")


def print_list(user):
    print(f"{user[0]} || {user[1]} ||  {user[2]} ||  {user[3]} ||  {user[4]} ||  {user[5]}")
         


def admin_check(entered_role):
   if entered_role.lower()=="admin":
        entered_pin=input("Enter Admin pin : ")
        if entered_pin==admin_pin:
          return True
        else:
           print("Invalid pin")
           return False
        
        
def manager_check(entered_role):
   if entered_role.lower()=="manager":
        entered_pin=input("Enter Manager pin : ")
        if entered_pin==manager_pin:
          return True
        else:
           print("Invalid pin")
           return False

def add_user():
     if users:
       userId = users[-1][0]+1
     else:
        userId=101
     while True:
      entered_username=input("Enter Username :")
      found=False
      for user in users:
       if(entered_username==user[1]):
          print("User name already exist\n change username")
          found=True
          break
      if not found:
         break
     username=entered_username
     password=input("Enter Password : ")
     entered_role = input("Enter Role : ")
     if admin_check(entered_role):
           role=entered_role.lower()
     elif manager_check(entered_role):
           role=entered_role.lower()
     elif entered_role.lower()=="user": 
          role=entered_role.lower()
     else:
        print("Invalid role") 
        return 
     status = "Inactive"
     loginattemp=0 
     new_user=[
         userId,
         username,
         password,
         role,
         status,
         loginattemp
     ]
     users.append(new_user)
     print("User added succesfully")
    
     
 

def remove_user():
    is_delete=False
    isfound=False
    userId=int(input("Enter userId you want delete : "))
    entered_role = input("Enter Role : ")
    if entered_role.lower()!="admin":
       print("Admin can only allowed to delete")
       return
    if admin_check(entered_role):
       confirm = input("you want to delete this user info from record (y/n) : ")
       if confirm.lower()=="y":
          for user in users:
            if user[0]==userId:
              isfound=True
              deleted_users.append(user)
              users.remove(user)
              is_delete=True
              print("Deleted user record")
              break
          if not isfound:
             print("Record not found")
       else:
          return
    else:
       print("Invalid pin")
    return is_delete



def search_user():
   is_found=False
   entered_role = input("Enter Role : ")
   if entered_role.lower()!="admin" and entered_role.lower()!="manager":
       print("Admin and manager can allowed to show information")
       return
   if admin_check(entered_role) or manager_check(entered_role):
      user_id=int(input("Enter User Id : "))
      line()
      for user in users:
          if user[0]== user_id:
             is_found=True
             print("Record found : ")
             print_user(user)
             break
      if  not is_found:
         print("Record not Found")
   



def login():
  count=0
  while count<3:
     username=input("Enter your Username : ")
     password=input("Enter your password : ")
     is_found=False
     for user in users:
       if username==user[1]:
         is_found=True
         if user[4].lower()=="locked":
             print("User are Locked Not Allowed to login")
             return
         if password==user[2]:
               user[4]="Active"
               print("Acess Granted")
               user[5]=0
               return
         else:
               user[5]+=1
               count+=1
               print("Invalid password")
               remaining=3-user[5] 
               if user[5]>=3:
                 user[4]="locked"
                 print("Your acount are locked ")
                 return
         break
     if not is_found:
        print("Invalid Username")
        count+=1
  print(" Login Failed ")
  
        
       
def lock_account():
   entered_role = input("Enter Role : ")
   if admin_check(entered_role):
      user_id=int(input("Enter user Id which you want to lock :"))
      for user in users:
         if user[0]==user_id:
            user[4]="Locked"
            print("user are Locked")
            return
      print("User not found")   
   else:
       print("Admin can only allowed ")

def unlock_account():
   entered_role = input("Enter Role : ")
   if admin_check(entered_role):
      user_id=int(input("Enter user Id which you want to unlock :"))
      for user in users:
         if user[0]==user_id:
            if user[4].lower()=="locked":
              user[4]="Inactive"
              print("user are unlocked")
              return
            else:
               print("user already unlocked")
               break
      print("User not found")   
   else:
       print("Admin can only allowed ")

def change_password():
  user_id=int(input("Enter Your user Id :"))
  for user in users:
    if user[0]==user_id:
      if user[4].lower()=="active":
         old_password=input("Enter your password : ")
         if old_password==user[2]:
            new_password=input("Enter your new password : ")
            confirm_password=input("Enter your new password (to confirm) : ")
            if new_password==confirm_password :
             user[2]=new_password
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

   

def  view_all_user():
  entered_role = input("Enter Role : ")
  if entered_role.lower()!="admin" or entered_role.lower()!="manager":
    for user in users:
       print_list(user)
  else:
     print("Not allow to show information")

def count_user():
   print(f"Count of users : {len(users)}")

def failed_login_tracking():
   entered_role = input("Enter Role : ")
   if admin_check(entered_role) or manager_check(entered_role):
     for user in users:
       if user[5]!=0:
         print(f"User Id : {user[0]}  failed attemp : {user[5]}")
       

def logout():
    user_id=int(input("Enter user Id which you want to logout :"))
    for user in users:
         if user[0]==user_id:
           if user[4].lower()=="active":
              user[4]="Inactive"
              print("--- Logged out successfully ---")
              return
           else:
             print("--- You are not logged in ---")
    print("User not found")
    line()
      



users=[
   #userId, username, password, role, status, login_failed
    [101, "rahul01", "Rahul@123", "Admin", "Active", 0],
    [102, "priya22", "Priya@456", "User", "Active", 0],
    [103, "amit_dev", "Amit#789", "User", "Inactive", 0],
    [104, "neha07", "Neha@321", "Manager", "Active", 0],
    [105, "karan99", "Karan#555", "User", "Locked", 0],
    [106, "simran18", "Simran@888", "User", "Active", 0],
    [107, "rohit_x", "Rohit@111", "Admin", "Inactive", 0],
    [108, "anjali_p", "Anjali#222", "Manager", "Active", 0],
    [109, "vivek09", "Vivek@999", "User", "Locked", 0],
    [110, "pooja_17", "Pooja#444", "User", "Active", 0]
]

deleted_users=[]



header()
admin_pin="9876"
manager_pin="1234"
is_delete=False
choice=1

while choice : 
    choice=menu()
    match choice:
          case 0:
              line()
              exit()
          case 1:
              add_user()
          case 2:
              is_delete=remove_user()
          case 3:
              search_user()
          case 4:
              login()
          case 5:
              lock_account()
          case 6:
              unlock_account()
          case 7:
              change_password()
          case 8:
              view_all_user()
          case 9:
              count_user()
          case 10:
              failed_login_tracking()
          case 11:
              logout()
          case _:
              print("!!! Invalid choice !!!")
          
