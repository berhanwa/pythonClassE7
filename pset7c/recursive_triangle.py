

Modified the function so that the print statment with the []s gets printed out BEFORE the recursion happens
def print_triangle (sideLength):
    print ( "[]"* sideLength)
    if sideLength < 1 :
        return
    print_triangle (sideLength-1)

print(print_triangle (4))
