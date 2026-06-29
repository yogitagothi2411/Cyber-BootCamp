"""
Project: Age calcultor
BootCamp Day: 01
Date: 28-06-2026
Author: pyLearner
"""



from datetime import date, datetime
from calendar import monthrange

print("----------------------------------------------------------------")
print("              :::: Age Calculator ::::")
print("----------------------------------------------------------------")

#today date
today =date.today()

name=input("Enter your name:")

#take input date in string and then convert into date object
date_str=input("Enter your date of birth(dd-mm-yyyy):")
try:
     birth=datetime.strptime(date_str,"%d-%m-%Y").date()
except ValueError:
     print("----------------------------------------------------------------")
     print("!! Invalid date !!")
     print("----------------------------------------------------------------")
     exit()


if birth > today:
   print("----------------------------------------------------------------")
   print("Invalid DOB ! birth date cannot be in the future.")
   print("----------------------------------------------------------------")
   exit()

  

year=today.year-birth.year
month=today.month-birth.month
days=today.day-birth.day

if days<0: 
    month-=1

    if today.month==1:
      prev_month=12
      prev_year=today.year-1
    else :
      prev_month=today.month-1
      prev_year=today.year

    days=days + monthrange(prev_year,prev_month)[1]

if month<0:
     year=year-1
     month=month+12


print("----------------------------------------------------------------")
print("Hello!",name)
print(f" Age : {year} years {month} months {days} days ")
print("----------------------------------------------------------------")