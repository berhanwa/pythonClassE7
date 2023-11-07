height = int(input('How tall do you want the pattern to be:'))

# n =

for i in range (1, height+1):
    print ('*' * height)
for i in range (height, 0, -1):
    print (" " * (height - i) + "*" * i)
# width = height -
