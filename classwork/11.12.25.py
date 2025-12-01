# Haunted House Theme
############################################################
# Title: Haunted House Sprint
# Author: Carmen Amond
# Descprition: Text-based adventure simulation game in Python
# The player makes choices at each stage, leading to different outcomes
# The goal is to survive and escape the house!
############################################################
# Read the story and type in the optins shown in brackets []
# Press Enter after typing your choice
# Each choice leads to a new situiation or ending
# There are at least three decision stages in this game
#############################################################

# ------------------------------------------------------------
# Stage 0: Introduction
# ------------------------------------------------------------
# print() to display text for the user to read
print("Welcome to Haunted House Sprint!")
# ------------------------------------------------------------
# Stage 1: First Choice
# ------------------------------------------------------------
# input() to ask for a response
# .strip() to remove extra spaces
# .lower() convert input to lower case
choice1 = input("You enter a dim foryer. Go [left] toward whisper or go [right] towards lights?").strip().lower()

# The 'if' keyword checks a condition. If it is true, the code inside runs.
# Stage 1a: left or right choice
if choice1 == "left":
    # This block will run if the user typed left
    print("You went left towards the whispers")
else:
    print("You went right towards the light")
# ------------------------------------------------------------
# Stage 2: Run or no?
choice2 = input("A ghost blocks the hall. Do you [run] past or [ask] it for help?").strip().lower()

if choice2 == "run":
    print("you ran past")
else:
    print("you asked")
# ------------------------------------------------------------
# Stage 3: Locked Door
choice3 = input("A door is ahead. Is it [locked] or [open]?").strip().lower()

if choice3 == "locked":
    print("The door is locked")
else:
    print("The door is open")
# ------------------------------------------------------------
# Stage 4: questions
# can be added from the class recording.
# ------------------------------------------------------------