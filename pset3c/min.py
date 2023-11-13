x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))


# Returns the integer that has the smallest value between x, y, and z.
def my_min(x, y, z):
    if (x < y and x < z):
        return x
    elif (y < x and y < z):
        return y
    else:
        return z
    
my_min(x, y, z)
    # else (z < x and z < y):
    #     return z
