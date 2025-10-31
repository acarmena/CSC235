# a Python Tutorial application on user input and slight variable usage.
# This code will teach the user how to ask for user inputs.
# To use this code you will answer the questions as they come.
# To see how input work from the user side as well as the programmer side.
# more info can be found on W3 Schools

print("Hi, welcome to a Python tutorial!") #start of code
print() #spacing for readability

print("Today, we are going to learn how to take user inputs!")
print() #spacing for readability

ans = input("To begin, what do you think you need to type? ") #variable to save the input from user

if ans == "input" : #if-else statement to handle user input
    print("Correct! You would type this for example: input('blah blah ')") #regular input example
    print() #spacing for readability
else:
    print("Wrong, but! that is why we are learning!")
    print("To ask for a user input, you need to type this 'input('whatever you want to ask the user')'")
    print() #spacing for readability


print("If you want to save the input in a variable you would do that same but set the input equal to a variable name.")
print() #spacing for readability

print("Let's try!")
name = input("Enter your name: ")
print() #spacing for readability

print("You notice how the code prompted you to enter answer earlier and just now?")
print("yeah! that is how the user enters information.")
print() #spacing for readability

print("Now if I wanted to print it as a variable I would say: 'variable = input('blah blah')'") #variable example
print("Then print the variable name.")
print("Like this:")
print(name + ". See how the name you entered earlier is printed again, without you typing again?") #concatinate example
print() #spacing for readability

print("congrats! See you next time.") #end of code