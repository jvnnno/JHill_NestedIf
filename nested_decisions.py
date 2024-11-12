# Task 1: Code Correction You are provided with a Python script that 
# is supposed to guide a user through an adventure game, but it has 
# some errors. Identify and fix them.

# Original Buggy Code:

place = input("Choose a place: forest or cave? ")  

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")


    # My correction:


place = input("Choose a place: forest or cave? ")
action = "climb a tree"  # <--- "action" needed to be defined as a variable 

if place == "forest":  # <---- need (==) instead of single (=), not comparison, value.
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":  # <---- "if" statement better fit, 2nd condition, "action" is not a set variable. Additionally needed (==) to express value.
        print("You found a bird's nest!")
    else:        # <--- "cross a river" not necessary when only other option. "else" gets same result.
        print("You found a boat!")
if place == "cave":    # <--- Elif statement not needed, 2nd separate condition
    print("You find a hidden treasure!")


# Task 2: Setting the Scene

# Based on your corrected code from Task 1, expand the game. If the user 
# chooses "cave", ask them if they want to "light a torch" or "proceed 
# in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")
action = "climb a tree"  

if place == "forest":  
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":  
        print("You found a bird's nest!")
    else:      
        print("You found a boat!")
if place == "cave":   
    action == input("Light a torch? Or proceed in the dark?")
    if action == "light a torch":
        print("You now have a light to proceed through the tunnel!")
    else:
        print("Good luck! Be careful in the dangerous dark cave!")


# Task 3: Default Path

# If the user makes an invalid choice at any point, incorporate 
# a pass statement to handle it. 

place = input("Choose a place: forest or cave? ")
action = "climb a tree"  

if place == "forest":  
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":  
        print("You found a bird's nest!")
    else:      
        print("You found a boat!")


if place == "cave":   
    action == input("Light a torch? Or proceed in the dark?")
    if action == "light a torch":
        print("You now have a light to proceed through the tunnel!")
    if action == "return" or "neither":
         pass
else:
        print("Good luck! Be careful in the dangerous dark cave!")

