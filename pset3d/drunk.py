import random

# end_block variable HOME if 1
# end_block variable JAIL if 11



# The student randomly wanders either up or down a block, so the rand range function here yields either -1 or 1
wander = random.randrange(-1, 2, 2)

def drunk_walk():
    start_block = 6
    steps = 0

    # block = random.randint(1, 11)
    while start_block != 1 and start_block != 11:
            if block == 1:
                print ("HOME")
            elif block == 11:
                print ("JAIL")
            break

    return block
print (block)

#   # steps ==
#         # simulates drunk walk
#         # starts at 6, can randomly go either down to 1 or up to 11

# def main():
#     # this process is repeated N times
#     for i in range (N):
#         steps = drunk_walk
