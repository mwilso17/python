# This file takes a text, splits its words into a list, and then prints the words
# in that list at whatever speed the user wants (200 or 300 words per minute currently).

# TODO: get rid of lower case only. Allow users to put in their own reading speed (input your reading speed, divide 60 by that number?).
# allow document text to retain punctuation. exit loop on key press. pause/resume on key press. Allow user to increase or decrease speed 
# on keypress or during pause.
import string
import time

text_file = open("reading_analysis\\shorter_sample.txt", encoding="utf-8")

def split_text(filename):
    try:
      with text_file as file:
        text_data = file.read()
        content = text_data.translate(str.maketrans('', '', string.punctuation)).lower()
        word_list = content.split()
        return word_list
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")


words_in_file = split_text(text_file)

two_hundred_wmp = .3
three_hundred_wmp = .2

for word in words_in_file:
   print(word)
   time.sleep(two_hundred_wmp)