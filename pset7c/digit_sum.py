# Step one: Make the function work as needed
# Step two: Now make it recursive

def digit_sum(n):

    if n < 10:
        return n

    elif n > 10:
        # Turned n to a string and assigned it to variable in order to iterate through it
        total = str(n)
        # Then turned the indices within total into a list of integers, in order to use the sum function
        digits = [int(i) for i in total]

        return digit_sum(digits[1:])

# Supposed to make it recursive by removing an index until n meets base case
    # else:
    #     return digit_sum(digits[1:])

print(digit_sum(3456))


# def digit_sum(n):

#     if n < 10:
#         return n

#     else:
#         # Turned n to a string and assigned it to variable in order to iterate through it
#         total = str(n)
#         # Then turned the indices within total into a list of integers, in order to use the sum function
#         digits = [int(i) for i in total]

#         return sum(digits)

# # Supposed to make it recursive by removing an index until n meets base case
#     else:
#         return digit_sum(digits[1:])





# def digit_sum(n):

#     total = 0

#     if n < 10:
#         return n
#     else:
#         for digit in n:
#                 total += int(digit)
#         return total
