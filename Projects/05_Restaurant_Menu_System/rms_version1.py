"""
Project: Restaurant Menu System
BootCamp Day: 05
Date: 02-07-26
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
    print("              :::: WELCOME TO RESTAURANT ::::")
    line()
    date_time()
   


def menu():
    line()
    print("Functionalities : ")
    print("1. Show Menu")
    print("2. Order Food")
    print("3. View Order")
    print("4. Calculate Bill")
    print("5. Print Receipt")
    print("0. Exit")
    line()
    choice=int(input("Enter your choice : "))
    line()
    return choice


def show_menu():
     print("============= Menu ==============")
     print(" 1. Plan Thali (80 Rs)")
     print(" 2. Specail Thali (100 /-)")
     print(" 3. Manchurain Gravy (100 /-)")
     print(" 4. Manchurain Dry (120 /-)")
     print(" 5. Manchurain semi-dry (110 /-)")
     print(" 6. Plan Rice (60 /-)")
     print(" 7. Jera Rice (70 /-)")
     print(" 8. Fried Rice (80 /-)")
     print(" 9. Dal Rice (90 /-)")
     print("10. Nodles (100 /-)")
     print("11. Crispy Corn (80 /-)")
     print(" 0. Exit")
     line()
     

def take_order(order):
    while True:
      dish=int(input("Enter your order dish number : "))
      quantity=int(input("Enter quantity : "))
      order.append([dish-1,quantity])
      check=input("Order more (y/n) : ")
      if check.lower()=="n":
          break
    return order



def show_order(order):
    print("Dish Name      : Price : Quantity")
    for item in order:
      dish=item[0]
      quantity=item[1]
      print(f"{food_menu[dish][0]} : {food_menu[dish][1]} : {quantity}")
    
       

def calculate_bill(order,total):
    for item in order:
        index=item[0]
        quantity=item[1]
        total=total+((food_menu[index][1])*quantity)
    print("Bill calculated\nNow you can print recipt")
    return total
        


def receipt(total,order):
        print("-------- BILL RECEIPT --------")
        date_time()
        print("------------------------------")
        for item in order:
         dish=item[0]
         quantity=item[1]
         print(f"{food_menu[dish][0]} :  {food_menu[dish][1]} * {quantity} = {food_menu[dish][1]*quantity}")
        print("-----------------------------")
        print(f"Total Amount   :     {total}")
       
        print("Thank You")






header()
bill=0
order=[]
total=0
choice=1

food_menu=[
    # dish_name,price,quantity
    ["Plan Thali",80],
    ["Specail Thali",100],
    ["Manchurain Gravy",100],
    ["Manchurain Dry",120],
    ["Manchurain semi-dry",110],
    ["Plan Rice",60],
    ["Jera Rice",70],
    ["Fried Rice",80],
    ["Dal Rice",90],
    ["Nodles",100],
    ["Crispy Corn",80]

]

while choice:
    choice=menu()
    match choice :
     case 0:
        print("Thankyou for visting.")
        line()
        break
     case 1:
         show_menu()
     case 2:
        order=take_order(order)
     case 3:
        show_order(order)
     case 4:
        total=calculate_bill(order,total)
     case 5:
            receipt(total,order)
     case _:
        print("Invalid Choice")
    
