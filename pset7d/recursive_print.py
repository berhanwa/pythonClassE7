# Started by assigning variables to lists by decimal type
def print_number(n):
    ones_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_numbers = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_numbers = ["", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if n < 0:
        print("minus", end = " ")
        n = abs(n)

    if n < 10:
        print(ones_numbers(n), end = " ")

    if n == 10:
        print(tens_numbers(n - 10 + 1), end = " ")

    elif n < 20:
        print(teens_numbers(n - 10), end = " ")

    elif n < 100:
        print(tens_numbers[n // 10], end = " ")
        print_number(n % 10)

    elif n < 1000:
        print_number(n // 10)
        print("hundred", end = " ")
        print_number(n % 100)

    elif n < 1000000:
        print_number(n // 1000)
        print("thousand", end = " ")
        print_number(n % 1000)

    elif n < 1000000000:
        print_number(n // 1000000)
        print("million", end = " ")
        print_number(n % 1000000)

    elif n < 1000000000000:
        print_number(n // 1000000000)
        print("billion", end = " ")
        print_number(n % 1000000000)

# print(print_number(143))
print_number(143)
print()
