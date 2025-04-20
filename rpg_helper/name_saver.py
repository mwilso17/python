# This program saves user names into a file. The names from this file can later be used to create new characters.

first_name_file = open("rpg_helper\\first_names.txt", "a")
last_name_file = open("rpg_helper\last_names.txt", "a")

first_name = input("Please enter your character's first name: ")
last_name = input("Please enter your character's last name: ")

first_name_file.write(first_name + "\n")
last_name_file.write(last_name + "\n")