#And == both condition are true
#Or == one of the condition are true 
#Not == reverse the condition answer


print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?\n "))
bill = 0
if height >= 120:
 print("You can ride the rollercoster! ")
 age = int(input("What is your age?\n"))
 if age < 12:
     bill = 5
     print("Child tickets are $5.")
 elif age <= 18:
     bill = 7
     print("Youth tickets are $7") 
 elif age >= 45 and age <= 55:
     print("Everything gona to be ok, Have a free ride on us!")  
 else:
     bill= 12
     print("Adult tickets are $12.")
    
 wants_photo = input("Do you want a photo taken? Y or N.\n")
 if wants_photo == "Y":
     bill +=3
     
 print(f"Your bill is ${bill}.")
 
else:
    print("Sorry, you have to grow taller before you can ride.")