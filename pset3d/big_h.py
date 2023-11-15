def print_h_block(size):

    # Setting the parameters to ensure users only submit a value between 1 and 10 in order to see an 'H'
    if size < 1 or size > 10:
        print("Please enter a number between 1 and 10.")
        return

    # Setting the parameters to ensure users only submit a value between 1 and 10 in order to see an 'H'
    for i in range(2*size + 1):
        if i == size :
            for j in range(i):
                print('*' * size + '*' * size + '*' * size)

        else:
            print('*' * size + ' ' * size + '*' * size)


user_input = int(input("Please enter a number (1-10) for the size of the letter 'H'"))
print_h_block(user_input)
