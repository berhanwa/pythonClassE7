from sys import argv

def main():

    argv
    # result_sum = sum([for _ in argv])

    result_sum = [sum(n) for n in argv]

    # for _ in argv:
    print(result_sum)

    # print(f"The sum of the args is:", sum(argv))

    # for i in argv:
    #     print(i)

main()
