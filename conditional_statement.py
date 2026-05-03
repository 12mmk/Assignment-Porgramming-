# 1. Write a program to check whether the given number is in between 1 and 100 or not.
from ast import Not


number=int(input("Enter number"))

if number>=1 and number<=100:
  print("The number exist in the range")
else:
  print("The number does not exist in the range")

# 2. Write a program to check whether the given number is even or odd.
number=int(input("Enter number"))

if number%2==0:
  print("Number is even")
else:
  print("Number is odd")

#  3. Write a program that asks the user for a number 

#           in the range of 1 to 12. 

#        The program should display the corresponding month, where 

#        1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 

#        8=august,9=september,10=october,11=november,12=december. The program should display an error 

#        message if the user enters a number that is outside the range of 1 to 12.

number=int(input("Enter number"))

month={
    1: "january",
  2: "february",
  3: "march",
  4: "april",
  5: "may",
  6: "june",
  7: "july",
  8: "august",
  9: "september",
  10: "october",
  11: "november",
  12: "december"
}
if number in month:
  print(month[number])

else:
  print("number out of range")


#   4. A school has following rules for grading system:

#         a. Below 25 - F

#         b. 25 to 45 - E

#         c. 45 to 50 - D

#         d. 50 to 60 - C

#         e. 60 to 80 - B

#         f. Above 80 - A

#         Ask user to enter marks and print the corresponding grade

marks=int(input("Enter marks"))
if marks<25:
  print("Grade F")
elif marks>=25 and marks<45:
  print("Grade E")
elif marks>=45 and marks<50:
  print("Grade D")
elif marks>=50 and marks<60:
    print("Grade C")
elif marks>=60 and marks<80:
    print("Grade B")
elif marks>=80:
    print("Grade A")


#  5. Write a program to check whether a number is divisible by 7 or not.
number=int(input("Enter number"))

if number%7==0:
  print("Number is divisible by 7")
else:
  print("Number is not divisible by 7")


# 6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.

#             Like:

#             Enter First Number: 7

#             Enter Second Number : 9

#             Enter operator : +

#             Your Answer is : 16

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
operator=input("Enter operator")

if operator=="+":
  print(num1+num2)
elif operator=="*":
  print(num1*num2)
elif operator=="-":
  print(num1-num2)
elif operator=="/":
  print(num1/num2)
elif operator=="%":
  print(num1%num2)

# 7. Write a Python program to check car loan eligibility:

#             Salary >= 50,000 and Credit Score >= 700: "Eligible"

#             Otherwise: "Not Eligible"

salary=int(input("Enter salary"))
credit_score=int(input("Enter credit score"))

if credit_score>700 and salary>=50000:
  print("Loan eligible")
else:
  print("Loan not eligible")

# 8. Write a Python program that takes an integer input n n. 

#         From given number, 

#         check if it is divisible by both 3 and 5, and print "FizzBuzz" 

#         if true. 

#         If the number is divisible only by 5, print "Buzz." If it is 

#         divisible only by 3, print "Fizz." 

#         Finally, if the number is not divisible by either 3 or 5, 

#         print the number itself.

number=int(input("Enter number"))
if number%3==0 and number%5==0:
  print("FizzBuzz")
elif number%5==0:
  print("Buzz")
elif number%3==0:
  print("Fizz")
else:
  print(number)


# 9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.

character=input("Enter character")
vowels=["a","e","i","o","u"]
if character in vowels:
  print("Character is vowel") 
else:
  print("Character is consonant")

# 10. Write a Python program to input marks and determine the grade based on the following conditions:

# 90-100: A

# 80-89: B

# 70-79: C

# Below 70: Fail

marks=int(input("Enter marks"))
grade={
    "A": range(90,101),
    "B": range(80,90),
    "C": range(70,80)
}
if marks in grade["A"]:
  print("Grade A")
elif marks in grade["B"]:
  print("Grade B")
elif marks in grade["C"]:
  print("Grade C")
else:
    print("Fail")


# 11. Write a Python program to categorize a person’s age:

# Age < 13: Child

# 13 <= Age <= 19: Teenager

# Age > 19: Adult

age=int(input("Enter age"))
if age<13:
  print("Child")
elif age>=13 and age<=19:
  print("Teenager")
elif age>19:
  print("Adult")


# 12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

character=input("Enter character")
if character.isupper():
  print("Character is uppercase")
elif character.islower():
    print("Character is lowercase")
elif character.isdigit():
    print("Character is digit")

# 13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").
color=input("Enter color")
if color=="Red":
    print("Stop")
elif color=="Yellow":
    print("Get Ready")
elif color=="Green":
    print("Go")

# 14. Write a Python program to check eligibility for a job based on age and experience:

# Age > 18 and Experience >= 2 years: Eligible

# Otherwise: Not Eligible
age=int(input("Enter age"))
experience=int(input("Enter experience in years"))
if age>18 and experience>=2:
    print("Eligible for job")
else:
    print("Not eligible for job")

# 15. Write a Python program to give advice based on the temperature:

# Temperature > 30°C: "It's hot, stay hydrated!"

# Temperature between 15-30°C: "Enjoy the weather!"

# Temperature < 15°C: "It's cold, wear warm clothes!"

temperature=int(input("Enter temperature"))
if temperature>30:
    print("It's hot, stay hydrated!")
elif temperature>=15 and temperature<=30:
    print("Enjoy the weather!")
elif temperature<15:
    print("It's cold, wear warm clothes!")

# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:

# Pizza: $10

# Burger: $7

# Pasta: $8

menu_option=input("Enter menu option")
if menu_option=="Pizza":
    print("Price is $10")
elif menu_option=="Burger":
    print("Price is $7")
elif menu_option=="Pasta":
    print("Price is $8")

# 17. Write a Python program to select players based on height:

# Height >= 6 feet: Selected

# Height < 6 feet: Not Selected

height=float(input("Enter height in feet"))
if height>=6:
    print("Selected")
else:
    print("Not selected")

# 18. Write a Python program to check if a person is eligible to watch a movie based on their age:

# Age >= 18: Allowed

# Age < 18: Not Allowed

age=int(input("Enter age"))
if age>=18:
    print("Allowed to watch movie")
else:
    print("Not allowed to watch movie")

# 19. Write a Python program to check login credentials:

# Username: "admin", Password: "password123"

# If correct, print "Access Granted"; otherwise, print "Access Denied."

username=input("Enter username")
password=input("Enter password")
if username=="admin" and password=="password123":
    print("Access Granted")
else:
    print("Access Denied")

# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:

# 12, 1, 2: "Winter"

# 3, 4, 5: "Spring"

# 6, 7, 8: "Summer"

# 9, 10, 11: "Autumn"

month=int(input("Enter month number"))
if month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
    
