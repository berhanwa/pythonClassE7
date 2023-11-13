# Started by assigning the input values to x, y, and z respectively.
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))

# Defined the function to return the integer with the smallest value between x, y, and z.
def my_min(x, y, z):
    if (x < y and x < z):
        return x
    elif (y < x and y < z):
        return y
    else:
        return z

# Then used print to actually show what the return from the function will be.
print (my_min(x, y, z))


# Removed this code from the if/else since it is implied
    # else (z < x and z < y):
    #     return z
