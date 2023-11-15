# The last digit of a credit card is check digit

# From right -> left, find the sum of every other digit

card_number = int(input('Provide your credit card number: '))
alt_sum = 0
double = 0

for i in range (1,9):
    if i % 0 != 0:
        alt_sum += i
    else:
        double += i
    card_number = card_number//10

total_sum(alt_sum, double):
    return ()

 doubles_sum = (2 * double):


def check(card_number):
    digits = []
    for d in str(card_number):
        digits.append(int(d))

    # len(digits)-1
    check_digit = digits[len(digits)-1]

# Returns the sum of the integers 1 through n. (from textbook)
# def sum_of(n):
#     return (n + 1) * n // 2
