# ############################################
# Time Machine Journal
# Purpose:
# # Practive Variables, input/output, and file reading & writing
# # Demonstrates text fil creation and persistence between runs

###
# ==================================
# This program demonstrates basic Python I/O (input/output) and how to save user data in a text file
###

# Step 1: Display a welcome message to the user
print("=================================================")
print("\t TIME MACHINE JOURNAL")
print("=================================================")
print("You can record journal entries that are saved between uses.")
print("Each entry included your name, year, and experience.")

#  Step 2: Collect user input(different data types)
# String variable - stores a user's name as text
name = input("What is your name? ")

# Integer variable - stores numeric value (whole numbers)
year = int(input("What year are you visiting today? "))

# Float variable - stores decimal values(4.5, etc)
rating = float(input("Rate this time-travel trip from 1.0 to 5.0: "))

# Another string variable = user enters a journal entry
entry = input("Write your journal entry: ")

# Step 3: Write data to a text file
# 'a' means append (add w/o erasing previous entries)
# encoding ='UTF-8'- allows special characters/emojis to be saved properly
with open ("journal.txt", "a", encoding ="utf-8") as f:
    f.write(f"Name: {name} | Year: {year} | Rating: {rating: .1f} | Entry: {entry}\n")

# Confirmation message for user feedback
print("\n Your entry has been saved to 'journal.txt'.") 

# Step 4: Ask if the user wants to read the previous journal entries
see_entries = input("Would you like to read your past journal entries? (y/n) ").lower()

# If the user types 'y', open the file and display contents

if see_entries == "y":
    try:
        # open file read mode ('r') and display all text
        with open("journal.txt", "r", encoding="utf-8") as f:
            history = f.read()
            print("\n --- Past Entries ---")
            print(history)
            print("-----------------------")
    except FileNotFoundError:
        # this will run of the file does not exist
        print("No Journal file found yet --- make an entry first.")

# Step 5: Goodbye message
print(f"\n Thank you, {name}")