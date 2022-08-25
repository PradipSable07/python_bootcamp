print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

combine_string_of_names = lower_case_name1+lower_case_name2

t = combine_string_of_names.count("t")
r = combine_string_of_names.count("r")
u = combine_string_of_names.count("u")
e = combine_string_of_names.count("e")

true = t + r + u + e

l = combine_string_of_names.count("l")
o = combine_string_of_names.count("o")
v = combine_string_of_names.count("v")
e = combine_string_of_names.count("e")

love = l + o + v + e

love_score = int(str(true)+str(love))

print(love_score)
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")