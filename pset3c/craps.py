# roll_1 = int(input('Roll the first die! '))
# roll_2 = int(input('Now roll the second die! '))


# roll 2 dice
def do_roll():
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    return roll_1 + roll_2

print (do_roll())

# def print_roll(roll_1, roll_2):
#     print ()

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
