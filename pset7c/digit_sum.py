def digit_sum(n):

    total = 0

    if n < 10:
        return n

    else:
        for digit in n:

        return digit_sum(n)


print(digit_sum(3456))



# def digit_sum(n):

#     total = 0

#     if n < 10:
#         return n
#     else:
#         for digit in n:
#                 total += int(digit)
#         return total
