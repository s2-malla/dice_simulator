#### This progam is created as a part of learning a basic course in python.

# import random module
import random

# since we don't know how many time user wants to
# roll the dice, it is prefered to use infnite loop
while True:
    #generates random number between 1 and 6 inclusive
    x = random.randint(1,6)
    # using conditional for 6 different cases
    if x == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")
    if x == 2:
        print("-----------")
        print("|         |")
        print("|   0  0  |")
        print("|         |")
        print("-----------")
    if x == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")
    if x == 4:
        print("-----------")
        print("| 0    0  |")
        print("|         |")
        print("| 0    0  |")
        print("-----------")
    if x == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")
    if x == 6:
        print("-----------")
        print("|  0   0   |")
        print("|  0   0   |")
        print("|  0   0   |")
        print("-----------")
    # takes user input after the structure is printed
    user_input = input ("Would you like to continue?[Y/N]")
    if user_input == "Y" or "y" or "yes":
        # continues looping through and printing the new result
        continue
    else:
        # breaks the program if user does not want to continue. 
        break
        print("Thank you for using dice simulator")
