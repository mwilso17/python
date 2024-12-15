import random

valid_choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(valid_choices)

user_input = input("Please enter your choice 'rock', 'paper', or 'scissors': " )
user_input_lower = str(user_input.lower().strip())

if (user_input_lower not in valid_choices):
  print("You must select either 'rock', 'paper', or 'scissors'.")
  user_input
else:
  print(f'Your choice is {user_input_lower}.')
  print(f'the computer picked {computer_choice}')