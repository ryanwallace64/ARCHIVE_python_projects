import random
import hangman_art
from hangman_words import word_list

# Pick random word from word option list
chosen_word = random.choice(word_list)

# Start user with six lives
lives = 6
game_over = False
guessed_letters = []

print(hangman_art.logo)
print(hangman_art.stages[lives])

# Create blank spaces for each letter in chosen word
display = []
for _ in range(len(chosen_word)):
    display += "_"

# Function to get user input for guessed letter
def guess_letter():
    global lives
    global game_over
    global guessed_letters
    correct = 0
    user_guess = input("Choose a letter to guess: ").lower()
   
    # Check user input against chosen word
    while user_guess not in guessed_letters:
        for position in range(len(chosen_word)):
            if chosen_word[position] == user_guess:
                display[position] = user_guess
                correct += 1
                guessed_letters += user_guess
            
        # Reduce lives if wrong and print new hangman
        if correct == 0:
            lives -= 1
            if lives == 0:
                game_over = True
            print(hangman_art.stages[lives])
            print(f"You guessed {user_guess}. It is not in the word.")
            guessed_letters += user_guess
    
# Run Loop until game complete
while chosen_word != "".join(display) and not game_over:
    guess_letter()
    print(display)

# Announce Win or Loss
if game_over == True:
    print("You Lose! :(")
    print(f"The word was: {chosen_word}")
else:
    print("You win!")


### Code from instructor's version ###
    
# import random

# from hangman_words import word_list

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# from hangman_art import logo
# print(logo)

# #Testing code
# # print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     from hangman_art import stages
#     print(stages[lives])