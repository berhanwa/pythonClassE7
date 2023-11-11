x = int(input('Enter the first number:'))
y = int(input('Now enter the second number:'))

def print_range (x,y):
    for i in range(x, y + 1):
        if x == y:
            print (x)
        elif x < y:
                print (i+1)
        else:
            print (x=x-1)

print_range(x,y)

    # while x < y:
    #     print (x += 1)
