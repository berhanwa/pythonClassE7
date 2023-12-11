def digit_sum(n):
    if n < 10:
        return n
    else:
        for i in range(n):
            return sum(i)


print(digit_sum(3456))
