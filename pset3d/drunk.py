import random


def drunk_walk():
    current_block = 6
    total_blocks_walked = 0

    # block = random.randint(1, 11)
    while current_block != 1 and current_block != 11:

        # The student randomly wanders either up or down a block, so the rand range function here yields either -1 or 1
        wander = random.randrange(-1, 2, 2)
        # The current block she's at gets updated to the block that she wanders to
        current_block += wander
        total_blocks_walked += 1

    print (f"Took {total_blocks_walked} steps, and")

    # Setting the conditions where it says if the student ended up at home (1) or at the jail (11, or else in this case)
    if current_block == 1:
        print("Landed at HOME")
    else:
        print("Landed at JAIL")

    return total_blocks_walked



def main():
    N = 5
    total_steps = 0
    average_steps = 0

    # Finding out how many times (N) the student walked
    for i in range (N):
        print("Here we go again... time for a walk!")
        total_steps += drunk_walk()

        average_steps = total_steps / N
        print (f"Average # of steps equals {round(average_steps, 1)}")

            # if block == 1:
main()

# end_block variable HOME if 1
# end_block variable JAIL if 11
