"""
Project: ATM simulator
BootCamp Day: 03
Date: 30-06-2026,02-07-26
Author: pyLearner
"""
from datetime import date, datetime


def line():
   print("----------------------------------------------------------------")

def date_time():
     today= date.today()
     current_time = datetime.now().time()
     print(f"Date : {today}")
     print(f"Time : {current_time.strftime('%H:%M:%S')}")
     



def header():
    line()
    print("              :::: WELCOME TO ATM ::::")
    line()
    date_time()
    line()


def menu():
    line()
    print("which funtionality you want to use : ")
    print("1.Withdraw Amount")
    print("2.Check Balance")
    print("3.Deposit Amount")
    print("4.Print Receipt")
    print("0.Exit")
    line()
    choice=int(input("Enter your choice : "))
    line()
    return choice


def withdraw(balance, total_withdraw):
     w_amount=int(input("Enter your amount you want to withdraw : "))
     confirm=input(f"You want to withdraw {w_amount}?  Y/N : ")
     if confirm.upper()=="Y":
           if w_amount <= balance and w_amount>0:
            print(f"withdraw succesful of amount : {w_amount}")
            balance-=w_amount
            print(f"Remaining Balance : {balance}")
            total_withdraw=total_withdraw + w_amount
           else:
            print("Insufficient Balance")
     else:
            print("!!Exit, you dont want to withdraw")
     return w_amount, balance, total_withdraw

def check_balance(balance):
    print(f"your current balance : {balance}")
    return balance
    
   

def deposit(balance,total_deposit):
      d_amount=int(input("Enter your amount you want to deposit : "))
      if d_amount>0:
               print(f"Deposit succesfull of amount {d_amount}")
               balance+=d_amount
               print(f"your current balance : {balance}")
               total_deposit=total_deposit + d_amount
      else:
             print("Invalid amount")
      return d_amount, balance,total_deposit

def receipt(balance, total_deposit, total_withdraw):
        print("------ ATM RECEIPT ------")
        date_time()
        print("-------------------------")
        print(f"Balance         : {balance}")
        print(f"Withdraw Amount : {total_withdraw}")
        print(f"Deposit Amount  : {total_deposit}")
        print("Thank You")
       

def pin_check():
     pin="0987"
     entered_pin=input("Enter your pin : ")
     if pin!=entered_pin:
        print("Incorrect pin!! Please try again")
        exit()
     


header()
pin_check()
balance=2000
total_withdraw=0
total_deposit=0
choice=1
while choice:
    w_amount=0
    d_amount=0
    choice=menu()
    match choice :
     case 0:
        print("Thankyou for using our ATM.")
        line()
        break
     case 1:
            w_amount, balance, total_withdraw=withdraw(balance, total_withdraw)
     case 2:
            balance=check_balance(balance)
     case 3:
            d_amount, balance,total_deposit=deposit(balance,total_deposit)
     case 4:
           receipt(balance,total_deposit,total_withdraw)
     case _:
        print("Invalid Choice")
    
