####  Attempted this problem for extra credit  ####


# Started by assigning variables to lists by decimal type
def print_number(n):
    # ones_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_numbers = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    first_twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                    "eighteen", "nineteen"]
    # teens_numbers = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    # In this if statement part, defined the different digit lengths and assigned the appropriate variable from above and what should be printed out
    if n < 0:
        print("negative", end = " ")
        n = abs(n)

    if n < 20:
        print(first_twenty[n], end=" ")

    elif n < 100:
        print(tens_numbers[n // 10], end=" ") # Print the tens
        print_number(n % 10) # Print the ones
        
    elif n < 1000:
        print_number(n // 100) # Print the hundreds
        print("hundred", end=" ")
        print_number(n % 100) # Print the rest

    elif n < 1000000:
        print_number(n // 1000) # Print the thousands
        print("thousand", end=" ")
        print_number(n % 1000) # Print the rest

    elif n < 1000000000:
        print_number(n // 1000000) # Print the millions
        print("million", end=" ")
        print_number(n % 1000000)

    # Attempted extra credit portion by factoring numbers larger than a million into the program
    elif n < 1000000000000:
        print_number(n // 1000000000)
        print("billion", end = " ")
        print_number(n % 1000000000)


# Then printed out some values to test the program
print(f"{print_number(143)} ")
print(f"{print_number(-3)} ")
print(f"{print_number(2002)} ")
print(f"{print_number(10)} ")


    # elif 10 <= n < 20:
    #     print(teens_numbers[n - 10], end = " ")
