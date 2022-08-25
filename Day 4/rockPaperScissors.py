# Rock
from random import random


rock = print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_input = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors"))

computer_input = random.randint(0,2)
print(f"Computer chose {computer_input}")


