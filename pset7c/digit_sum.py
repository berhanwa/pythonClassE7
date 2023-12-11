def digit_sum(n):

    total = 0

    if n < 10:
        return n
    else:
        for digit in range(n):
                int(digit) += total
            return total


print(digit_sum(3456))
