def check(num):
    multiple = num * 4
    reversed_number = 0

    while multiple > 0:
        digit = multiple % 10
        reversed_number = (reversed_number * 10) + digit
        # to remove the last digit
        multiple //= 10

    if reversed_number == num:
        return True
    else:
        return False

def main():

    for i in range(1000, 100000):
        if check(i):
            print(i)

main()
