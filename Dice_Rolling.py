#import the Required module
import random

# Dice value ranges
min_val = 1
max_val = 6

roll = 'yes'

while roll == 'yes' or roll == 'y':
    print("Rolling the Dices...")
    
    #Generate the Value for Dice 1 by Dice range
    dice1 = random.randint(min_val,max_val)
    print("the value of Dice 1 is ",dice1 )

    #Generate the Value for Dice 2 by Dice Range
    dice2 = random.randint(min_val,max_val)
    print("the value of Dice 2 is ",dice2)

    #total values of Both Dice
    print("the Total Value of Both Dice is ",dice1 + dice2)

    #Asking user to Play Again or Not 
    roll = input("Can you Roll the Dice Again? (y/n): ").lower()

    if roll != 'y' or roll != 'yes':
        print("Thank you!")
