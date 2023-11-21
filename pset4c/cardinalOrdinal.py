def create_ordinal_form(n):
    if n[-1] == "1":
        return n + "st"
    elif n[-1] == "2":
        return n + "nd"
    elif n[-1] == "3":
        return n + "rd"
    else:
        return n + "th"

# ad = str(input('Enter the real estate ad: '))
def main():
    n = str(1)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    # n = str(2)
    # print(f"{n} returns the String {create_ordinal_form(n)}")

    # n = str(3)
    # print(create_ordinal_form(n))

main()
