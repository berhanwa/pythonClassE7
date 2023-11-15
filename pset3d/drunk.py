import random

# end_block variable HOME if 1
# end_block variable JAIL if 11


def drunk_walk():
    current_block = 6
    steps = 0

    # block = random.randint(1, 11)
    while current_block != 1 and current_block != 11:

        # The student randomly wanders either up or down a block, so the rand range function here yields either -1 or 1
        wander = random.randrange(-1, 2, 2)
        # The current block she's at gets updated to the block that she wanders to
        current_block += wander
        steps += 1

    return steps
print (steps)

            # if block == 1:
            #     print ("HOME")
            # elif block == 11:
            #     print ("JAIL")
            # break


#   # steps ==
#         # simulates drunk walk
#         # starts at 6, can randomly go either down to 1 or up to 11

# def main():
#     # this process is repeated N times
#     for i in range (N):
#         steps = drunk_walk
