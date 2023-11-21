def create_ordinal_form(n):
    if n[-1] == "1":
        return n + "st"
    elif n[-1] == "2":
        return n + "nd"
    elif n[-1] == "3":
        return n + "rd"
    else:
        return n + "th"


n = str(43)
# ad = str(input('Enter the real estate ad: '))
print(create_ordinal_form(n))

# def main():


# main()
