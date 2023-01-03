# ACaffeinatedCoder's Basic Console Python Dice Roller
# Structure:
#   user input dice sides
#   user input must not be less or equal to 1
#   output random number between and including 1 and user input
#   add loop breaking option
#   catch value error exception
#   loop
import random

while True:
    try:
        sides = int(input("Dice Sides: "))
        if sides <= 1:
            print("Invalid amount of sides. You must have 2 or more sides. Please try again.")
            continue
        else:
            while True:
                roll = input("Input 'r' to roll the dice, any character to stop: ")
                roll = roll.lower()
                if roll == 'r':
                    rolled = random.randint(1, sides)
                    print("You rolled " + str(rolled))
                else:
                    break
        reset = input("Input 'r' to reset sides, any character to exit: ")
        reset = reset.lower()
        if reset == 'r':
            continue
        else:
            break
    except ValueError:
        print("You made an invalid input. The sides input must only be numerical characters. Please try again.")
print("Thank you for using the program.")
