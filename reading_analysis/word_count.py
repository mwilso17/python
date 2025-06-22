import string

text_file = open("reading_analysis\\frankenstein.txt", encoding="utf-8")

def get_word_count(filename):
    try:
      with text_file as file:
        text_data = file.read()
        content = text_data.translate(str.maketrans('', '', string.punctuation)).lower()
        word_list = content.split()
        word_count = len(word_list)
        print(f"There are approximately {word_count} words in this text.")
    except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")

get_word_count(text_file)