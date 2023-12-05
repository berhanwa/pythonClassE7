from sys import argv

def main():

    # With list comprehension, got argv converted to int and excluded the 0th index which has the script name as the value
    ints = [int(argv) for argv in argv[1:]]

    # And then used a second variable that is responsible for finding the sum of the values of from the ints variable
    result_sum = sum(ints)
    # for _ in argv:
    print(result_sum)

main()
