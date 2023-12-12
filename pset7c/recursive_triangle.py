def print_triangle (sideLength):
    if sideLength < 1 :
        return
    print_triangle (sideLength-1)
    print ( "[]"* sideLength)

print(print_triangle (4))
