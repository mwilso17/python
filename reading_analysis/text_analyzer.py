text_string = "This is a string of text."

def get_word_count(text):
  split_text = text.split()
  word_count = len(split_text)
  print(f"There are {word_count} words in this text.")


get_word_count(text_string)