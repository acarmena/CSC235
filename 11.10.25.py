###

### Decision Logic Activity Adventure

### This fun activity teaches:
# Structured programming (sequencing/ selection/ decision/ iterations/ loops)
# Expressions and operators (aritmetic/ comparisson, logial assignments)
# If/ elif/ else + nested decisions
# basis: writing tiny, readable functions

##########################################################
# print_line() - prints a divder line to make console output easier to read

def print_line(): # defines a simple helper function withno inputs
    # function prints a visual divider line
    print("_" * 60) # multiplying a string ('_') by 60, it repeats 60 times

############################################################
# 1) SEQUENCE: step by step intro + warm up
# -----------------------------------------
# Print a welcome banner to set the theme of the activity
print_line() # calls function
print("Welcome to the Decision logic Adventure")
print("We'll explore operators, expressions, and conditional logic together")
print_line()

# Demonstrate an expression with arithmetic operators
# We'll compute a pretend "adventure energy score" using arithmetic operations
base_energy = 10 # assign operrator(=) binds value 10 to the name base_energy
bonus_energy = 5 * 2 # multiplicatin operator (*) and assignment (=)
total_energy = base_energy + bonus_energy # addition operator(+)

# Show results to user
print(f"Base Energy: {base_energy}")
print(f"Bonus Energy: {bonus_energy}")
print(f"Total Energy: {total_energy}")

print("RECAP: You practiced...")
print(" - Sequence reading inputs, computing values, ")
print("")
print("")