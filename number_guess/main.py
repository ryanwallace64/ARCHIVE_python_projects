import random
from replit import clear
from art import logo

def generate_number():
    return random.randint(1, 100)

def check_guess(guess):
    if guess == number:
        print(f"Congratulations! You win! The answer was {number}.")
        return True
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        return False
    else:
        print("Too low.")
        print("Guess again.")
        return False

end_game = False
while not end_game:
    print(logo)
    clear()
    number = generate_number()
    print("Welcome to Number Guess!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        lives = 5
    else:
        lives = 10

    win = False
    while lives > 0 and not win:
        print(f"You have {lives} attempts remaining to guess the number.")
        win = check_guess(int(input("Make a guess: ")))
        lives -= 1

    if lives == 0 and not win:
        print(f"Out of guesses. You lose! The number was {number}.")
        
    if input("Would you like to play again? Type 'y' or 'n': ") == "n":
        end_game = True
    
print("See ya! Thanks for playing!")
