deck = {"Ace of Spades": "black", "2 of Spades": "black", "3 of Spades": "black", "4 of Spades": "black", "5 of Spades": "black", "6 of Spades": "black", "7 of Spades": "black", "8 of Spades": "black", "9 or Spades": "black", "10 of Spades": "black", "Jack of Spades": "black", "Queen of Spades": "black", "Kings of Spades": "black",
         "Ace of Hearts": "red", "2 of Hearts": "red", "3 of Hearts": "red", "4 of Hearts": "red", "5 of Hearts": "red", "6 of Hearts": "red", "7 of Hearts": "red", "8 of Hearts": "red", "9 or Hearts": "red", "10 of Hearts": "red", "Jack of Hearts": "red", "Queen of Hearts": "red", "Kings of Hearts": "red",
         "Ace of Clubs": "black", "2 of Clubs": "black", "3 of Clubs": "black", "4 of Clubs": "black", "5 of Clubs": "black", "6 of Clubs": "black", "7 of Clubs": "black", "8 of Clubs": "black", "9 or Clubs": "black", "10 of Clubs": "black", "Jack of Clubs": "black", "Queen of Clubs": "black", "Kings of Clubs": "black",
         "Ace of Diamonds": "red", "2 of Diamonds": "red", "3 of Diamonds": "red", "4 of Diamonds": "red", "5 of Diamonds": "red", "6 of Diamonds": "red", "7 of Diamonds": "red", "8 of Diamonds": "red", "9 or Diamonds": "red", "10 of Diamonds": "red", "Jack of Diamonds": "red", "Queen of Diamonds": "red", "Kings of Diamonds": "red"}


print(len(deck))

for card, color in list(deck.items()):
  if color == "red":
    del deck[card]

print(len(deck))