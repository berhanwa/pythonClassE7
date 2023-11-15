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
# if 2 * double results in a double digit number, then split up into single digits i.e. 18 becomes 1 and 8. Then need to sum everything up together

def check(card_number):
    digits = []
    for d in str(card_number):
        digits.append(int(d))

# Returns the sum of the integers 1 through n. (from textbook)
# def sum_of(n):
#     return (n + 1) * n // 2
