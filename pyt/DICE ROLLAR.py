#Rolling the dice
import random
min = 1
max = 6
roll_again =input("Roll the dice!yes or no")
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    roll_again =input("Roll the dice again?")
