#the logo of number guessing game
from random import randint
from asciiLogo import title_logo
print(title_logo)

EASY_LEVEL_TURNS = 10
# MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

# Make fucntion to set difficulty level 
# difficulty level input: based on the difficulty level change the number of attempts from the game like hard have 5 attempts and easy have 10 attempts
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy','medium' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    # elif level == "medium":
    #     return MEDIUM_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TURNS
# Function to check user's guess against actual answer.

def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def guessTheNumber():    
    # write a welcome massage 
    # Choosing a rangom number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    answer = randint(1,101)
    print(f"pass the correct answer is {answer}")
    
    turns = set_difficulty()            
    # print(turns)
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Let the user guess a number.
        guess = int(input("Make a guess: "))
        
        # Track the number of turns and reduce by 1 if they get is wrong.
        check_answer(guess , answer, turns)
        if turns == 0:
            print("You've run out of guessess, you lose.")
            return 
        elif guess != answer:
            print("Guess again!")

guessTheNumber()