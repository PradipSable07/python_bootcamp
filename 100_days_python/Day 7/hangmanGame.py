# HangmanGame
import random
import hangman_words
import hangman_art
import replit
#importing the hangman word list from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
#Printing the Hangman Logo from hangman_art
print(hangman_art.hangman_logo)

#Testing code
print(f'pssst, The solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position:{position}\n Current letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position]= letter
            
        #Check if user if wrong
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -=1
            if lives ==0:
                end_of_game = True 
                print("You lose.")
            
     #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
            
        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True 
            print("You win.")

        #importing the hangman_art
        print(hangman_art.hangman_stages[lives])