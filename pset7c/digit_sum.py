# Step one: Make the function work as needed
# Step two: Now make it recursive

def digit_sum(n):

    # Base case - if n is a single digit, the function just itself
    if n < 10:
        return n

    # If not, then the sum of n is calculated by adding last digit of n (found by n % 10) that were collected after recursively iterating through the digits of n
    else:
        return n % 10 + digit_sum(n // 10)


# Tested the program with some example 1, 2, 3, and 4-digit integer values
def main()
    print(digit_sum(3))
    print(digit_sum(23))
    print(digit_sum(345))
    print(digit_sum(3456))
main()

    # If not, then the sum of n is calculated by adding last digit of n (found by n % 10) recursively onto the function after the last digit is removed (by n // 10)





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
