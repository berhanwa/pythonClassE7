from sys import argv

def main():
    # print([argv])
    for i in argv:
        print(i)
    # print(f"The sum of the args is:", sum((int(argv))))

main()
