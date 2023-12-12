def sum_to(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_to(1/n)

print(sum_to(2))
