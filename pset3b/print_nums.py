x = int(input('Enter the first number:'))
y = int(input('Now enter the second number:'))

def print_range (x,y):
        if x == y:
            print (x)
        elif x < y:
            for i in range(x, y + 1):
                print (i)
        else:
            print (i-1)

print_range(x,y)

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
