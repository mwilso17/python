import random

deck = {"Ace of Spades": ["black", "spade", "numeric", 1], "2 of Spades": ["black", "spade", "numeric", 2], "3 of Spades": ["black", "spade", "numeric", 3], "4 of Spades": ["black", "spade", "numeric", 4], "5 of Spades": ["black", "spade", "numeric", 5], "6 of Spades": ["black", "spade", "numeric", 6], "7 of Spades": ["black", "spade", "numeric", 7], "8 of Spades": ["black", "spade", "numeric", 8], "9 or Spades": ["black", "spade", "numeric", 9], "10 of Spades": ["black", "spade", "numeric", 10], "Jack of Spades": ["black", "spade", "face"], "Queen of Spades": ["black", "spade", "face"], "Kings of Spades": ["black", "spade", "face"],
         "Ace of Hearts": ["red", "heart", "numeric", 1], "2 of Hearts": ["red", "heart", "numeric", 2], "3 of Hearts": ["red", "heart", "numeric", 3], "4 of Hearts": ["red", "heart", "numeric", 4], "5 of Hearts": ["red", "heart", "numeric", 5], "6 of Hearts": ["red", "heart", "numeric", 6], "7 of Hearts": ["red", "heart", "numeric", 7], "8 of Hearts": ["red", "heart", "numeric", 8], "9 or Hearts": ["red", "heart", "numeric", 9], "10 of Hearts": ["red", "heart", "numeric", 10], "Jack of Hearts": ["red", "heart", "face"], "Queen of Hearts": ["red", "heart", "face"], "Kings of Hearts": ["red", "heart", "face"],
         "Ace of Clubs": ["black", "club", "numeric", 1], "2 of Clubs": ["black", "club", "numeric", 2], "3 of Clubs": ["black", "club", "numeric", 3], "4 of Clubs": ["black", "club", "numeric", 4], "5 of Clubs": ["black", "club", "numeric", 5], "6 of Clubs": ["black", "club", "numeric", 6], "7 of Clubs": ["black", "club", "numeric", 7], "8 of Clubs": ["black", "club", "numeric", 8], "9 or Clubs": ["black", "club", "numeric", 9], "10 of Clubs": ["black", "club", "numeric", 10], "Jack of Clubs": ["black", "club", "face"], "Queen of Clubs": ["black", "club", "face"], "Kings of Clubs": ["black", "club", "face"],
         "Ace of Diamonds": ["red", "diamond", "numeric", 1], "2 of Diamonds": ["red", "diamond", "numeric", 2], "3 of Diamonds": ["red", "diamond", "numeric", 3], "4 of Diamonds": ["red", "diamond", "numeric", 4], "5 of Diamonds": ["red", "diamond", "numeric", 5], "6 of Diamonds": ["red", "diamond", "numeric", 6], "7 of Diamonds": ["red", "diamond", "numeric", 7], "8 of Diamonds": ["red", "diamond", "numeric", 8], "9 or Diamonds": ["red", "diamond", "numeric", 9], "10 of Diamonds": ["red", "diamond", "numeric", 10], "Jack of Diamonds": ["red", "diamond", "face"], "Queen of Diamonds": ["red", "diamond", "face"], "Kings of Diamonds": ["red", "diamond", "face"]}

colors = ["red", "black"]
suits = []

color_guess = str(random.choice(colors))


print("There are 52 cards in a standard deck of cards. Please select 1 and I will try to guess it.")
print("'Aces' are not considered a face card and has a value of 1.")
print("When I ask a question, please respond with yes or no (y/n).")

first_question = input(f"Is your card {color_guess}? (y/n): ")

if first_question == "y":
  for card, color in list(deck.items()):
    if color[0] != color_guess:
      del deck[card]
else:
  for card, color in list(deck.items()):
      if color[0] == color_guess:
        del deck[card]

if (color_guess == "red" and first_question == "y") or (color_guess == "black" and first_question == "n"):
  suits = ["heart", "diamond"]
if (color_guess == "black" and first_question == "y") or (color_guess == "red" and first_question == "n"):
  suits = ["spade", "club"]


suit_guess = str(random.choice(suits))

second_question = input(f"Is your card a {suit_guess}? (y/n): ")

if second_question == "y":
  for card, suit in list(deck.items()):
    if suit[1] != suit_guess:
      del deck[card]
else:
  for card, suit in list(deck.items()):
      if suit[1] == suit_guess:
        del deck[card]

third_question = input(f"Is your card a face card? (y/n): ")

if third_question == "y":
  for card, numeric_or_face in list(deck.items()):
    if numeric_or_face[2] != "face":
      del deck[card]

  card_list = list(deck.keys())
  computer_guess = random.choice(card_list)
  card_list == card_list.remove(computer_guess)
  first_guess = input(f"Is your card the {computer_guess}? (y/n): ")

  if first_guess == "y":
    print("I have guessed your card on the first try!")
  else:
    computer_guess_2 = random.choice(card_list)
    card_list == card_list.remove(computer_guess_2)
    second_guess = input(f"Is your card the {computer_guess_2}? (y/n): ")
    
    if second_guess == "y":
      print("I have guessed your card on the second try!")
    else:
      final_guess = random.choice(card_list)
      print(f"Then your card must be the {final_guess}!")