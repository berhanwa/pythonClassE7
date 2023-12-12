def digit_sum(n):
    # Base case - if n is a single digit, the function just returns n itself
    if n < 10:
        return n

    # If not, then the sum of the values within n is calculated by adding last digits of n (found by n % 10) that were collected after recursively iterating through the digits of n
    else:
        return n % 10 + digit_sum(n // 10)


# Tested the program with some example 1, 2, 3, and 4-digit integer values
def main():
    print(digit_sum(3))
    print(digit_sum(23))
    print(digit_sum(345))
    print(digit_sum(3456))
main()
