import random

# end_block variable HOME if 1
# end_block variable JAIL if 11


def drunk_walk():
    current_block = 6
    total_blocks_walked = 0

    # block = random.randint(1, 11)
    while current_block != 1 and current_block != 11:

        # The student randomly wanders either up or down a block, so the rand range function here yields either -1 or 1
        wander = random.randrange(-1, 2, 2)
        # The current block she's at gets updated to the block that she wanders to
        current_block += wander
        steps += 1
    print (steps)
    return steps



def main():
    N = 0
    total_steps = 0
    average_steps = 0

    # Finding out how many times (N) the student walked
    for i in range (N):
        total_steps += drunk_walk()

    average_steps = total_steps / N
    print (f"Landed at {current_block}")

            # if block == 1:
            #     print ("HOME")
            # elif block == 11:
            #     print ("JAIL")
            # break
