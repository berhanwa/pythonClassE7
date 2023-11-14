import random

# end_block variable HOME if 1
# end_block variable JAIL if 11

start_block = 6

def drunk_walk():

    block = random.randint(1, 11)
        while True:
            if block == 1:
                print ("HOME")
            elif block == 11:
                print ("JAIL")
            break

    return block

#   # steps ==
#         # simulates drunk walk
#         # starts at 6, can randomly go either down to 1 or up to 11
#         return total blocks walked

# def main():
#     # this process is repeated N times
#     for i in range (N):
#         steps = drunk_walk
