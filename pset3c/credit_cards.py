# The last digit of a credit card is check digit

# From right -> left, find the sum of every other digit

card_number = int(input('Provide your credit card number: '))
alt_sum = 0
double = 0


def check(card_number):
    digits = []
    for d in str(card_number):
        digits.append(int(d))

    # Saving the 8th digit since arrays start from 0 with len(digits)-1
    check_digit = digits[len(digits)-1]

    print(digits)
    print(f"Check digit: {check_digit}")

    sum_odds = 0
    doubles = []
    sum_double = 0
    odds = []

    # Finding the sum of every other digit (odds)
    for i in range (1,9):
        if i % 0 != 0:
            alt_sum += i
        else:
            double += i
        card_number = card_number//10

    total_sum(alt_sum, double):
        return ()

    doubles_sum = (2 * double):


#     return (n + 1) * n // 2
