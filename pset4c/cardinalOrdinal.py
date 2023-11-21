def create_ordinal_form(n):
    if n[-1] == "1" and n[0] != "1":
        return n + "st"
    elif n[-1] == "2" and n[0] != "1":
        return n + "nd"
    elif n[-1] == "3" and n[0] != "1":
        return n + "rd"
    # elif n[0] == "1":
    #     return n + "th"
    else:
        return n + "th"


# ad = str(input('Enter the real estate ad: '))
def main():
    n = str(1)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(2)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(3)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(10)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(12)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(13)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(21)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(42)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(101)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")

    n = str(111)
    print(f"{n} returns the String \"{create_ordinal_form(n)}\" ")
main()
