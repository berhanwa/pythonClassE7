import random

# do_roll() function 'rolls' the dice
def do_roll():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    print_roll(roll_1, roll_2)
    return roll_1 + roll_2

# print_roll() function prints the results of the rolls
def print_roll(roll_1, roll_2):
    print (f"Computer rolls a {roll_1} and a {roll_2} )


# def get_point():

#     # while True:

#     if roll_sum == 4 or 5 or 6 or 8 or 9 or 10:
#         roll_sum = int(point)
#     elif do_roll() == 7:
#         return 0   # stop immediately
#         # print ("YOU LOSE")

#     takes no input
#     rolls until point is est
#     return val of point


# def play_from_point(point):
#     while point != 7:
        # keep playing

#     takes point val
#     cont game until W or L
#     take bool for ^

# print ("Computer rolls a", roll_1 "and a" roll_2 "for a total of" )
# # use 2 separate while loops for this game
