# roll_1 = int(input('Roll the first die! '))
# roll_2 = int(input('Now roll the second die! '))

# from random import *
import random

# roll 2 dice
def do_roll():
    roll_1 = random.randint(1, 7)
    roll_2 = random.randint(1, 7)
    # print (roll_1)
    # print (roll_2)
    return roll_1 + roll_2

print (do_roll())

def print_roll(roll_1, roll_2):
 if do_roll = 4 or 5 or 6 or 8 or 9 or 10:
    do_roll = point
 else do_roll = 7
    print ("YOU LOSE")



# def get_point():
#     takes no input
#     rolls until point is est
#     return val of point

# def play_from_point(point):
#     takes point val
#     cont game until W or L
#     take bool for ^

# print ("Computer rolls a", roll_1 "and a" roll_2 "for a total of" )
# # use 2 separate while loops for this game
