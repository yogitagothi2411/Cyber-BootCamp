"""
Project: ATM simulator
BootCamp Day: 03
Date: 30-06-2026
Author: pyLearner
"""
from datetime import date, datetime
today= date.today()
Time = datetime.now().time()
print("----------------------------------------------------------------")
print("              :::: WELCOME TO ATM ::::")
print("----------------------------------------------------------------")
print(f"Date : {today}")
print(f"Time : {Time.strftime('%H:%M:%S')}")
print("----------------------------------------------------------------")

pin="0987"
entered_pin=input("Enter your pin : ")
print("----------------------------------------------------------------")
balance=2000
total_withdraw=0
total_deposit=0
choice=1
if pin!=entered_pin:
   print("Incorrect pin!! Please try again")
   exit()
   
   
while choice:
    w_amount=0
    d_amount=0
    #menu
    print("which funtionality you want to use : ")
    print("1.Withdraw Amount")
    print("2.Check Balance")
    print("3.Deposit Amount")
    print("4.Print Receipt")
    print("0.Exit")
    print("----------------------------------------------------------------")
    choice=int(input("Enter your choice : "))
    
    print("----------------------------------------------------------------")
    match choice :
     case 0:
        print("Thankyou for using our ATM.")
        print("----------------------------------------------------------------")
        exit()
     case 1:
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
     case 2:
        print(f"your current balance : {balance}")

     case 3:
          d_amount=int(input("Enter your amount you want to deposit : "))
          if d_amount>0:
               print(f"Deposit succesfull of amount {d_amount}")
               balance+=d_amount
               print(f"your current balance : {balance}")
               total_deposit=total_deposit + d_amount
          else:
             print("Invalid amount")
     case 4:
        print("---- ATM RECEIPT ----")
        print(f"Date            : {today}")
        print(f"Time            : {Time.strftime('%H:%M:%S')}")
        print(f"Balance         : {balance}")
        print(f"Withdraw Amount : {total_withdraw}")
        print(f"Deposit Amount  : {total_deposit}")
        print("Thank You")
        
     case _:
        print("Invalid Choice")
    print("----------------------------------------------------------------")

