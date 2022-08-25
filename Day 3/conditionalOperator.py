# if/else statement

# if condition is True
#   then do 
# else 
#  do this

# Example

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#  print("You can ride the rollercoster! ")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Exercise : check number is even or odd.

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#     print("This is a even number")
# else:
#     print("This is a odd number")

#Nested if / else

#nested means loop another loop

# if condition:
#     if another condtion:
#         do this 
#     else: 
#         do this
# else:
#     do this

#Example

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#  print("You can ride the rollercoster! ")
#  age = int(input("What is your age?"))
#  if age <=  18:
#      print("Please pay $7.")
#  else:
#      print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
        
#Elif condition


print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))
if height >= 120:
 print("You can ride the rollercoster! ")
 age = int(input("What is your age?"))
 if age < 12:
     print("Please pay $5.")
 elif age <= 18:
     print("Please pay $7")    
 else:
     print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
 