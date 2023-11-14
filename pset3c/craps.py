import random

# do_roll() function 'rolls' the dice
def do_roll():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    print_roll(roll_1, roll_2)
    return roll_1 + roll_2

# print_roll() function prints the results of the rolls
def print_roll(roll_1, roll_2):
    print (f"Computer rolls a {roll_1} and a {roll_2}, for a total of {roll_1 + roll_2}.")

# get_point() function finds the point for the first round and returns it (first while loop is used here)
def get_point():
    point = 0

    while True:
        roll = do_roll()

#       Conditions for point to be met
        if roll >= 4 and roll != 7 and roll <= 10:
            point = roll
            break

    return point

# play_from_point() function calculates if a roll results in a win or a loss by using Boolean logic (second while loop is used here)
def play_from_point(point):
    while True:
        roll = do_roll()

#       returns loss
        if roll == 7:
            return False

#       returns win
        if roll == point:
            return True

# game() wraps everything up and prints the results of whether the rolls' sum results in a point (win) or a 7 (loss)
def game():
    point = get_point()
    print (f"{point} is now the established POINT.")
    if play_from_point(point):
        print ("YOU WIN")
    else:
        print ("YOU LOSE")


# Called the game function
game ()
