# This program uses first_names.txt and last_names.txt in order to generate a new character name.
# As the list of names grows from user input, so does the number of unique combinations of new names.
# TODO: trailing \n in txt files cause blank name to appear. Need to handle that.

import random

first_names = open("rpg_helper\\first_names.txt")
last_names = open("rpg_helper\last_names.txt")

first_name_list = first_names.read().split("\n")
last_name_list = last_names.read().split("\n")

generated_first_name = random.choice(first_name_list)
generated_last_name = random.choice(last_name_list)
generated_full_name = generated_first_name + " " + generated_last_name

print("Your generated name is: " + generated_full_name)
