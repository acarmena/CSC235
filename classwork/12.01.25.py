# ------------------------------------------------------------
# HERO SIMULATOR LITE
# OOP (OBJECT ORIENTED PROGRAMMING), ENCAPSULATION, INHERITANCE, GUI
# ------------------------------------------------------------
# This program demonstrates:
# How to create classes and objects
# How to use inheritance to extend base classes
# How 
# GOAL: is to see an object (a hero) respond when GUI buttons are clicked
# ------------------------------------------------------------
# Import tkinter (python built in GUI library)
import tkinter as tk

# ------------------------------------------------------------
# Part 1: Create the base class
# ------------------------------------------------------------
class Character:
    # the constructor (__init__) runs when a new Character is created
    def __init__(self, name):
        # Store the character name
        self.name = name
        # health is encapsulated (protected)
        # meaning it shouldn't be changed directly outside the class
        self.health = 100

    # a basic attack that all character share
    def do_basic(self):
        return f"{self.name} perform a basic attack!"
        
# ------------------------------------------------------------
# PART 2: Create Child Classes
# ------------------------------------------------------------
# Wizard is a child of character, so it inherits everything from Character
class Wizard(Character):
    # A special move unique to Wizard
    def special(self):
        return f"{self.name} casts a blazing Fireball!"
    # Warrior is another child class of Character, so it inherits from Character
class Warrior(Character):
    # A special move unique to Warrior
    def do_special(self):
        return f"{self.name} swings a mighty Sword Slash!"
# ------------------------------------------------------------
# PART 3: Create the GUI
# ------------------------------------------------------------
class HeroGUI:
    # set up the GUI window and objects
    def __init__(self, root):
        # create a hero object (Wizard or Warrior)
        # you can change wizard to warrior if you want
        self.hero = Wizard("Gandalf")
        # self.hero = Warrior("Blaze")

        # create a label at the top of the GUI
        self.label = tk.Label(root, text = "Choose an action for your hero:")
        self.label.pack() #pack() places the label in the window

        # button for basic attack
        self.basic_btn = tk.Button(root, text = "Basic Attack", command = self.do_basic) #calls method when button clicked
        self.basic_btn.pack()

        # button for special move
        self.special_btn = tk.Button(root, text = "Special Move", command = self.do_special)
        self.special_btn.pack()

        # output area to show results on the screen
        self.output = tk.Label(root, text = "", font =("Arial", 14))
        self.output.pack()

# ------------------------------------------------------------
# PART 4: Event Handlers; these methods run when buttons are clicked
# ------------------------------------------------------------

    # Respond to basic attack button click
    def do_basic(self):
        # updates the label text to show the result of the basic attack's message
        self.output.config(text = self.hero.do_basic())

    # Respond to special move button click's text
    def do_special(self):
        # updates the label text to show the result of the special move's message
        self.output.config(text = self.hero.special())

# ------------------------------------------------------------
# PART 5: MAIN PROGRAM
# -----------------------------------------------------------
# create the main GUI window
root = tk.Tk()

# set the window title
root.title("Hero Simulator Lite")

# create an instances of the GUI application
app = HeroGUI(root)

# start the GUI event loop
root.mainloop()

# ------------------------------------------------------------
# END OF PROGRAM
# ------------------------------------------------------------