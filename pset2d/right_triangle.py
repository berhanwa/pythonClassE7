# Started by asking user to input the number that will determine both the height and width of the pattern
height = int(input('How tall do you want the pattern to be:'))

# n =
for i in range (height, 0, -1):
    print (" " * (height - i) + "*" * i)
