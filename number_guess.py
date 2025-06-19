# This is a simple number guessing game where the computer takes a random integer and the player attempts to guess it.
import random


attempts = 0

computer_choice = random.randint(1, 100)

print(f"debugger: {computer_choice}")

player_choice = int(input("I am thinking of a number between 1 and 100. What number am I thinking of?: "))




while True:

  if player_choice == computer_choice and attempts == 0:
    print("You got it right on the first try. Either you are pyschic or a cheater! Congrats!")
    break
  elif player_choice == computer_choice:
    print(f"Congrats! It took you {attempts + 1} tries to guess it right!")
    break
  elif player_choice > computer_choice:
    player_choice = int(input("Your choice is too high. Guess again: "))
    attempts += 1
  elif player_choice < computer_choice:
    player_choice = int(input("Your choice is too low. Guess again: "))
    attempts += 1
