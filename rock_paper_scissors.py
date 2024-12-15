import random


wins = 0
loses = 0
ties = 0

while True:
  valid_choices = ["rock", "paper", "scissors"]

  computer_choice = random.choice(valid_choices)

  user_input = input("Please enter your choice 'rock', 'paper', or 'scissors': " )
  user_choice = str(user_input.lower().strip())

  if (user_choice not in valid_choices):
    print("You must select either 'rock', 'paper', or 'scissors'.")
    user_input
  elif (user_choice == computer_choice):
    print(f"You picked {user_choice}. The computer picked {computer_choice}.")
    print("This match was a tie!")
    ties = ties + 1
    print(f"Wins: {wins}. Loses: {loses}. Ties: {ties}.")
  elif ((user_choice == "rock" and computer_choice == "scissors") or 
        (user_choice == "paper" and computer_choice == "rock") or 
        (user_choice == "scissors" and computer_choice == "paper")):
    print(f"You picked {user_choice}. The computer picked {computer_choice}.")
    print("You win!")
    wins = wins + 1
    print(f"Wins: {wins}. Loses: {loses}. Ties: {ties}.")
  else:
    print(f"You picked {user_choice}. The computer picked {computer_choice}.")
    print("You lose!")
    loses = loses + 1
    print(f"Wins: {wins}. Loses: {loses}. Ties: {ties}.")

  play_again = input("Play again? (y/n): ")
  if play_again.lower().strip() != "y":
    break
