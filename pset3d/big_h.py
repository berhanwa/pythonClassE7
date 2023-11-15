def print_h_block(size):

    if size < 1 or size > 10:
        print("Please enter a number between 1 and 10.")
        return

    for i in range(2*size + 1):
        if i == size :
            for j in range(i):
                print('*' * size + '*' )
