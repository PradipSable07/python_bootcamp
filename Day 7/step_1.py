# step 1
word_list = ["pradip","kapil","anand","ravindra","amit"]
# TODO - 1: Randomly choose a word form the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

# TODO - 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess the letter:").lower()

# TODO - 3: Check if the letter the user guessed (guess) is one of the leters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        
