def print_h(size):

    # Setting the parameters to ensure users only submit a value between 1 and 10 in order to see an 'H'
    if size < 1 or size > 10:
        print("Please enter a number between 1 and 10.")
        return

    # Setting the parameters to ensure users only submit a value between 1 and 10 in order to see an 'H'
    for i in range(2*size + 1):
        if i == size :

             # Prints middle row as many times as size is set to
            for j in range(i):

                # Set * 3 times because the least amount of size will yield 3 rows
                # Middle row has * as the middle column instead of ' '
                print('*' * size + '*' * size + '*' * size)

         # Prints * and ' ' as many times as size is set to
        else:
            print('*' * size + ' ' * size + '*' * size)


user_input = int(input("Please enter a number between 1 and 10 for the size of the letter 'H' "))
print_h(user_input)
