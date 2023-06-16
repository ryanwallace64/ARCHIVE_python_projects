import random

#ASCII ART
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Commented out first iteration after creating a more stream-lined and efficient program further below.

# player_choice = input('Choose "rock", "paper", or "scissors": ')

# randnum = random.randint(1, 3)
# if randnum == 1:
#   computer_choice = "rock"
# elif randnum == 2:
#   computer_choice = "paper"
# else:
#   computer_choice = "scissors"

# if player_choice == "rock" and computer_choice == "rock":
#   print("Player:")
#   print(rock)
#   print("Computer:")
#   print(rock)
#   print("Tie!")
# elif player_choice == "rock" and computer_choice == "paper":
#   print("Player:")
#   print(rock)
#   print("Computer:")
#   print(paper)
#   print("You Lose!")
# elif player_choice == "rock" and computer_choice == "scissors":
#   print("Player:")
#   print(rock)
#   print("Computer:")
#   print(scissors)
#   print("You Win!")

# if player_choice == "paper" and computer_choice == "rock":
#   print("Player:")
#   print(paper)
#   print("Computer:")
#   print(rock)
#   print("You Win!")
# elif player_choice == "paper" and computer_choice == "paper":
#   print("Player:")
#   print(paper)
#   print("Computer:")
#   print(paper)
#   print("Tie!")
# elif player_choice == "paper" and computer_choice == "scissors":
#   print("Player:")
#   print(paper)
#   print("Computer:")
#   print(scissors)
#   print("You Lose!")

# if player_choice == "scissors" and computer_choice == "rock":
#   print("Player:")
#   print(scissors)
#   print("Computer:")
#   print(rock)
#   print("You Lose!")
# elif player_choice == "scissors" and computer_choice == "paper":
#   print("Player:")
#   print(scissors)
#   print("Computer:")
#   print(paper)
#   print("You Win!")
# elif player_choice == "scissors" and computer_choice == "scissors":    
#   print("Player:")
#   print(scissors)
#   print("Computer:")
#   print(scissors)
#   print("Tie!")

# Create list with ASCII art
game_images = [rock, paper, scissors]

# Player chooses an option
player_choice = int(input('Enter "0" for rock, "1" for paper, or "2" for scissors: '))

# Catch if invalid entry
if player_choice >= 3 or player_choice < 0:
  print("Invalid number entered. You Lose!")
else:
  print("Player Choice:")
  print(game_images[player_choice])

  # Computer choice randomly generated
  computer_choice = random.randint(0, 2)
  print("Computer choice:")
  print(game_images[computer_choice])
  
  # Win/Lose/Tie logic
  if player_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and player_choice == 2:
    print("You Lose!")
  elif computer_choice > player_choice:
    print("You Lose!")
  elif player_choice > computer_choice:
    print("You Win!")
  elif computer_choice == player_choice:
    print("Tie!")