# Loop_simulation.py
#---------------------------------------------------------------
# This program is a simple text-based simulation
# that demonstrates 
# - Functions
# - While Loops 
# - For Loops 
# - break and continue 
# - Parameters and return values 
# - Asking the user if they want to play again
#-------------------------------------------------------------------

# This function prints a visual divider line to improve UX
def print_divider():
    # Print a line of dashes to visually separate sections
    print("\n" + "-" * 50 + "\n")

# This function asks the player for their name and returns it 
def get_player_name():
    # Ask the user to type their name.
    name = input("Welcome, explorer! What's your name? ")
    # Return the name so other functions can use it
    return name 

# This function displays options and returns a valid choice 
# It accepts a parameter called "options" which is a dictionary that maps menu numbers like 1, 2
# to description text 
def get_player_choice(options):
    #Use a while loop to keep asking until the user enters a valid choice
    while True:
        # Print each option using a for loop
        # The for loop interates over the key value paires in the options dictionary
        for key, description in options.items():
            # Print the menu line for this option.
            print(f"{key}. {description}")
        
        # Ask the user to choose one of the menu options
        choice = input("Please enter the number of your choice: ")

        #If the user's choice is one of the keys in the options dictionary..
        if choice in options:
            # We break out of the while loop by returning the valid choice 
            return choice 
        else:
            # If the choice id not valid, tell the user
            print("\n That is not a valid choice. Please try again. \n")

# The function prints the introduction to the simulation and returns the player's name 
def show_intro():
    #Call print_divider() to separate the intro from the rest of the text.
    print_divider()

    #Print a welcome message that explains the story
    print("Welcome to the Loop Quest Simulation")
    print("In this adventure, your decisions are powered by loops and functions!")
    print("You will explore a magical world as we secretly practice Python concepts.")

    # Call get_player_name() to ask for player's name
    name = get_player_name

    #Greet the player using their name
    print(f"\nNice to meet you, {name}! Let's begin your journey.")

    # Return the player's name so other functions can use it
    return name 

# This function represents the "forest" path in the story
# It takes name as a parameter so we can personalize messages 
# It return a score based on what the player does 
def forest_path(name):
    # Call print_divider() to separate this section visually
    print_divider()

    # Let the player know where they are
    print("f {name}, you chose to enter the Enchanted Forest.")
    print("The forest is quiet, and you feel a soft glow around you.")

    # Start the player with a base score of 0.
    score = 0

    #Create a list of tasks the player must complete in the forest
    forest_tasks = [
        "Cross a narrow bridge over a river"
        "Solve a glowing rune puzzle on a stone"
        "Help a lost traveler find their way"
    ]

    # Use a for loop to go through each task in the forest_tasks
    for tasks in forest_tasks:
        #Describe the current task
        print(f"\nYou encounter a challenge: {tasks}")
        # Ask the player if they want to try the task
        answer = input("Do you attempt this challenge? (y/n): ").lower()

        #If the player types y, they gain points 
        if answer == "y":
            print("You bravely complete the challenge and gain 10 points!")
            # Increase score by 10
            score += 10
        # If the player types n, they skip the task
        elif answer == "n":
            print("You decide to skip this challenge and move on.")
            # Score does not change
        else: 
            #If the input is not "y" or "n" give a default response
            print("You hestitate and the opportunity passes by...")
    
    # After the loop, print a summary message 
    print(f"\nYou leave the forest with a score of {score} points.")

    # Return the final score from the forest path
    return score 

# This function represents the "city" path in the story
# It also takes the name as a parameter and returns a value 
def city_path(name):
    print_divider()

    # Let the player know where they are
    print(f" {name}, you chose to explore the Cyber City.")
    print("Neon lights flash around you, and the air buzzes with energy.")

    # Start the player with 0 points 
    score = 0

    # Use a while loop to simulate visiting different city districts 
    # Well allow the player to visit up to 3 districts 
    visits = 0 # this variable counts how many districts have been visited 

    # Start with the loop that continues while visits is less than 3
    while visits < 3:
        print(f"\n You have visited {visits} district(s) so far.")

        #Create options for which district to visit next
        options = {
            "1": "Tech Market (trade gadgets for knowledge points)",
            "2": "Energy Plaza (restore your stamina with glowing drinks)",
            "3": "Sky Rails (take a quick tour of the skyline and end your city visit)",
        }

        # Call get_player_choice() to ask which district to visit
        district_choice = get_player_choice(options)

        # IF the player choose option "1"
        if district_choice == "1":
            print("\nYou explore the Tech Market and trade gadgets for data points!")
            score += 8
            visits += 1
        elif district_choice == "2":
            print("\nYou relax at the Energy Plaza and feel refrshed!")
            score += 5
            visits += 1
        elif district_choice == "3":
            print("\nYou ride the Sky Rail and enjoy the beautiful city view.")
            print("Your city adventure ends with a burst of inspiration!")
            score += 12
            # Use a break to exit the while loop early
            break

        # This else block will not normally run because get_player_choice() guarantees a valid choice
        # It is included for completeness
        else:
            print("Something unexpected happened in the city...")
            # Use the continue to go back to the top of the while loop
            continue
    # After the loop ends, print summary message 
    print(f"\nYou leave the city with a score of {score} points.")
    return score 

# This function asks the player which main path they want to take 
def choose_main_path(name):
    print_divider()

    # Explain the two main path options to the player 
    print("You stand at a crossroads between two adentures:")
    print("1. The Enchanted Forest (mystical and calm)")
    print("2. The Cyber City (futuristic and energetic)")

    # Create a dictionary of options to pass into get_player_choice()
    options = {
        "1": "Enter the Enchanted Forest",
        "2": "Visit the Cyber City",
    }

    # Call get_player_choice() to get a valid path choice from the player 
    path_choice = get_player_choice(options)

    if path_choice == "1":
        score = forest_path(name)
    else:
        score = city_path(name)
    return score 

# This function shows the final result of the simulation
# It does take the player's name and score as parameter and does not return a value 

def show_results(name, score):
    print_divider()

    # Print the player's final score 
    print(f"Adventure complete, {name}!")
    print(f"Your final score is: {score} points.")

    # Use if / elif / else to give different feedback based on the score 
    if score >= 30:
        print("Incredible! You made brave and wise choice throughout your journey.")
    elif score >= 15:
        print("Great job! You explored thoughtfully and made solid decisions.")
    else: 
        print("You took cautious path. Next time, try taking a few more risks!")
    
    # End with a friendly message 
    print("\nThanks for playing Loop Quest Simulation!")

# this function runs one full version of the simulation from start to finish
def run_simulation():
    name = show_intro()

    score = choose_main_path(name)

    show_results(name, score)

# This is the main function that controls replaying the simulation 
def main():
    print("Welcome to the Loops & Functions Simulation Assignment!\n")

    # Start with while loop to allow the player to replay the simulation
    while True:
        run_simulation()

        # Ask the user if they want to play again
        replay = input("\nWould you liek to run the simulation again? (y/n): ").lower()

        if replay == "y":
            print("\nRestarting the simulation...\n")
            continue
        elif replay == "n":
            print("\nThanks for exploring loops and functions today, Goodbye!")
            break
        else:
            print("\n I didn't understand that, let's ask again.")
            continue

# This line checks if the script is being run directly (not imported).
# If it is, it calls main() to start the program
if __name__ == "__main__":
    main()