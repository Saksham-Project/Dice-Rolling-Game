'''
Dice rolling game
'''

import random

while True:
    dice = random.randint(1,6)
    user_choice = input("Roll the dice 'y' for continuing and 'n' for stop the game(y/n):")
    if user_choice.lower() == 'y':
        print(f"you rolled a 🎲... and it's a {dice}.")
        if dice == 6:
            print("Jackpot! 🎉 You hit the highest number!")
        elif dice == 1:
            print("Oof, just a 1. Better luck next roll.")
    elif user_choice.lower() == 'n':
        break
    else:
        print("Invalid Choice. Please enter 'y' or 'n'. ")
        continue