##################################################[DEBUGGING]################################################################

# # Describe Problem
"""
def my_function():
    for i in range(1,20):
        if i==20:
            print("You got it")
my_function()
"""
# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("You got it")
# my_function()

# Reproduce the Bug
""" 
from random import randint
dice_imags = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
dice_num = randint(1,6)
print(dice_imags[dice_num])
"""
# from random import randint
# dice_imags = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
# dice_num = randint(0,5)
# print(dice_imags[dice_num])

# Play Computer
"""
year = int(input("What's your year of bith?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Geb z.")
"""
# year = int(input("What's your year of bith?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Geb z.")

# Fixing Errors 
"""" 
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
"""
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
    
# Print is Your Friend
"""
pages = 0 
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
"""
# pages = 0 
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

