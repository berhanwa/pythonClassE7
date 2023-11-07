# Started by asking user to input the number that will determine both the height and width of the pattern
height = int(input('How tall do you want the pattern to be:'))

# Then used the range function to set the rows to go down in descending order
# and inside the loop, the negative space " " is printed out as many times as height-i of the range
# and this is concatenated with the number of * that i specifies per row
for i in range (height, 0, -1):
    print (" " * (height - i) + "*" * i)
