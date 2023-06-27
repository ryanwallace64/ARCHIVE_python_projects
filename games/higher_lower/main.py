import random
import game_data
import art
from replit import clear

def new_person():
    '''Return a new person object from game_data.py'''
    return random.choice(game_data.data) 

def game():
    '''Run game until player loses'''
    print(art.logo)
    score = 0
    compare_b = new_person()

    end_game = False
    while not end_game:
        compare_a = compare_b
        compare_b = new_person()
        while compare_b == compare_a:
            compare_b = new_person()
    
        if compare_a["follower_count"] > compare_b["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"
       
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, {compare_a['country']}.")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, {compare_b['description']}, {compare_b['country']}.")
        guess = input("Who has more followers? 'A' or 'B': ")

        if guess == correct_answer:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Currect score: {score}.")
        else:
            clear()
            print(art.logo)
            print(f"You're wrong. You lose! Your score was: {score}.")
            end_game = True
        
keep_playing = True
while keep_playing == True:
    game()
    if input("Would you like to play again? 'y' or 'n': ") == "n":
        keep_playing = False
    else:
        clear()

print("Thanks for playing!")