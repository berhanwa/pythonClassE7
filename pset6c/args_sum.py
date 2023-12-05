from sys import argv

def main():

    argv
    result_sum = []
    
    for _ in argv:
        print(sum(argv))

    print(f"The sum of the args is:", sum(argv))

    # for i in argv:
    #     print(i)

main()
