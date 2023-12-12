####  Attempted this problem for extra credit  ####


# Started by assigning variables to lists by decimal type
def print_number(n):
    ones_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_numbers = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_numbers = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if n < 0:
        print("negative", end = " ")
        n = abs(n)

    if n < 10:
        print(ones_numbers[n], end = " ")

    if n == 10:
        print(tens_numbers[n - 10 + 1], end = " ")

    elif n < 20:
        print(teens_numbers[n - 10], end=" ")

    elif n <= 100:
        print(tens_numbers[n // 10], end = " ")
        print_number(n % 10)

    elif n < 1000:
        print(ones_numbers[n // 100], "hundred", end = " ")
        print_number(n % 100)

    elif n < 1000000:
        # print_number(n // 1000)
        print(ones_numbers[n // 1000], "thousand", end = " ")
        print_number(n % 1000)

    elif n < 1000000000:
        print_number(n // 1000000)
        print("million", end = " ")
        print_number(n % 1000000)

    # Attempted extra credit portion by factoring numbers larger than a million into the program
    elif n < 1000000000000:
        print_number(n // 1000000000)
        print("billion", end = " ")
        print_number(n % 1000000000)

        

print(f"{print_number(143)} ")
print(f"{print_number(-3)} ")
# print_number(143)
# print_number(-3)
# print_number(2003)



    # elif 10 <= n < 20:
    #     print(teens_numbers[n - 10], end = " ")
