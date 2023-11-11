x = int(input('Enter the first number:'))
y = int(input('Now enter the second number:'))

# Defined the print range function that prints the first number if it's the same as the second, prints an increasing sequence if the first number is greater than the second or a decreasing sequence if the opposite is true
def print_range (x,y):
        if x == y:
            print (x)
        else:
           increment = 1 if x < y else -1

        for i in range (x, y + 1, increment):
                print (i)

print_range(x,y)

# These were my previous attempts that didn't get me right the sequences
# def print_range (x,y):
#         if x == y:
#             print (x)
#         elif x < y:
#             for i in range(x, y + 1):
#                 print (i)
#         else:
#             print (i-1)

# print_range(x,y)


# def print_range (x,y):
#     for i in range(x, y + 1):
#         if x == y:
#             print (x)
#         elif x < y:
#             print (i+1)
#         else:
#             print (i-1)

# print_range(x,y)
