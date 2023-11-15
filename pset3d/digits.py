def check(num):
    multiple = num * 4
    reversed_number = 0

    # Reverses the number
    while multiple > 0:
        digit = multiple % 10
        reversed_number = (reversed_number * 10) + digit
        # to remove the last digit
        multiple //= 10

    # Checks if the reversed number is the same as the original number
    if reversed_number == num:
        return True
    else:
        return False

def main():

    # Finds the five digit numbers that match the criteria of the check function
    for i in range(1000, 100000):
        if check(i):
            print(i)

main()
