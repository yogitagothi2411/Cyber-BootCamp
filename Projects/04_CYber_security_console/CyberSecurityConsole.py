"""
Project: Cyber Security Console(v1)
update-User Authentication Manager(v2)
user profile Manager(v3)
BootCamp Day: 04 / 07 / 08
Date: 01-07-2026 /05-07-2026 /07-07-2026
Author: pyLearner
"""


def line():
  print("========================================================================")


def header():
    line()
    print("         !!! CYBER SECURITY CONSOLE !!!")
    line()
      



def front_menu():
    print()
    print("===============!!! MENU !!!===============")
    print("1. Login")
    print("2. Signup")
    print("0. Exit")
    line()
    choice=int(input("Enter Your Choice : "))
    return choice



def menu():
    print()
    print("===============!!! MENU !!!===============")
    print(" 1. Remove User")
    print(" 2. Search User")
    print(" 3. Lock Account")
    print(" 4. Unlock Account")
    print(" 5. Change Password")
    print(" 6. View All User ")
    print(" 7. Count Users ")
    print(" 8. Failed Login Tracking")
    print(" 9. Logout")
    print(" 0. Exit")
    line()
    choice=int(input("Enter Your Choice : "))
    return choice


def print_user(user,username):
   print("----------------------------------------")
   print(f"username      : {username}")
   print(f"password      : {user['password']}")
   print(f"Role          : {user['role']}")
   print(f"Status        : {user['status']}")
   print(f"Failed Attempts : {user['failed_attempts']}")
   print("----------------------------------------")


def print_list(username,details):
    print(f"{username} || {details['password']} ||  {details['role']} ||  {details['status']} ||  {details['failed_attempts']} ")
         


def add_user():
     while True:
      username=input("Enter Username :").strip()
      if username in users:
          print("User name already exist\n change username")
      else :
         break
     password=input("Enter Password : ").strip()
     role ="User"
     users[username]= {
       
          "password": password,
          "role": role,
          "status": "Inactive",
          "failed_attempts": 0
    }
     print("User added succesfully")
    
     
 

def remove_user():
   username=input("Enter Username :").strip()
   if username in users:
     confirm = input("Do you want to delete this user? (y/n) : ").strip()
     if confirm.lower()=="y":
        deleted_users[username]=users.pop(username)
        print("User deleted successfully.")
     else:
        print("Deletion cancelled.")    
   else :
     print("Record not found")


def search_user():
    username=input("Enter Username :").strip()
    if username in users:
       user=users[username]
       print_user(user,username) 
    else:
       print("User not found")


def login():
  while True:
     username=input("Enter your username : ").strip()
     password=input("Enter your password : ").strip()
     if username not in users:
        print("Username not found")
        continue
     if users[username]["status"]=="Locked":
           print("Your account is looked")
           return False
     if users[username]["password"]==password:
           users[username]["failed_attempts"]=0
           users[username]["status"]="Active"
           print("Access Granted")
           return True
     
     users[username]["failed_attempts"]+=1
     print("Wrong password")
     if users[username]["failed_attempts"]>=3:
          users[username]["status"]="Locked"
          print("Account Locked")
          return False
 
        
       
def lock_account():
      username=input("Enter username which you want to lock :")
      if username in users:
         if users[username]["status"]!="Locked":
            users[username]["status"]="Locked"
            print("user are Locked")
            return
         else:
          print("User are already Locked")   
      else:
       print("User not Found")


def unlock_account():
    username=input("Enter username which you want to lock :")
    if username in users:
         if users[username]["status"]=="Locked":
            users[username]["status"]="Inactive"
            print("user are unlocked")
            return
         else:
          print("User are already unlocked")   
    else:
       print("User not Found")
 


def change_password():
  username=input("Enter Your username :")
  if username in users:
      if users[username]["status"].lower()=="active":
         old_password=input("Enter your password : ")
         if old_password==users[username]["password"]:
            new_password=input("Enter your new password : ")
            confirm_password=input("Enter your new password (to confirm) : ")
            if new_password==confirm_password :
             users[username]["password"]=new_password
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
    for username, details in users.items():
       print_list(username,details)
  



def count_user():
   print(f"Count of users : {len(users)}")

def failed_login_tracking():
     for username, details in users.items():
       if details["failed_attempts"] > 0:
         print(f"Username : {username}")
         print(f"failed attempts : {details['failed_attempts']}")
       

def logout():
    username=input("Enter username which you want to logout :")
    if username in users:
        if users[username]['status'].lower()=="active":
            users[username]['status']="Inactive"
            print("--- Logged out successfully ---")
            return
        else:
             print("--- You are not logged in ---")
    else: 
       print("User not found")
    line()
      



users = {
    "rahul01": {
        "password": "Rahul@123",
        "role": "Admin",
        "status": "Active",
        "failed_attempts": 0
    },

    "priya22": {
        "password": "Priya@456",
        "role": "User",
        "status": "Active",
        "failed_attempts": 0
    },

    "amit_dev": {
        "password": "Amit#789",
        "role": "User",
        "status": "Inactive",
        "failed_attempts": 0
    },

    "neha07": {
        "password": "Neha@321",
        "role": "Manager",
        "status": "Active",
        "failed_attempts": 0
    },

    "karan99": {
        "password": "Karan#555",
        "role": "User",
        "status": "Locked",
        "failed_attempts": 0
    },

    "simran18": {
        "password": "Simran@888",
        "role": "User",
        "status": "Active",
        "failed_attempts": 0
    },

    "rohit_x": {
        "password": "Rohit@111",
        "role": "Admin",
        "status": "Inactive",
        "failed_attempts": 0
    },

    "anjali_p": {
        "password": "Anjali#222",
        "role": "Manager",
        "status": "Active",
        "failed_attempts": 0
    },

    "vivek09": {
        "password": "Vivek@999",
        "role": "User",
        "status": "Locked",
        "failed_attempts": 0
    },

    "pooja_17": {
        "password": "Pooja#444",
        "role": "User",
        "status": "Active",
        "failed_attempts": 0
    }
}
deleted_users={}



header()
is_delete=False
choice=1
while choice : 
    choice=front_menu()
    match choice:
          case 0:
              line()
              exit()
          case 1:
              login()
          case 2:
              add_user()

if login():
    while True : 
      choice=menu()
      match choice:
          case 0:
              line()
              exit()
          case 1:
              remove_user()
          case 2:
              search_user()
          case 3:
              lock_account()
          case 4:
              unlock_account()
          case 5:
              change_password()
          case 6:
              view_all_user()
          case 7:
              count_user()
          case 8:
              failed_login_tracking()
          case 9:
              logout()
          case _:
              print("!!! Invalid choice !!!")
          

