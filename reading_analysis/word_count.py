import string
from collections import Counter

# TODO: exclude or option to exclude common words like a, the, in, of, etc. Regex to only consider words of 4 characters or more in 
# common word list. Calculator for wmp, minutes per day to read, user input for those days.
# Allow user to decide how many words appear on most common list. Need further logic on most_common_words def: currently returning
# some wrong information (like Elizabeth (99th most common) returning 81 times although text has more instances).
# punctuation with quotes if off (showing the word 'night"' as different than 'night').

text_file = open("reading_analysis\\frankenstein.txt", encoding="utf-8")

def get_word_count(filename):
    try:
      with text_file as file:
        text_data = file.read()
        content = text_data.translate(str.maketrans('', '', string.punctuation)).lower()
        word_list = content.split()
        word_count = len(word_list)
        return word_count, word_list
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
   
def most_common_words(list):
   count_words = Counter(list)
   most_common = count_words.most_common(10)
   return most_common

def least_common_words(list):
   count_words = Counter(list)
   least_common = count_words.most_common()
   return least_common

word_count, word_count_list = get_word_count(text_file)
most_common = most_common_words(word_count_list)
least_common = least_common_words(word_count_list)

print(f"There are approximately {word_count} words in this text.")

print("The most common words and their frequency in appearance are: ")
for word, frequency in most_common:
   print(f"The word: {word} appears {frequency} times.")

print("The least common words appearing at least 20 times but less than 50 times are: ")
for word, frequency in least_common:
  if frequency <=50 and frequency >= 20:
    print(f"The word: {word} appears {frequency} times.")
  else:
    pass