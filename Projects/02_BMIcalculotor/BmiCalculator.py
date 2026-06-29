"""
Project: BMI calcultor
BootCamp Day: 02
Date: 29-06-2026
Author: pyLearner
"""
from datetime import date, datetime
date = date.today()
Time = datetime.now().time()
print("----------------------------------------------------------------")
print("              :::: BMI Calculator ::::")
print("----------------------------------------------------------------")
print(f"Date : {date}")
print(f"Time : {Time.strftime('%H:%M:%S')}")
print("----------------------------------------------------------------")
#menu
print ("which units you want to Enter:")
print("1. pounds & Inches")
print("2. kilograms & meters")

choice=int(input("Enter your choice : "))
name= input("Enter your name :")
match choice:
    case 1: 
         Wpounds=float(input("Enter your weight in pounds : "))
         Hinches=float(input("Enter your height in Inches : "))
         Weight=Wpounds*0.453592
         Height=Hinches*0.0254
        
    case 2:
        Weight=float(input("Enter your weight in kg : "))
        Height=float(input("Enter your height in meter : "))
    case _ :
        print("Invalid choice")
        exit()


if Weight<=0 or Height<=0:
    print("Weight and height must be greater than 0.") 
    exit()
Bmi=Weight/(Height*Height)
idealWeight1=18.5*(Height*Height)
idealWeight2=24.9*(Height*Height)

print("----------------------------------------------------------------")
if Bmi<18.5:
    category = "Underweight"
    advice= "Eat a nutritious, balance diet."
elif Bmi<=24.9:
    category = "Normal weight"
    advice="Maintain your healthy lifestyle."
elif Bmi<=29.9:
     category = "overweight"
     advice="Exercise regularly and eat a balance diet."
else:
    category = "Obese"
    advice="Consult a helthcare professional."
print(f"hello, {name}!")
print(f"Weight    : {Weight:.2f}")
print(f"Height    : {Height:.2f}")
print(f"BMI       : {Bmi:.2f}")
print(f"Category  : {category}")
print(f"Advice    : {advice}")
print(f"Your ideal weight should be between {idealWeight1:.2f}kg and {idealWeight2:.2f}kg")
print("----------------------------------------------------------------")