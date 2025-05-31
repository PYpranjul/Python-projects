import random
a=["Snake","Water","Gun"]
Human=input("Enter Your Choice: ")
Computer=random.choice(a)
print("Computer choice  is",Computer)
def check (Human,Computer):
    if Human==Computer:
        return "it's a tie"
    elif Human=="Snake" and Computer=="Water":
        return "Human Wins"
    elif Human=="Snake" and Computer == "Gun":
        return "Computer Wins"
    elif Human=="Water" and Computer=="Snake":
        return "Computer Wins"
    elif Human=="Water" and Computer=="Gun":
        return "Human Wins"
    elif Human=="Gun" and Computer=="Snake":
        return "Human Wins"
    elif Human=="Gun" and Computer=="Water":
        return "Computer Wins"
    else:
        return "Invalid Input"
    
print(check(Human,Computer))
    