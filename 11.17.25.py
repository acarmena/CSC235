# Guessing game
# ------------------------------------------------------------
# Python Loops & Functions
# Number Guessing Game
# ------------------------------------------------------------
# we need to import a module/ library to generate a number
import random
# ------------------------------------------------------------
# Function: greet_player
# Purpose: print a welcome message to the user
# Inputs: player_name (string)
# returns: None
# ------------------------------------------------------------
def greet_player(player_name):
    # use a f-string to include the player's name in the message
    print(f"\nWelcome, {player_name}!")
    print("We're going to play a number guessing game.")
    print("Try to guess the secret number in as few tries as possible.")
# ------------------------------------------------------------
# Function: get_secret_number
# Purpose: generate and return a random number
# Inputs: none
# Returns: secret_number(int)
# ------------------------------------------------------------
def get_secret_number():
    # random.randint(1, 20) returns integer between 1 and 20(inclusive)
    secret_number = random.randint(1, 20)
    return secret_number # we send secret number back to the caller
# ------------------------------------------------------------
# Function: play_round
# Purpose: play one round of the guessing game
# Inputs: round_number(int)
# Returns: number of guesses (int) if guessed correctly in time
# ------------------------------------------------------------
def play_round(round_number):
    print(f"\n===== ROUND {round_number} =====")
    secret_number = get_secret_number()

    # set the max number of guesses
    max_guesses = 5

    # initialze a counter for guess number
    guesses_used = 0

    # use while loop to let the user guess multiple times
    # the loop keeps goinf as long as guess-used is less than max_guesses
    while guesses_used < max_guesses:
        # ask the iser for a guess and convert it to an integer
        guess = int(input("Enter your guess (1 to 20): "))

        # increase the number of guesses by 1
        guesses_used += 1

        # check of the guess is correct
        if guess == secret_number:
            print("Correct! You guesses the secret number!")
            print(f"You used {guesses_used} guess(es).")
            # return the num of guesses
            return guesses_used
        
        # if the guesses is too low, give a hint
        elif guess < secret_number:
            print("too low! Try again.")

        # if the guess is too high
        else:
            print("too high! Try again")
        
        # If the player still has guesses left, ltk
        if guesses_used < max_guesses:
            print(f"You have {max_guesses - guesses_used} guesses left. \n")
        # if we exit like normal, ran out of guesess
        print("\n Out of guesses!")
        print(f"The number was: {secret_number}")
        # we return none to show the player did not guess the number
        return None
# ------------------------------------------------------------
# Function: summary
# Purpose: show a summary of how the player played
# Input: resultList (list of guesses per round or None)
# return: none
# ------------------------------------------------------------
def summary(resultList):
    print("\n===== GAME SUMMARY =====")

    # use a for loop to go through each round result
    # enumerate gives both the index (round num) and the value (guesses_used)
    for index, guesses_used in enumerate(resultList, start = 1):
        # if guesses_used is none, the player did not guess correctly that round
        if guesses_used is None:
            print(f"Round {index}: Did not guess correctly")
        else:
            print(f"Round {index}: Guessed Correctly in {guesses_used} guess(es).")

    # Optional: we can calculate how many rounds were successful
    # 
    successful_rounds = 0
    # loop through the list again
    for guesses_used in resultList:
        # if the value is not None, that means it was a successful round.
        if guesses_used != None:
            successful_rounds += 1
        # after the loop, print out how many rounds were successful
        print(f"\nYou guessed correctly in {successful_rounds} out of {len(resultList)} round(s).")

# ------------------------------------------------------------
# Function: Main
# Purpose: this is the main function that runs the whole game
# Inputs: none
# Returns: none
# ------------------------------------------------------------
def Main():
    # ask user for their name
    player_name = input("What is your name? ")
    # call greeting
    greet_player(player_name)
    # ask how many rounds
    total_rounds = int(input("How many rounds would you like to play? "))

    # create an empty list to store results
    round_results = []

    # use for loop to play multiple rounds
    # range(total_rounds) will loop from 0 up to - 1 the total rounds
    # we add 1 to should round beginging at 1
    for round_number in range(1, total_rounds + 1):
        # call play round and capture the result
        play_round()