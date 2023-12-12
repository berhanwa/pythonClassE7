# Set the base case to return 0 if that is what n is, and the error message if n is a negative number
def sum_to(n):
    if n == 0:
        return 0
    elif n < 0:
        return None

    # Here, 
    else:
        return 1/n + sum_to(n-1)


def main():
    print(sum_to(2))
    print(sum_to(3))
    print(sum_to(0))
    print(sum_to(-12))
main()


 # print("Error")
