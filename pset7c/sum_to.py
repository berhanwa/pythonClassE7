def sum_to(n):
    if n == 0:
        return 0
    else:
        return 1 + ( 1 / sum_to(n-1))

print(sum_to(2))
