# random password generator
from lib2to3.pygram import Symbols
import numbers
import random
from symtable import Symbol

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','2','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J''K''L','M','N','0','P','Q','R','S','T','U','V''W''Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to Python Random Password Generator.")
number_latter = (int(input("How many latter you would you like in your password?\n")))

number_symbols = (int(input("How many symbols you would you like in your password?\n")))
number_number = (int(input("How many number you would you like in your password?\n")))

#easy_type
# password = ""

# for char in range(1,number_latter+1):
#     password += random.choice(alphabets)

# for sym in range(1,number_symbols+1):
#     password += random.choice(Symbols)

# for num in range(1,number_number+1):
#     password += random.choice(numbers)

# print(password)

#Hard_level_Or_Type
password_list = []


for char in range(1,number_latter+1):
    password_list += random.choice(alphabets)

for sym in range(1,number_symbols+1):
    password_list += random.choice(Symbols)

for num in range(1,number_number+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    
print(f"Your password is {password}")


