# Set the base case to return 0 if that is what n is, and the error message if n is a negative number
def sum_to(n):
    if n == 0:
        return 0
    elif n < 0:
        return None

    # Here, the recursive iteration through n is adding up its reciprocals until the value reaches 1
    else:
        return 1/n + sum_to(n-1)


# Then tested the program with some values that pertain to each if statement
def main():
    print(sum_to(2))
    print(sum_to(3))
    print(sum_to(0))
    print(sum_to(-12))
main()


 # print("Error")
