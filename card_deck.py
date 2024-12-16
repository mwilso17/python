import random

deck = {"Ace of Spades": ["black", "spade"], "2 of Spades": ["black", "spade"], "3 of Spades": ["black", "spade"], "4 of Spades": ["black", "spade"], "5 of Spades": ["black", "spade"], "6 of Spades": ["black", "spade"], "7 of Spades": ["black", "spade"], "8 of Spades": ["black", "spade"], "9 or Spades": ["black", "spade"], "10 of Spades": ["black", "spade"], "Jack of Spades": ["black", "spade"], "Queen of Spades": ["black", "spade"], "Kings of Spades": ["black", "spade"],
         "Ace of Hearts": ["red", "heart"], "2 of Hearts": ["red", "heart"], "3 of Hearts": ["red", "heart"], "4 of Hearts": ["red", "heart"], "5 of Hearts": ["red", "heart"], "6 of Hearts": ["red", "heart"], "7 of Hearts": ["red", "heart"], "8 of Hearts": ["red", "heart"], "9 or Hearts": ["red", "heart"], "10 of Hearts": ["red", "heart"], "Jack of Hearts": ["red", "heart"], "Queen of Hearts": ["red", "heart"], "Kings of Hearts": ["red", "heart"],
         "Ace of Clubs": ["black", "club"], "2 of Clubs": ["black", "club"], "3 of Clubs": ["black", "club"], "4 of Clubs": ["black", "club"], "5 of Clubs": ["black", "club"], "6 of Clubs": ["black", "club"], "7 of Clubs": ["black", "club"], "8 of Clubs": ["black", "club"], "9 or Clubs": ["black", "club"], "10 of Clubs": ["black", "club"], "Jack of Clubs": ["black", "club"], "Queen of Clubs": ["black", "club"], "Kings of Clubs": ["black", "club"],
         "Ace of Diamonds": ["red", "diamond"], "2 of Diamonds": ["red", "diamond"], "3 of Diamonds": ["red", "diamond"], "4 of Diamonds": ["red", "diamond"], "5 of Diamonds": ["red", "diamond"], "6 of Diamonds": ["red", "diamond"], "7 of Diamonds": ["red", "diamond"], "8 of Diamonds": ["red", "diamond"], "9 or Diamonds": ["red", "diamond"], "10 of Diamonds": ["red", "diamond"], "Jack of Diamonds": ["red", "diamond"], "Queen of Diamonds": ["red", "diamond"], "Kings of Diamonds": ["red", "diamond"]}

colors = ["red", "black"]
suits = ["heart", "spade", "diamond", "club"]

color_guess = random.choice(colors)

print(len(deck))

print("There are 52 cards in a standard deck of cards. Please select 1 and I will try to guess it.")
print("When I ask a question, please respond with yes or no (y/n).")

first_question = input(f"Is your card {color_guess}")

if first_question == "y":
  for card, color in list(deck.items()):
    if color[0] != str(color_guess):
      del deck[card]
else:
  for card, color in list(deck.items()):
      if color[0] == str(color_guess):
        del deck[card]

print(deck)

##for card, suit in list(deck.items()):
##  if suit[1] == 'club':
##    del deck[card]
##
##print(len(deck))