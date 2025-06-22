# This file takes a text, splits its words into a list, and then prints the words
# in that list at whatever speed the user wants (200 or 300 words per minute currently).

# TODO: Allow users to put in their own reading speed (input your reading speed, divide 60 by that number?).
# exit loop on key press. pause/resume on key press. Allow user to increase or decrease speed 
# on keypress or during pause. Validation for user input. Speed limits for user input (ie: someone says they
# read at 1400 words per minute, ask them if they are sure.)
import time

text_file = open("reading_analysis\\shorter_sample.txt", encoding="utf-8")

def split_text(filename):
    try:
      with text_file as file:
        text_data = file.read()
        content = text_data.translate(str.maketrans('', ''))
        word_list = content.split()
        return word_list
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")


words_in_file = split_text(text_file)

two_hundred_wmp = .3
three_hundred_wmp = .2

user_wmp = input("Please enter your reading speed in words per minute: ")
user_wmp_int = int(user_wmp)
converted_wmp = 60/user_wmp_int

for word in words_in_file:
   print(word)
   time.sleep(converted_wmp)