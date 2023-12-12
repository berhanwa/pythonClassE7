# Modified the function so that the print statment with the []s gets printed out BEFORE the recursion happens
def print_triangle (sideLength):
    print ( "[]"* sideLength)

    # Here, I retained the recursion that allows the []s to be printed out all the way until sideLength reaches 0
    if sideLength < 1 :
        return
    print_triangle (sideLength-1)


print(print_triangle (4))
