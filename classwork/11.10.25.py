###

### Decision Logic Activity Adventure

### This fun activity teaches:
# Structured programming (sequencing/ selection/ decision/ iterations/ loops)
# Expressions and operators (aritmetic/ comparisson, logial assignments)
# If/ elif/ else + nested decisions
# basis: writing tiny, readable functions

##########################################################
# print_lines() just prints a divider line to make console output easier to read 

def print_lines(): #defines a simple helper function with no inputs 
    # This function prints a visual divider line 
    print("_" * 60) # multipying a sting ('_') by 60 repeats it 60 times 

#---------------------------------------------------------------------------
# 1) SEQUENCE: step by step intro + warm up math
#---------------------------------------------------------------------------
# Print a welcome banner to set the theme of the activity
print_lines() # call our helper function to draw a divider 
print("Welcome to the Decision Logic Adventure!")
print("We'll explore operators, expressions, and conditional logic together")
print_lines()

# Demonstrate an expression with arithmetic operators 
# We'll compute a pretend "adventure energy score" using arithmetic operations 
base_energy = 10 # assignment operator (=) binds value 10 to the name base_energy
bonus_energy = 5 * 2 # multiplication operator (*) and assignment (=); 5*2=10
total_energy = base_energy + bonus_energy # addition operators (+); 10+10=20

# Show results to the learner 
print(f"Base Energy: {base_energy}") #f-string prints the variable value nicely
print(f"Bonus Energy: {bonus_energy}") # display the computed bonus 
print(f"Total Energy: {total_energy}") # display the total 
print_lines()

#-------------------------------------------------------------------------------
#2) INPUT + VALIDATION (SEQUENCE) --> Leads into DECISION (SELECTION)
#-------------------------------------------------------------------------------
# Ask the learner for their name using input(), which will return a string 
player_name = input("What's your name, adventurer? ") # save user input to a variable 

# Use strip() to remove extra spaces the user might accidentally add 
player_name = player_name.strip() # cleans up the input 

# If the user provided an empty name, give them a friendly default 
if player_name == "": # comparison operator (==) check equality
    # Selection: If the condition is TRUE, run this block
    player_name = "Brave Coder"
    print("No worries, we'll call you 'Brave Coder! ") # let them the default was used 

# Say hello to the player with (possible default name)
print(f"Great to meet you, {player_name}")
print_lines()

#-------------------------------------------------------------------------------
#3) OPERATORS AND EXPRESSIONS 
#-------------------------------------------------------------------------------

# Arithmetic operators: +, -, *, /, %, 
a = 9
b = 4
sum_ab = a + b
difference = a - b
product = a * b 
true_division = a / b # true division (float) results should be 2.25 
floor_division = a // b # floor division result should be 2 (dropping remainder)
remainder = a % b # modulus gives remainder for 9 % 4 = 1 
power = a ** b # exponentiation (9 ** 4) 6561

# Show arithmetic results 
print("Arithmetic Examples:")
print(f"{a} + {b} = {sum_ab}")
print(f"{a} / {b} = {true_division}")
print(f"{a} // {b} = {floor_division}")
print_lines()

# Comparison Operators: ==, !=, >, <, >=, <= 
x = 7 
y = 10 

print("Comparison Examples:")
print(f"{x} == {y} -> {x == y}") # False 7 is not equal to 10 
print(f"{x} != {y} -> {x != y}") # True 7 is not equal to 10 
print(f"{x} > {y} -> {x > y}") # False 
print(f"{x} >= {7} -> {x >= 7}") # true 
print_lines()

# Logical Operators: and, or, not 
is_sunny = True # Boolean True 
have_hat = False # Boolean False 

print("Logical Examples:")
print(f"is_sunny and have_hat -> {is_sunny and have_hat}") # and needs BOTH true -> False
print(f"is_sunny or have_hat -> {is_sunny or have_hat}") # or needs EITHER true -> True 
print(f"not have_hat -> {not have_hat}") # not flips the boolean TRUE 
print_lines()

#------------------------------------------------------------------------------
#4) SELECTION: if / elif / else - branching based on a condition
#------------------------------------------------------------------------------
# Let's ask a simple question to drive the branching logic 
choice = input("Choose a path (left/right/straight): ").strip.lower() # normalize text 

# Begin branching using if / elif / else 
if choice == "left": # if player types left, this block runs
    print("You find a friendly dragon who shares wisdom!") #fun outcome 
elif choice == "right": # If the first condition was False but this is true 
    print("You discover a treasure chest filled with gears and gadgets")
elif choice == "straight": #Another branch
    print("You meet a guide who gives you a map!")
else: # if none of the above matched, run this default branch 
    print("You wander in circles until you decide to try again...")
print_lines()

#-------------------------------------------------------------------------------
#5) NESTED DECISION - decision inside another decision 
#-------------------------------------------------------------------------------

# Prompt the user about having a key and knowing the secret code 
has_key_input = input("Do you have the golden key? (yes/no): ").strip().lower()
knows_code_input = input("Do you know the secret code? (yes/no): ").strip().lower()

# Convert text answer to booleans for cleaner logic
has_key = (has_key_input == "yes") # True if user types 'yes'
knows_code = (knows_code_input == "yes") # True if user types 'yes'

# Nested Decision: outer decision checks for key and inner decision checks for the code 
if has_key: # outer decision
    # only run this block if user has the key 
    if knows_code: #inner decision
        print("Door opens! You enter the Hall of Knowledge") # if both conditions are true 
    else: 
        print("The door is locked. You need the code.") # Has the key but not the code 
else: 
    print("No Key? The door won't budge.") # No key at all
print_lines()

#-----------------------------------------------------------------------------------
#6) WRAP UP - RECAP OF WHAT WE LEARNED
#-----------------------------------------------------------------------------------
print("RECAP: You practiced.....")
print(" - Sequence: reading inputs, computing values, printing results in order")
print(" - Selection: if / else if / else (including nested decision)")
print(" - Operators: arithmetic, comparison, logical, assignment")
print_lines()

print("Nice work, {name}! Keep experimenting and have fun coding in VS code!".format(name=player_name))
print_lines()